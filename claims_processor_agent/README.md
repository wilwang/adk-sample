# claims_processor_agent

Sample of a agentic assistant to aid human claims processors on evaluating claims and determining whether the claim seems fraudulent or legitmate


## How to Run in ADK Web for development

Run at the agent folder level (i.e., `claims_processor_agent`)

```
> python3 -m venv .venv
> source .venv/bin/activate
> pip install -r requirements.txt
```

ADK web should be run in the parent folder `adk-sample`
```
> cd ..
> pip install google-adk
> adk web
```