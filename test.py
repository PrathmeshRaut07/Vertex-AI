from google.cloud import aiplatform
import os
def list_models( location):
    # Initialize the Vertex AI client
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"stoked-forest-447811-u4-ecf33505a9e7.json"
    aiplatform.init( location=location)

    # List all models in the specified project and location
    models = aiplatform.Model.list()
    print(models)

    # Print details of each model
    for model in models:
        print(f"Model Display Name: {model.display_name}")
        print(f"Model Name: {model.name}")
        print(f"Model Version: {model.version_id}")
        print(f"Model URI: {model.artifact_uri}")
        print(f"Model Creation Time: {model.create_time}")
        print(f"Model Update Time: {model.update_time}")
        print("-" * 40)


    
location = "us-central1"  # e.g., "us-central1", "europe-west4", etc.

list_models(location)