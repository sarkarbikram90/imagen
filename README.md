# imagen
Simplified Text-to-Image Generator
A beginner-friendly Python project that generates simple images based on text prompts, showcasing the basic principles of text-to-image systems.
# Overview
This project demonstrates how to convert a text input into an image by:

Mapping Text to Numerical Embeddings: Converting the input text into a numerical representation.
Mapping Embeddings to Visual Parameters: Using the embedding to define attributes like shape, color, and size.
Generating Images: Drawing simple shapes (circles or squares) based on the extracted parameters.

The goal is to provide an educational starting point for understanding text-to-image generation.
# Features
Generates images with one shape: circle or square.
The shape's color and size are dynamically derived from the input text.
Supports customizable canvas size.
# Usage
Clone the repository:
```bash
git clone https://github.com/sarkarbikram90/imagen.git
```
Navigate to the project directory:
```bash
cd imagen
```
Run the script:
```bash
python imagen.py
```
Enter a text prompt when prompted. The generated image will be displayed in a new window.
# Limitations
The image generation is based on simple heuristics, not advanced machine learning.
Only basic shapes (circle or square) are supported.