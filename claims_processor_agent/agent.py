from google.adk.agents.llm_agent import Agent
from google.adk.tools.agent_tool import AgentTool
from google.genai import types

from .prompt import AGENT_INSTRUCTION
from .subagents.data_analyst import data_analyst
from .subagents.information_extractor import information_extractor

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful claims assistant to help you analyze a claim.',
    instruction=AGENT_INSTRUCTION,
    generate_content_config=types.GenerateContentConfig(temperature=0.2),
    tools=[
        AgentTool(agent=information_extractor),
        AgentTool(agent=data_analyst),
    ],
)
