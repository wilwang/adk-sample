from google.adk.agents.llm_agent import Agent

data_analyst = Agent(
    model='gemini-2.5-flash',
    name='data_analyst',
    description='An agent that analyzes details from a claim and evaluates whether the claim seems fraudulent, legitmate, or requires more information.',
    instruction="""
        Based on the data you receive, determine whether a claim seems fraudulent, legitmate, or requires more information. 
        Take into account factors such as whether the injury seems plausible given the context of the data. For example, an 
        office worker is unlikely to incur an injury typically seen in more active activities.
    """,
)
