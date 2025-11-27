import asyncio
import json
import os
from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_agentchat.conditions import MaxMessageTermination, TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.agents.web_surfer import MultimodalWebSurfer
from autogen_ext.models.openai import OpenAIChatCompletionClient

os.environ["OPENAI_API_KEY"] = "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"

async def main():
    openai_model_client = OpenAIChatCompletionClient(model="gpt-4o")
    websurfer_agent = MultimodalWebSurfer(
        name="WebSurfer",
        model_client=openai_model_client,
        headless = False,
        animate_actions = True
    )
    agent_team=RoundRobinGroupChat(participants=[websurfer_agent],max_turns=3)
    await Console(agent_team.run_stream(task ="Navigate to google.com search for 'latest advancements in renewable energy', click on the first link, and summarize the key points from the article."))

asyncio.run(main())