from vertexai.preview.vision_models import ImageGenerationModel
import os
# Path to your service account key file
key_path = r"stoked-forest-447811-u4-ecf33505a9e7.json"

# Set the environment variable
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_path
imagen_model = ImageGenerationModel.from_pretrained("imagen-3.0-generate-001")
image_prompt = "A delicious pizza"

response = imagen_model.generate_images(
    prompt=image_prompt,
)

response.images[0].show()