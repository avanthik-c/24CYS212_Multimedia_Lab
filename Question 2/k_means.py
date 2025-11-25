import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def kmeans_quantization(img, k):
    # Load the image
    image = Image.open(img)
    image = image.convert("RGB")  # Convert to RGB

    # Convert to numpy array and reshape to (num_pixels, 3)
    image = np.array(image)
    pixels = image.reshape(-1, 3)

    # Apply K-Means clustering (fixed n_init warning)
    kmeans = KMeans(n_clusters=k, random_state=7, n_init='auto')
    kmeans.fit(pixels)

    # Cluster centers (quantized colors) and labels
    centers = kmeans.cluster_centers_.astype(np.uint8)
    labels = kmeans.labels_

    # Reconstruct quantized image
    quantized_image = centers[labels].reshape(image.shape)

    # Compute Mean Squared Error (distortion)
    mse = np.mean((image - quantized_image) ** 2)

    # Display original and quantized images
    plt.figure(figsize=(12,6))

    plt.subplot(1,2,1)
    plt.title("Original Image")
    plt.imshow(image)
    plt.axis('off')

    plt.subplot(1,2,2)
    plt.title(f"Quantized Image (k={k})\nMSE={mse:.2f}")
    plt.imshow(quantized_image)
    plt.axis('off')

    plt.show()

    # Save quantized image
    output_path = f"quantized_k{k}.png"
    Image.fromarray(quantized_image).save(output_path)
    print("Saved as:", output_path)

    return quantized_image, mse


# Example usage
quantized_img, mse = kmeans_quantization("octree_input.jpg", k=256)