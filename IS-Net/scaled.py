import cv2

# Load the image
image = cv2.imread('/content/IS-Net/demo_datasets/annotated_image/annotated_image 1.png')

# Scale the image
scale_percent = 70  # percentage of original size
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)

# Resize the image
resized_image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

# Save or display the image
cv2.imwrite('/content/IS-Net/scaled_image/1_m70.jpg', resized_image)
