from PIL import Image
import os

def create_image_grid_fit(folder_path, output_path, grid_size=(17, 12), cell_size=(40 * 20, 40 * 20), gap=8 * 20, background_color="#1F1F1F"):
    """
    Create a grid of images from the specified folder. Images are fitted into cells without distortion.
    :param folder_path: Path to the folder containing images.
    :param output_path: Path to save the output image.
    :param grid_size: Tuple of (columns, rows) for the grid.
    :param cell_size: Size of each cell in the grid (width, height).
    :param gap: Gap between cells in pixels.
    :param background_color: Background color of the grid.
    """
    # Calculate the total size of the grid
    total_width = (cell_size[0] + gap) * grid_size[0] - gap
    total_height = (cell_size[1] + gap) * grid_size[1] - gap

    # Create a new blank image for the grid with the specified background color
    grid_image = Image.new('RGB', (total_width, total_height), background_color)

    # Load all images from the folder
    images = [Image.open(os.path.join(folder_path, file)) for file in os.listdir(folder_path)
              if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]

    # Fit images into cells and place them in the grid
    for row in range(grid_size[1]):
        for col in range(grid_size[0]):
            index = row * grid_size[0] + col
            if index < len(images):
                img = images[index]

                # Calculate the scaling factor to fit the image in the cell without distortion
                scale = min(cell_size[0] / img.width, cell_size[1] / img.height)
                new_size = (int(img.width * scale), int(img.height * scale))

                # Resize and center the image in the cell
                img = img.resize(new_size)
                offset = ((cell_size[0] - new_size[0]) // 2, (cell_size[1] - new_size[1]) // 2)
                position = (col * (cell_size[0] + gap) + offset[0], row * (cell_size[1] + gap) + offset[1])
                grid_image.paste(img, position)

    # Save the grid image
    grid_image.save(output_path)

# Replace these paths with your actual file paths
# folder_path = 'C:/Users/Juliu/GitHub/365/204-ende'  # Replace with the path to your images
folder_path = 'C:/Users/Juliu/GitHub/365/target-2'  # Replace with the path to your images
output_path = './1.jpg'  # Replace with the path to save the grid image
create_image_grid_fit(folder_path, output_path)