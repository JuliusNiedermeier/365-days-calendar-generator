from PIL import Image, ExifTags
import os

factor = 20

def create_image_grid_fit(folder_path, output_path, grid_size=(14, 12), cell_size=(40 * factor, 40 * factor), gap=8 * factor, background_color="#1F1F1F"):
    # Calculate the total size of the grid with added space for the border
    border_size = gap
    total_width = (cell_size[0] + gap) * grid_size[0] - gap + 2 * border_size
    total_height = (cell_size[1] + gap) * grid_size[1] - gap + 2 * border_size

    # Create a new blank image for the grid with the specified background color
    grid_image = Image.new('RGB', (total_width, total_height), background_color)

    # Load all images from the folder
    images = [Image.open(os.path.join(folder_path, file)) for file in os.listdir(folder_path)
              if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]
    
    # Load all images from the folder
    images = []
    for file in os.listdir(folder_path):
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            img_path = os.path.join(folder_path, file)
            img = Image.open(img_path)

            # Correct the orientation using EXIF data
            if hasattr(img, '_getexif'):  # only present in JPEGs
                for orientation in ExifTags.TAGS.keys():
                    if ExifTags.TAGS[orientation] == 'Orientation':
                        break
                exif = img._getexif()  # returns None if no EXIF data
                if exif is not None:
                    exif = dict(exif.items())
                    orientation = exif.get(orientation, None)

                    if orientation == 3:
                        img = img.rotate(180, expand=True)
                    elif orientation == 6:
                        img = img.rotate(270, expand=True)
                    elif orientation == 8:
                        img = img.rotate(90, expand=True)

            images.append(img)

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
                position = (col * (cell_size[0] + gap) + offset[0] + border_size, 
                            row * (cell_size[1] + gap) + offset[1] + border_size)
                grid_image.paste(img, position)
                print(index)

    # Save the grid image
    grid_image.save(output_path)

# Replace these paths with your actual file paths
folder_path = 'C:/Users/Juliu/GitHub/365/204-ende'  # Replace with the path to your images
# folder_path = 'C:/Users/Juliu/GitHub/365/target-2'  # Replace with the path to your images
output_path = './2.jpg'  # Replace with the path to save the grid image
create_image_grid_fit(folder_path, output_path)
