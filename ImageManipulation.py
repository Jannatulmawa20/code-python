import cv2
import matplotlib.pyplot as plt

# Load the image
img_file = "C:/Users/HP/PycharmProjects/myfirstproject/openCVPycharm/img1.jpg"  # Replace with the path to your image
img = cv2.imread(img_file)

# Check if the image is loaded
if img is None:
    raise FileNotFoundError(f"Image not found: {img_file}")

# Convert the image to RGB for displaying with matplotlib
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Perform transformations
# 1. Resizing
img_resized_half = cv2.resize(img_rgb, None, fx=0.5, fy=0.5)
img_resized_double = cv2.resize(img_rgb, None, fx=2.0, fy=2.0)

# 2. Rotations
height, width = img_rgb.shape[:2]
center = (width // 2, height // 2)
rotation_matrix_90 = cv2.getRotationMatrix2D(center, 90, 1)
img_rotated_90 = cv2.warpAffine(img_rgb, rotation_matrix_90, (width, height))

rotation_matrix_180 = cv2.getRotationMatrix2D(center, 180, 1)
img_rotated_180 = cv2.warpAffine(img_rgb, rotation_matrix_180, (width, height))

rotation_matrix_270 = cv2.getRotationMatrix2D(center, 270, 1)
img_rotated_270 = cv2.warpAffine(img_rgb, rotation_matrix_270, (width, height))

# 3. Flipping
img_hflip = cv2.flip(img_rgb, 1)  # Horizontal flip
img_vflip = cv2.flip(img_rgb, 0)  # Vertical flip

# 4. Cropping
x, y, w, h = 50, 50, width - 100, height - 100  # Define the crop region
img_crop = img_rgb[y:y + h, x:x + w]

# Display the images
fig, axes = plt.subplots(3, 3, figsize=(10, 7))
axes = axes.ravel()

axes[0].imshow(img_rgb)
axes[0].set_title('Original Image')
axes[0].axis('off')

axes[1].imshow(img_resized_half)
axes[1].set_title('Resized Image: Half')
axes[1].axis('off')

axes[2].imshow(img_resized_double)
axes[2].set_title('Resized Image: Double')
axes[2].axis('off')

axes[3].imshow(img_rotated_90)
axes[3].set_title('Rotated Image 90°')
axes[3].axis('off')

axes[4].imshow(img_rotated_180)
axes[4].set_title('Rotated Image 180°')
axes[4].axis('off')

axes[5].imshow(img_rotated_270)
axes[5].set_title('Rotated Image 270°')
axes[5].axis('off')

axes[6].imshow(img_hflip)
axes[6].set_title('Horizontal Flip')
axes[6].axis('off')

axes[7].imshow(img_vflip)
axes[7].set_title('Vertical Flip')
axes[7].axis('off')

axes[8].imshow(img_crop)
axes[8].set_title('Cropped Image')
axes[8].axis('off')

plt.tight_layout()
plt.show()
