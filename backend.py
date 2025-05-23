import os
import base64
from mistralai import Mistral

from dotenv import load_dotenv 
load_dotenv()

def encode_image(image_path):
    """Encode the image to base64."""
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    except FileNotFoundError:
        print(f"Error: The file {image_path} was not found.")
        return None
    except Exception as e:  # Added general exception handling
        print(f"Error: {e}")
        return None
    

def describe_image(image_path):
    

    # Getting the base64 string
    base64_image = encode_image(image_path)


    api_key = os.environ["MISTRAL_KEY"]
    model = "pixtral-12b-2409"

    client = Mistral(api_key=api_key)

    chat_response = client.chat.complete(
        model = model,
        messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "décris l'image"
                },
                {
                    "type": "image_url",
                    "image_url": f"data:image/jpeg;base64,{base64_image}" 
                }
            ]
        },
        ]
    )

    return(chat_response.choices[0].message.content)

image_path = r"C:\Users\roron\Pictures\rap festif.png"   
print(describe_image(image_path))
