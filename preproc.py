from PIL import Image
import os

# Set the input and output directories
input_dir = 'detection/celebA/img_align_celeba/'
output_dir = 'detection/images_with_eyeglasses_resized/'

# Set the desired image size
image_size = (128, 128)

# Loop over all images in the input directory
for filename in os.listdir(input_dir):
    # Check if the image has eyeglasses attribute
    if df.loc[filename]['Eyeglasses'] == 1:
        # Load the image using PIL
        image = Image.open(os.path.join(input_dir, filename))
        # Resize the image to the desired size
        image = image.resize(image_size)
        # Save the resized image to the output directory
        image.save(os.path.join(output_dir, filename))
