from PIL import Image

def split_image(image_path, n, m):
    with Image.open(image_path) as image:
        # Get the size of the image
        width, height = image.size

        # Calculate the size of each sub-image
        sub_width = width // n
        sub_height = height // m

        # Loop through each sub-image
        for i in range(n):
            for j in range(m):
                # Calculate the bounding box for the current sub-image
                left = i * sub_width
                top = j * sub_height
                right = left + sub_width
                bottom = top + sub_height

                # Crop the sub-image from the original image
                sub_image = image.crop((left, top, right, bottom))

                # Save the sub-image with a unique filename
                sub_image.save(f'pieces/sub_image_{i}_{j}.png')



split_image('perspective_jigsaw.jpg', 40, 25) # splits image into a 40x25 matrix of sub-images
