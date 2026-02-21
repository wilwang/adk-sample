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

## How to Deploy on Vertex Agent Engine

You can use `adk` command line tool to deploy to the managed Agent Engine service. Run the `adk deploy` command in the adk_sample directory and specify the agent.
```
export PROJECT_ID=my-project-id
export LOCATION_ID=my-location

adk deploy agent_engine \
    --project=$PROJECT_ID \
    --region=$LOCATION_ID \
    --display_name="Claims Processor Agent" \
    claims_processor_agent
```

Once you have deployed, the message should include the resource path for the agent similar to this:
```
projects/<PROJECT_ID>/locations/<LOCATION_ID>/reasoningEngines/<RESOURCE_ID>
```

### Test Agent Engine Deployment

Set your env variables
```
export PROJECT_ID=my-project-id
export LOCATION_ID=your-location
export RESOURCE_ID=your-resource-id # if you deployed to Vertex Agent Engine
```

List your agents
```
curl -X GET \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    https://${LOCATION_ID}-aiplatform.googleapis.com/v1/projects/${PROJECT_ID}/locations/${LOCATION_ID}/reasoningEngines
```

Create a session
```
curl \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    https://${LOCATION_ID}-aiplatform.googleapis.com/v1/projects/${PROJECT_ID}/locations/${LOCATION_ID}/reasoningEngines/${RESOURCE_ID}:query \
    -d '{"class_method": "async_create_session", "input": {"user_id": "u_123"},}'
```

Send a message to the agent using session id created in previous step
```
curl -i -X POST https://${LOCATION_ID}-aiplatform.googleapis.com/v1/projects/${PROJECT_ID}/locations/${LOCATION_ID}/reasoningEngines/${RESOURCE_ID}:streamQuery \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    -d '{
    "class_method": "async_stream_query",
    "input": { 
        "user_id":"u_123", 
        "session_id":"4167409790965776384",
        "message":"Can you help me analyze this claim? legit_claim.pdf" 
        },
    }'
```

## How to Containerize and Run on Different Platforms

ADK is platform agnostic so you can containerize and run agents anywhere. You just need to containerize it and serve it through web app framework like Flask. To test, run:

```
> python main.py
```

### Build the container and push to Artifact Registry

```
# Set env variables
export PROJECT_ID="your-project-id"
export REGION="your-location"
export REPO_NAME="adk-sample"
export IMAGE_NAME="adk-sample"

# Create repository on Artifact Registry
gcloud artifacts repositories create $REPO_NAME \
    --project=$PROJECT_ID \
    --repository-format=docker \
    --location=$REGION \
    --description="Docker repository for FastAPI agents"

# Authenticate Docker to Google Cloud
gcloud auth configure-docker $REGION-docker.pkg.dev

# Build the image locally
docker build -t $IMAGE_NAME .

# Tag it for Artifact Registry
docker tag $IMAGE_NAME $REGION-docker.pkg.dev/$PROJECT_ID/$REPO_NAME/$IMAGE_NAME:latest

# Push it to the repo on Artifact Registry
docker push $REGION-docker.pkg.dev/$PROJECT_ID/$REPO_NAME/$IMAGE_NAME:latest

# Deploy image to Cloud Run
gcloud run deploy $IMAGE_NAME \
    --project $PROJECT_ID \
    --image $REGION-docker.pkg.dev/$PROJECT_ID/$REPO_NAME/$IMAGE_NAME:latest \
    --platform managed \
    --region $REGION \
    --allow-unauthenticated
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