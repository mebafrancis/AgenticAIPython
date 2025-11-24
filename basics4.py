import asyncio
import os
from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_agentchat.conditions import MaxMessageTermination, TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient

os.environ["OPENAI_API_KEY"] = "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"

async def main():
    openai_model_client = OpenAIChatCompletionClient(model="gpt-4o")
    assistant = AssistantAgent(
        name="MathTeacher",
        model_client=openai_model_client,
        system_message=(
            "You are a math teacher that helps students with their math problems. "
            "When the user says 'Thanks' or similar words, you should end the conversation politely."
        )
    )
    user_proxy = UserProxyAgent(name="Student")
    team = RoundRobinGroupChat(
        participants=[user_proxy,assistant],
        termination_condition=TextMentionTermination(terms=["LESSON COMPLETED","Thanks","thank you"])
    )
    await Console(team.run_stream(task="Let's discuss the Pythagorean theorem."))

asyncio.run(main())