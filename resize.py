import os
from PIL import Image

path = './assets/'
image_extensions = ['.jpg', '.jpeg', '.png', '.tiff']


def print_directory_tree(folder_path):
    """
    Print the names of all directories and subdirectories in a folder.

    Args:
        folder_path (str): The path of the folder to traverse.
    """
    # print(folder_path)
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path):
            print_directory_tree(item_path)
        else:
            if not item_path.endswith('.DS_Store'):
                # Split the path into directory path and file name
                end_path, file_name = os.path.split(item_path)
                # Resize the image
                resize_image(end_path, file_name, item_path)


def create_folder(subfolder_path):
    try:
        # Create the directory (and any missing parent directories)
        os.makedirs(subfolder_path)
    except OSError:
        print(f"Failed to create the directory at {subfolder_path}.")

    return subfolder_path


def save_new_image(image, new_image_width, new_image_height, end_path, file_name):
    resized_image = image.resize((new_image_width, new_image_height), resample=Image.BICUBIC)
    resized_image.save(end_path + '/' + file_name, 'JPEG', quality=100)


def square_and_vertical_image_dimensions(image_width, image_height, new_image_size):

    if image_width > image_height:
        width_resize_ratio = round(image_height/new_image_size, 2)
        new_image_width = int(image_width/width_resize_ratio)
        new_image_height = new_image_size
    else:
        height_resize_ratio = round(image_width/new_image_size, 2)
        new_image_height = int(image_height/height_resize_ratio)
        new_image_width = new_image_size

    return new_image_width, new_image_height


def horizontal_image_resize(end_path, file_name, full_image_path):

    image = Image.open(full_image_path)
    image_width, image_height = image.size

    new_image_width = 0
    new_image_height = 0
    tmp_end_path = end_path

    subfolder_names = ('Twitter_1600x900', 'Facebook_1200x630')
    for subfolder_name in subfolder_names:

        if subfolder_name == 'Twitter_1600x900':

            subfolder_path = os.path.join(tmp_end_path, subfolder_name)
            if os.path.exists(subfolder_path) and os.path.isdir(subfolder_path):
                tmp_end_path = subfolder_path
            else:
                tmp_end_path = create_folder(subfolder_path)

            new_image_width = 1600
            height_resize_ratio = round(image_width/new_image_width, 2)
            new_image_height = int(image_height/height_resize_ratio)
        elif subfolder_name == 'Facebook_1200x630':

            subfolder_path = os.path.join(tmp_end_path, subfolder_name)
            if os.path.exists(subfolder_path) and os.path.isdir(subfolder_path):
                tmp_end_path = subfolder_path
            else:
                tmp_end_path = create_folder(subfolder_path)

            new_image_width = 1200
            height_resize_ratio = round(image_width/new_image_width, 2)
            new_image_height = int(image_height/height_resize_ratio)

        if new_image_width != 0 and new_image_height != 0:
            save_new_image(image, new_image_width, new_image_height, tmp_end_path, file_name)

        tmp_end_path = end_path

    image.close()


def square_and_vertical_image_resize(end_path, file_name, full_image_path):

    image = Image.open(full_image_path)
    image_width, image_height = image.size
    new_image_width = 0
    new_image_height = 0

    tmp_end_path = end_path

    subfolder_names = ('Instagram_1080x1080', 'Facebook_1200x1200', 'Pinterest_1000x1000', 'Pinterest_1000x1500', 'Twitter_800x800')
    for subfolder_name in subfolder_names:
        subfolder_path = os.path.join(tmp_end_path, subfolder_name)

        if subfolder_name == 'Instagram_1080x1080':

            if os.path.exists(subfolder_path) and os.path.isdir(subfolder_path):
                tmp_end_path = subfolder_path
            else:
                tmp_end_path = create_folder(subfolder_path)

            new_image_size = 1080
            new_image_width, new_image_height = square_and_vertical_image_dimensions(image_width, image_height, new_image_size)

        elif subfolder_name == 'Facebook_1200x1200':

            if os.path.exists(subfolder_path) and os.path.isdir(subfolder_path):
                tmp_end_path = subfolder_path
            else:
                tmp_end_path = create_folder(subfolder_path)

            new_image_size = 1200
            new_image_width, new_image_height = square_and_vertical_image_dimensions(image_width, image_height, new_image_size)

        elif subfolder_name == 'Pinterest_1000x1000':

            if os.path.exists(subfolder_path) and os.path.isdir(subfolder_path):
                tmp_end_path = subfolder_path
            else:
                tmp_end_path = create_folder(subfolder_path)

            new_image_size = 1000
            new_image_width, new_image_height = square_and_vertical_image_dimensions(image_width, image_height, new_image_size)

        elif subfolder_name == 'Pinterest_1000x1500':

            if os.path.exists(subfolder_path) and os.path.isdir(subfolder_path):
                tmp_end_path = subfolder_path
            else:
                tmp_end_path = create_folder(subfolder_path)

            new_image_size = 1500
            new_image_width, new_image_height = square_and_vertical_image_dimensions(image_width, image_height, new_image_size)

        elif subfolder_name == 'Twitter_800x800':

            if os.path.exists(subfolder_path) and os.path.isdir(subfolder_path):
                tmp_end_path = subfolder_path
            else:
                tmp_end_path = create_folder(subfolder_path)

            new_image_size = 800
            new_image_width, new_image_height = square_and_vertical_image_dimensions(image_width, image_height, new_image_size)

        if new_image_width != 0 and new_image_height != 0:
            save_new_image(image, new_image_width, new_image_height, tmp_end_path, file_name)

        tmp_end_path = end_path

    image.close()


def resize_image(end_path, file_name, full_image_path):
    # Get the file extension
    file_extension = os.path.splitext(file_name)[1]

    # Print the directory path, file name, and file extension
    # print("Directory path:", end_path)
    # print("File name:", file_name)
    if file_extension in image_extensions:
        # Open the image
        image = Image.open(full_image_path)
        # Get the image width and height
        image_width, image_height = image.size
        # print(f'original image size: {image_width}x{image_height}')

        current_resolution = image.info['dpi'][0]

        # Print the estimated resolution
        if current_resolution is not None:
            if current_resolution > 72:
                new_resolution = 72
                # Calculate the new size of the image in pixels
                new_width = int(image_width * new_resolution / current_resolution)
                new_height = int(image_height * new_resolution / current_resolution)
                # Resize the image to the new size and resolution
                resized_image = image.resize((new_width, new_height), resample=Image.BICUBIC)
                resized_image.info['dpi'] = (new_resolution, new_resolution)
                image = resized_image

        if file_extension not in ('.jpg', '.jpeg'):
            # Save the image as a JPEG
            image.save(end_path + '/' + file_name, 'JPEG', quality=100)
        else:
            image.save(full_image_path, 'JPEG', quality=100)

        image.close()

        # Resize the image for Facebook
        print('Starts saving horizontal images')
        horizontal_image_resize(end_path, file_name, full_image_path)
        print('End saving horizontal images')

        # Resize the image for Instagram
        print('Starts saving square and vertical images')
        square_and_vertical_image_resize(end_path, file_name, full_image_path)
        print('End saving square and vertical images')


print_directory_tree(path)
