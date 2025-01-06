import numpy as np
from PIL import Image, ImageDraw
import random

# Step 1: Simple Text-to-Embedding
def text_to_embedding(text):
    # Assign a numerical vector to each word (toy example)
    embedding = np.sum([ord(char) for char in text]) % 256
    return embedding

# Step 2: Map Embedding to Visual Parameters
def embedding_to_visual_params(embedding):
    # Map the embedding to colors and shapes
    color = (embedding % 256, (embedding * 2) % 256, (embedding * 3) % 256)  # RGB color
    shape_type = "circle" if embedding % 2 == 0 else "square"  # Shape type
    size = 50 + (embedding % 100)  # Size of the shape
    return color, shape_type, size

# Step 3: Generate an Image
def generate_image_from_text(text, image_size=(256, 256)):
    embedding = text_to_embedding(text)
    color, shape_type, size = embedding_to_visual_params(embedding)
    
    # Create a blank image
    image = Image.new("RGB", image_size, (255, 255, 255))
    draw = ImageDraw.Draw(image)
    
    # Draw a shape based on the parameters
    center_x, center_y = image_size[0] // 2, image_size[1] // 2
    if shape_type == "circle":
        draw.ellipse(
            [center_x - size, center_y - size, center_x + size, center_y + size],
            fill=color
        )
    else:
        draw.rectangle(
            [center_x - size, center_y - size, center_x + size, center_y + size],
            fill=color
        )
    
    return image

# Step 4: Test the Generator
if __name__ == "__main__":
    text_prompt = input("Enter a prompt: ")
    generated_image = generate_image_from_text(text_prompt)
    generated_image.show()
