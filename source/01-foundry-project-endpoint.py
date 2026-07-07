import os

from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from dotenv import load_dotenv

load_dotenv()

project_endpoint = os.getenv("FOUNDRY_PROJECT_ENDPOINT")
if not project_endpoint:
    raise ValueError("FOUNDRY_PROJECT_ENDPOINT is not set in .env")

project_client = AIProjectClient(
    credential=DefaultAzureCredential(),
    endpoint=project_endpoint
)

openai_client = project_client.get_openai_client()

# Generate a response using the OpenAI-compatible client
response = openai_client.responses.create(
    model="gpt-5.4",
    input="What is Microsoft Foundry?"
)

print(response.output_text)