import os
import matplotlib.pyplot as plt
import math

# Get folder path from user input
folder_path = input("Enter the folder path containing images: ")

# Check if the folder path is valid
if not os.path.isdir(folder_path):
    print("Invalid folder path. Exiting...")
    exit()

# Get image file paths from the folder
image_paths = [os.path.join(folder_path, filename) for filename in os.listdir(folder_path) if filename.endswith('.jpg')]

# Load images
images = []
for path in image_paths:
    image = plt.imread(path)
    images.append(image)

# Calculate the number of rows and columns based on the number of images
num_images = len(images)
num_rows = int(math.ceil(num_images / 3))
num_cols = min(num_images, 3)

# Create the grid of subplots
fig, axes = plt.subplots(num_rows, num_cols, figsize=(12, 9))

# Adjust the size of each subplot and remove axis ticks
for i, ax in enumerate(axes.flat):
    if i < num_images:
        # Plot the image
        ax.imshow(images[i])
        ax.axis('off')
        ax.set_aspect('equal')
    else:
        fig.delaxes(ax)  # Remove unused subplots

plt.tight_layout()

# Save the grid image in the same folder with JPEG format
output_path = os.path.join(folder_path, 'image_grid.jpg')
fig.savefig(output_path, format='jpeg', bbox_inches='tight', pad_inches=0)

plt.close(fig)  # Close the figure to release resources

print(f"Grid image saved at {output_path}")