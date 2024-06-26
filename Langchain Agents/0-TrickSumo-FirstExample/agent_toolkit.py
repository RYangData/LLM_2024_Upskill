from langchain_experimental.agents.agent_toolkits import create_python_agent
from langchain.agents import AgentExecutor, create_react_agent

from langchain.agents import Tool
from langchain_experimental.utilities import PythonREPL
from langchain_experimental.tools import PythonREPLTool
from langchain_openai import AzureChatOpenAI

from dotenv import load_dotenv
load_dotenv()


chat_model = AzureChatOpenAI(
    streaming=True,
    azure_endpoint="https://gt-dse-openai.openai.azure.com/",
    api_key="a92828e9ec0b4860abd015cb22b01136",
    azure_deployment="gt-dse-gpt-4-turbo",
    openai_api_version="2023-03-15-preview",
    temperature = 0.8
)


python_repl = PythonREPL()

# You can create the tool to pass to an agent
repl_tool = Tool(
    name="python_repl",
    description="A Python shell. Use this to execute python commands. Input should be a valid python command. If you want to see the output of a value, you should print it out with `print(...)`.",
    func=python_repl.run,
)

tools = [repl_tool]

from langchain import hub
prompt = hub.pull("hwchase17/react")
# prompt = """Load the data.csv file, evaluate expression in first column and save it to the second column.
#      Do this for all rows and save new file as solved.csv
#     """


# prompt = """Answer the following questions as best you can. You have access to the following tools:

# {tools}

# Use the following format:

# Question: the input question you must answer
# Thought: you should always think about what to do
# Action: the action to take, should be one of [{tool_names}]. 
# Action Input: the input to the action
# Observation: the result of the action
# ... (this Thought/Action/Action Input/Observation can repeat N times)
# Thought: I now know the final answer
# Final Answer: the final answer to the original input question

# Begin!

# Question: {input}
# Thought:{agent_scratchpad}"""


python_agent = create_react_agent(chat_model, 
                                   tools,
                                    # verbose = True,
                                    prompt
                                    )

# res = python_agent.run(
#     "What is the 10th fibonacci number"
# )

# res = python_agent.run(
#    """Load the data.csv file, evaluate expression in first column and save it to the second column.
#     Do this for all rows and save new file as solved.csv
#    """
# )


agent_executor = AgentExecutor(agent=python_agent, 
                                tools=tools,
                                handle_parsing_errors=True,
                                verbose=True,
                                max_iterations=3)

agent_executor.invoke(
    {"input": """Load the data.csv file, evaluate expression in first column and save it to the second column.
     Do this for all rows and save new file as solved.csv
    """}
)


# print(res)