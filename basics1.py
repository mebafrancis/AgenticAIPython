import asyncio
import os

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient

#os.environ["OPENAI_API_KEY"] = "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"
async def main1():
    print("Hello, World!")
    openai_model_client = OpenAIChatCompletionClient(
        model="gpt-4o",api_key="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")
    assistant= AssistantAgent(name="assistant",model_client=openai_model_client)
    await Console(assistant.run_stream(task = "What is 25*25"))
    await openai_model_client.close()

asyncio.run(main1())
