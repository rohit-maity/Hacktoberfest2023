from PIL import Image, ImageDraw, ImageFont
from faker import Faker
import random

# Create a Faker instance to generate fake names
fake = Faker()

# Define the size of the image
width, height = 300, 400

# Create a blank image
image = Image.new('RGB', (width, height), (255, 255, 255))
draw = ImageDraw.Draw(image)

# Load a random font (you can provide the path to a font file)
font = ImageFont.load_default()

# Generate a random name and display it on the image
name = fake.name()
text_width, text_height = draw.textsize(name, font)
text_x = (width - text_width) / 2
text_y = (height - text_height) / 2
draw.text((text_x, text_y), name, fill=(0, 0, 0), font=font)

# Save the image
image.save("random_person_photo.png")

# Display the image (optional)
image.show()
