from PIL import Image
import numpy as np

# open the image file
image = Image.open('jigsaw.jpg')

# convert the image to a numpy array
image_array = np.array(image)

# transpose the image array
transposed_array = np.transpose(image_array, (1, 0, 2))

# reshape the transposed array to a 2D array
reshaped_array = transposed_array.reshape(image_array.shape[1], -1)

# print the shape of the reshaped array
print(reshaped_array.shape)

image = Image.fromarray(np.uint8(reshaped_array))

# Save the image as a JPEG file
image.save("new_jigsaw.jpg")