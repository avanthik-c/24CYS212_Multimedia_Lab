from PIL import Image

def grayscale_conv(img):
    """
    Convert an image to grayscale using the (min + max) / 2 method.
    This method averages the darkest and brightest channel for each pixel.
    
    """
    img=img.convert("RGB")   # Ensure the image is in RGB mode
    pixels=img.load()        # Load pixel map for direct access
    
    #Iterate through every pixel in the image
    for x in range(img.width):
        for y in range(img.height):
            # Extract RGB values of current pixel
            r,g,b=pixels[x,y]      
            # Grayscale formula: midpoint of min and max RGB values
            gray=(min(r,g,b)+max(r,g,b))//2
            # Assign grayscale value to the pixel
            pixels[x,y]=(gray,gray,gray)
    return img

# Load the input image
img=Image.open("desaturation_input.jpg")
# Apply grayscale conversion
result=grayscale_conv(img)
# Save the output image
result.save("desaturation_output.png")