import asyncio
import os
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.conditions import MaxMessageTermination
from autogen_agentchat.messages import MultiModalMessage
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_core import Image
from autogen_ext.models.openai import OpenAIChatCompletionClient


os.environ["OPENAI_API_KEY"] = "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"

async def main():
    openai_model_client = OpenAIChatCompletionClient(model="gpt-4o")
    assistant1 = AssistantAgent(name="MathTeacher", model_client=openai_model_client,
                               system_message="You are a math teacher that helps students with their math problems.")

    student1 = AssistantAgent(name="Student", model_client=openai_model_client,
                                system_message="You are a curious student with math problems.")

    team = RoundRobinGroupChat(participants=[assistant1, student1] ,termination_condition= MaxMessageTermination(max_messages=6) )
    await Console(team.run_stream(task = "Lets discuss about Pythagorean theorem."))
    await openai_model_client.close()
asyncio.run(main())



