# claims_processor_agent

Sample of a agentic assistant to aid human claims processors on evaluating claims and determining whether the claim seems fraudulent or legitmate

## How to Run in ADK Web for development

ADK web should be run in the parent folder `adk-sample`

```
> python -m venv .venv
> source .venv/bin/activate
> pip install -r requirements.txt
> adk web
```

## Containerize and run on different platforms

ADK is platform agnostic so you can containerize and run agents anywhere. You just need to containerize it and serve it through web app framework like Flask.

```
> python main.py
```


### Test the API

Create a session
```
curl -X POST http://0.0.0.0:8080/apps/claims_processor_agent/users/user_123/sessions/session_abc \
    -H "Content-Type: application/json" \
    -d '{"preferred_language": "English", "visit_count": 1}'
```

Send requests to the agent
```
curl -X POST http://0.0.0.0:8080/run_sse \
    -H "Content-Type: application/json" \
    -d '{
    "app_name": "claims_processor_agent",
    "user_id": "user_123",
    "session_id": "session_abc",
    "new_message": {
        "role": "user",
        "parts": [{
        "text": "can you evaluate this claim document? fake.pdf"
        }]
    },
    "streaming": false
    }'
```