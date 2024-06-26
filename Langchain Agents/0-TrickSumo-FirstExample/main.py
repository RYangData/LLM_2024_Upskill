from langchain_core.prompts import PromptTemplate
# from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool, AgentType

from langchain_openai import AzureOpenAI
from langchain_openai import AzureChatOpenAI

from langchain.utilities import SerpAPIWrapper

from tool import is_prime
from dotenv import load_dotenv
load_dotenv()

prompt_template = PromptTemplate.from_template("""{num} is not a prime number, right?
                                               If number is prime number, then tell me what is 
                                               the rebranded name of twitter? 
                                               """)

chat_model = AzureChatOpenAI(
    streaming=True,
    azure_endpoint="https://gt-dse-openai.openai.azure.com/",
    api_key="a92828e9ec0b4860abd015cb22b01136",
    azure_deployment="gt-dse-gpt-35-turbo",
    openai_api_version="2023-03-15-preview",
)

serp = SerpAPIWrapper()
print(serp.run("What is mysql?")
      )


agent_tools = [
    Tool.from_function(name="Prime number checker",
                       func=is_prime,
                       description="this tool helps to figure out if number is prime or not"
                       ),

    Tool.from_function(name = "serp API google search",
                       func=serp.run, 
                       description="tool to do google search engine search"
                       )
]

agent = initialize_agent(tools=agent_tools, 
                         llm=chat_model, 
                         agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
                         verbose=True)

res = agent.run(prompt_template.format_prompt(num=49721450073))
print(res)