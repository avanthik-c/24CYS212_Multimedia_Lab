from PIL import Image
def octree_quantize_image(img, output, max_colors):
    """
    Perform color quantization using the FASTOCTREE method.
    Reduces the number of colors in the image to the specified limit.
    
    Parameters:
        img (str): Path to the input image.
        output(str): Where the quantized image will be saved.
        max_colors (int): Maximum number of colors allowed in the output image.

    """
    #Open image and ensure it's in RGB format
    img = Image.open(img).convert('RGB')

    print(f"Quantizing image to max {max_colors} colors using FASTOCTREE method")
    #Apply Octree-based color quantization
    quantized_img = img.quantize(colors=max_colors, method=Image.Quantize.FASTOCTREE)
    
    # Save the quantized output image
    quantized_img.save(output)
    print(f"Quantized image saved to: {output}")


#Ask user how many colors they want to preserve
max_colors = int(input("Enter maximum number of colors you want : "))
#Call the quantization function
octree_quantize_image("octree_input.jpg","octree_output.png", max_colors)