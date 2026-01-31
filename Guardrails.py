# Required imports
import os
from dotenv import find_dotenv, load_dotenv
from agents import (
    Agent, 
    OpenAIChatCompletionsModel, 
    AsyncOpenAI, 
    Runner, 
    function_tool, 
    trace,
    GuardrailFunctionOutput, 
    InputGuardrailTripwireTriggered, 
    input_guardrail, 
    RunContextWrapper, 
    TResponseInputItem
)

# Load environment variables from the .env file
load_dotenv(find_dotenv()) 

# Access the API key
# 1. Which LLM Provider to use? -> Google Chat Completions API Service
external_client: AsyncOpenAI = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# 2. Which LLM Model to use?
llm_model: OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash", # Adjusted to a standard Gemini model name
    openai_client=external_client
)

# Create a tool
@function_tool()
def get_order_status(orderID: int) -> str:
    """
    Returns the order status given an order ID
    Args:
        orderID (int) - Order ID of the customer's order
    Returns:
        string - Status message of the customer's order
    """
    if orderID in (100, 101):
        return "Delivered"
    elif orderID in (200, 201):
        return "Delayed"
    elif orderID in (300, 301):
        return "Cancelled"
    return "Order ID not found"

# Create a guardrail
@input_guardrail
def complaint_detector_guardrail(
    ctx: RunContextWrapper[None],
    agent: Agent,
    prompt: str | list[TResponseInputItem]
) -> GuardrailFunctionOutput:

    tripwire_triggered = False

    # Ensure prompt is treated as a string for the check
    content = str(prompt)
    if "complaint" in content.lower():
        tripwire_triggered = True

    return GuardrailFunctionOutput(
        output_info="The word Complaint has been detected",
        tripwire_triggered=tripwire_triggered,
    )

# Define an agent
agent = Agent(
    name="Customer service agent",
    instructions="You are an AI Agent that helps respond to customer queries for a local paper company",
    model=llm_model, # Removed the redundant model="gpt-4o"
    tools=[get_order_status],
    input_guardrails=[complaint_detector_guardrail]
)

# Simple loop to interact with the agent
with trace("Input Guardrails"):
    while True:
        try:
            question = input("You: ")
            if question.lower() in ["exit", "quit"]:
                break
                
            # The runner executes the agent logic
            result = Runner.run_sync(agent, question)
            print("Agent: ", result.final_output)
            
        except InputGuardrailTripwireTriggered :
            print(f"System: Input blocked by guardrail. Reason:")
       