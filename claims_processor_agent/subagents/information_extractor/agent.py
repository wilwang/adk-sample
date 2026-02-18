from google.adk.agents.llm_agent import Agent

from .tools.tools import file_content_extractor

information_extractor = Agent(
    model='gemini-2.5-flash',
    name='information_extractor',
    description='An agent that extracts details of a claimant and a claim from documents provided by the user',
    instruction='Answer user questions to the best of your knowledge',
    tools=[
        file_content_extractor,
    ],
)
