from PIL import Image
import os

def create_image_grid(folder_path, output_path, grid_size=(17, 12), image_size=(40, 40), gap=8):
    """
    Create a grid of images from the specified folder.
    :param folder_path: Path to the folder containing images.
    :param output_path: Path to save the output image.
    :param grid_size: Tuple of (columns, rows) for the grid.
    :param image_size: Size of each image in the grid (width, height).
    :param gap: Gap between images in pixels.
    """
    # Calculate the total size of the grid
    total_width = (image_size[0] + gap) * grid_size[0] - gap
    total_height = (image_size[1] + gap) * grid_size[1] - gap

    # Create a new blank image for the grid
    grid_image = Image.new('RGB', (total_width, total_height), "#2E2E2E")

    # Load all images from the folder
    images = [Image.open(os.path.join(folder_path, file)) for file in os.listdir(folder_path)
              if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]

    # Resize images and place them in the grid
    for row in range(grid_size[1]):
        for col in range(grid_size[0]):
            index = row * grid_size[0] + col
            if index < len(images):
                ratio = images[index].width / images[index].height
                target_size
                if ratio > 1:
                    #Landscape
                    height = images[index].width / ratio
                else:
                    #Portrait
                # img = images[index].resize(image_size)
                grid_image.paste(img, (col * (image_size[0] + gap), row * (image_size[1] + gap)))

    # Save the grid image
    grid_image.save(output_path)

# Example usage
folder_path = 'C:/Users/Juliu/GitHub/365/target-2'  # Replace with the path to your images
output_path = './grid_image.jpg'  # Replace with the path to save the grid image
create_image_grid(folder_path, output_path)