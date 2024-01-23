
import io
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials

subscription_key = "your_vision_subsription_key"    #Replace with your subscription key
endpoint = "https://ocr-python-code.cognitiveservices.azure.com/"

client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

image_path = "path_to_your_image"  # Replace with your image path

with open(image_path, "rb") as image_file:
    image_data = image_file.read()

image_stream = io.BytesIO(image_data)

read_results = client.recognize_printed_text_in_stream(image_stream)

for region in read_results.regions:
    sentence = ""
    for line in region.lines:
        line_text = " ".join([word.text for word in line.words])
        sentence += line_text + " "
    print(sentence.strip())