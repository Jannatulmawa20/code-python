import cv2
import matplotlib.pyplot as plt

# Define the list of image file paths
image_files = [
    "C:/Users/HP/PycharmProjects/myfirstproject/openCVPycharm/a-Original-MRI-brain-tumor-image-b-Colored-MRI-image.png",
    "C:/Users/HP/PycharmProjects/myfirstproject/openCVPycharm/img.png",
    "C:/Users/HP/PycharmProjects/myfirstproject/openCVPycharm/gratisography-cool-cat-800x525.jpg",
    "C:/Users/HP/PycharmProjects/myfirstproject/openCVPycharm/img_1.png",
    "C:/Users/HP/PycharmProjects/myfirstproject/openCVPycharm/41598_2023_41576_Fig1_HTML.png",
    "C:/Users/HP/PycharmProjects/myfirstproject/openCVPycharm/a-Original-MRI-brain-tumor-image-b-Colored-MRI-image.png",
]

# Define the number of images to display
img_count = 6
image_files = image_files[:img_count]

# Create a 2x3 subplot
fig, axes = plt.subplots(2, 3, figsize=(10, 7))
axes = axes.ravel()  # Flatten the 2D matrix into 1D for easier iteration

# Loop through images and plot
for i, img_file in enumerate(image_files):
    img = cv2.imread(img_file)  # Read the image
    if img is None:
        print(f"Failed to load image: {img_file}")
        continue
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
    axes[i].imshow(img_rgb)  # Display the image
    axes[i].axis('off')  # Turn off axis

# Adjust layout and show the plot
plt.tight_layout()
plt.show()
