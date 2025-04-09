from langchain.llms import OpenAI 
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain 
from langchain.tools import Tool 
from langchain.agents import initialize_agent 
from langchain.agents import AgentType 
import os 

os.environ['OPENAI_API_KEY'] = ""

llm = OpenAI(temperature = 0.0)




def get_generic_recommendations(query : str): 
    """Returns a few generic recommendations based on the query""" 

    if "smartphone" in query:
        return "Based on 'smartphone', you might like the iPhone 16, Samsung Galaxy S25, or Google Pixel 9."
    elif "chair" in query:
        return "For 'chair', consider the Herman Miller Aeron, IKEA Markus, or a comfortable gaming chair."
    elif "book" in query:
        return "If you're looking for a 'book', you might enjoy 'Project Hail Mary', 'The House in the Cerulean Sea', or 'Sapiens'."
    else:
        return "I can provide more specific recommendations if you tell me what kind of product you're looking for."

tools = [
    Tool(
        name = "get_generic_recommendations", 
        func = get_generic_recommendations, 
        description = "Provides generic product recommendations based on keywords. "
    )
]


template = """ 
You are a helpful recommendation assistant. 
You have access to a product recommendation tools {tool_descriptions}.
use the following format. 
Thought: You should always think what to do. 
Action: the action to take should be one of [{tool_names}]. 
Action Input: The input to the action.
Observation: The result of action. 
... (This Thought/Action/Action Input/Observation can repeat 3 times)
Thought: I now know the final answer. 
Final asnwer: Here are some product recommendations based on your request: {final_answer}

Begin!

Input: {input} 
{agent_scratchpad}
"""

prompt = PromptTemplate(
    template = template, 
    input_variables = ['input', 'agent_scratchpad', 'tool_names', 'tool_descriptions', 'final_answer']
)


agent = initialize_agent(
    llm = llm, 
    tools = tools, 
    agent = AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
    verbose = True
)

user_input = input("Tell me what type of product are you looking for:")

response = agent.run(user_input) 

print(response)

