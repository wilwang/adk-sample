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

### Build the container and push to Artifact Registry

```
# Set env variables
export PROJECT_ID="your-project-id"
export REGION="us-central1"
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