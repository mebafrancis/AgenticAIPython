import asyncio
import json
import os
from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_agentchat.conditions import MaxMessageTermination, TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat, SelectorGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient

async def main():
    openai_model_client = OpenAIChatCompletionClient(model="gpt-4o")
    researcher = AssistantAgent(
        name="ResearcherAgent",
        model_client=openai_model_client,
        system_message=(
            "You are a researcher . Your role is to gather information and provide research insights. "
        )
    )
    writer = AssistantAgent(
        name="WriterAgent",
        model_client=openai_model_client,
        system_message=(
            "You are a writer. Your role is to create well-structured and engaging content based on the research provided. "
        )
    )

    critic = AssistantAgent(
        name="CriticAgent",
        model_client=openai_model_client,
        system_message=(
            "You are a critic. Your role is to review the content created by the writer and provide constructive feedback. "
            "Say 'TERMINATE' when you think the content is satisfactory."
        )
    )

    team =SelectorGroupChat(participants =[critic, writer, researcher],
                      model_client=openai_model_client,
                      termination_condition= MaxMessageTermination(max_messages=10),
                      allow_repeated_speaker=True)

    await Console(team.run_stream(task="Create a comprehensive article on the impact of climate change on global agriculture."))

asyncio.run(main())