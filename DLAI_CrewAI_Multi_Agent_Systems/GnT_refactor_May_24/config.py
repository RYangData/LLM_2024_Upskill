import os

from dotenv import load_dotenv

from functools import lru_cache

load_dotenv()


#TODO: replace config = Config with this, add pydantic singleton
@lru_cache
def get_config():
    return Config()


class Config:
    AZURE_OPENAI_API_KEY = os.environ["AZURE_OPENAI_API_KEY"]
    AZURE_OPENAI_ENDPOINT = os.environ["AZURE_OPENAI_ENDPOINT"]
    # AZURE_OPENAI_API_KEY = os.environ["AZURE_OPENAI_API_KEY_US_WEST"]
    # AZURE_OPENAI_ENDPOINT = os.environ["AZURE_OPENAI_ENDPOINT_US_WEST"]

    AZURE_GPT_35 = "gt-dse-gpt-35-turbo"
    AZURE_GPT_35_turbo_16k="gpt-35-turbo-16k"
    AZURE_GPT4 = "gt-dse-gpt-4"
    AZURE_GPT4_TURBO = "gt-dse-gpt-4-turbo"
    AZURE_GPT4_32k = "gt-dse-gpt-4-32k"

    # AZURE_OPENAI_API_KEY_US_WEST=os.environ["AZURE_OPENAI_API_KEY_US_WEST"]
    # AZURE_OPENAI_ENDPOINT_US_WEST=os.environ["AZURE_OPENAI_ENDPOINT_US_WEST"]
    # AZURE_GPT4o_US_WEST=os.environ["AZURE_GPT4o_US_WEST"]
    # AZURE_GPT4o_US_WEST_API_VERSION=os.environ["AZURE_GPT4o_US_WEST_API_VERSION"]

    BING_SUBSCRIPTION_KEY = os.environ["BING_SUBSCRIPTION_KEY"]
    BING_SEARCH_URL = os.environ["BING_SEARCH_URL"]

    DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost:5432/chat" #TODO: update to the connection string that Gideon will provide

    # db_url description "postgresql+asyncpg://[user_name]:[password]@[server_address]/[database_name]"

    SMTP_SERVER = os.environ["SMTP_SERVER"]
    SMTP_PORT = os.environ["SMTP_PORT"]
    EMAIL_SENDER = os.environ["EMAIL_SENDER"]
