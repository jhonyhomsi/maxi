from PIL import Image

# Open the JPEG image
with Image.open('logo.jpg') as im:

    # Convert the image to PNG
    im.save('image.png', 'PNG')
