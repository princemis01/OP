import colorsys
from PIL import Image, ImageDraw, ImageFont

# Prompt the user for a background color
color_input = input('Enter a background color as a hexadecimal RGB value (e.g. #ff0000): ')

# Convert the hexadecimal RGB value to an RGB color
rgb_color = tuple(int(color[2:], 16) for color in color_input[1:].split('/'))

# Define the size of the image
image_size = (500, 200)

# Create a new image with the specified size and background color
image = Image.new('RGB', image_size, color=rgb_color)

# Define the text to be added to the image
text = 'BUS PASS CCTT BUS PASS'

# Load a font to use for the text
font = ImageFont.truetype('arial.ttf', size=40)

# Create a drawing context for the image
draw = ImageDraw.Draw(image)

# Calculate the position of the text in the image
text_width, text_height = draw.textsize(text, font=font)
text_x = (image_size[0] - text_width) // 2
text_y = (image_size[1] + text_height) // 2

# Draw the text on the image
draw.text((text_x, text_y), text, font=font, fill=(0, 0, 0))

# Save the image to a file
image.save('image_with_bg_color.png')

# Display the image
image.show()