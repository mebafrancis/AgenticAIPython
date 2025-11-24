import asyncio
import os

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import MultiModalMessage
from autogen_agentchat.ui import Console
from autogen_core import Image
from autogen_ext.models.openai import OpenAIChatCompletionClient

#os.environ["OPENAI_API_KEY"] = "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"
async def main1():
    print("Hello, World!")
    openai_model_client = OpenAIChatCompletionClient(model="gpt-4o")
    assistant= AssistantAgent(name="Multimodel",model_client=openai_model_client)
    image =Image.from_file("/Galaxy.jpg")
    multimodal_message = MultiModalMessage(content=["What do you see in the image?", image])
    await Console(assistant.run_stream(task = multimodal_message))
    await openai_model_client.close()

asyncio.run(main1())
