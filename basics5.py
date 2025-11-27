import asyncio
import json
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
        model_client=openai_model_client
    )
    assistant1 = AssistantAgent(
        name="MathTeacher",
        model_client=openai_model_client
    )
    await Console(assistant.run_stream(task="Let's discuss the Pythagorean theorem."))
    state = await assistant.save_state()
    with open("memory.json", "w") as f:
        json.dump(state, f, default = str)

    with open("memory.json", "r") as f:
        state = json.load(f)
    await assistant1.load_state(state)

    await Console(assistant1.run_stream(task="Can you remind me what we discussed about the Pythagorean theorem?"))

    await openai_model_client.close()

asyncio.run(main())