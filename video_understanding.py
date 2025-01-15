import vertexai

from vertexai.generative_models import GenerativeModel, Part
import os
# TODO(developer): Update and un-comment below line
# PROJECT_ID = "your-project-id"
key_path = r"stoked-forest-447811-u4-ecf33505a9e7.json"

# Set the environment variable
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_path
vertexai.init( location="us-central1")

vision_model = GenerativeModel("gemini-1.5-flash-002")

# Generate text
response = vision_model.generate_content(
    [
        Part.from_uri(
            "gs://cloud-samples-data/video/animals.mp4", mime_type="video/mp4"
        ),
        "What is in the video?",
    ]
)
print(response.text)
# Example response:
# Here's a summary of the video's content.
# The video shows a series of animals at the Los Angeles Zoo interacting
# with waterproof cameras attached to various devices.
# ...