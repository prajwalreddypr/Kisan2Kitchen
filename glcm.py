import cv2
import numpy as np
import pandas as pd
import sys
import openpyxl
import io
import re

# read the image path from the command line argument
image_path = sys.argv[1]

# read the image and convert to grayscale
img = cv2.imread(image_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# compute the GLCM matrix
glcm = np.zeros((256, 256), dtype=np.float32)
for i in range(gray.shape[0]-1):
    for j in range(gray.shape[1]-1):
        i1 = gray[i, j]
        i2 = gray[i+1, j]
        glcm[i1, i2] += 1
        glcm[i2, i1] += 1
glcm = glcm / np.sum(glcm)

# compute the GLCM features
px, py = np.mgrid[0:256, 0:256]
px = px.reshape((-1, 1))
py = py.reshape((-1, 1))
contrast = 0
for i in range(256):
    for j in range(256):
        contrast += ((i - j) ** 2) * glcm[i, j]
homogeneity = 0
for i in range(256):
    for j in range(256):
        homogeneity += glcm[i, j] / (1 + abs(i - j))
energy = np.sum(glcm ** 2)
entropy = -np.sum(glcm * np.log2(glcm + 1e-6))
variance = 0
for i in range(256):
    for j in range(256):
        variance += ((i - np.mean(px)) ** 2) * glcm[i, j]

features = {
    "Entropy": entropy,
    "Variance": variance,
    "Energy": energy,
    "Contrast": contrast,
    "Homogeneity": homogeneity
}

# read the excel file as binary
with open("glcm_features.xlsx", "rb") as f:
    file_bytes = f.read()

# create a file-like object from the bytes
file = io.BytesIO(file_bytes)

# read the excel file as a DataFrame
df = pd.read_excel(file, engine='openpyxl')

# add a new row with the GLCM features
# extract the image number from the filename
img_num = re.findall(r'\d+', image_path)[-1]
row = [img_num] + [features[k] for k in df.columns[1:]]
df = df.append(pd.Series(row, index=df.columns), ignore_index=True)

# write the updated excel file
df.to_excel('glcm_features.xlsx', engine='openpyxl', index=False)

# print the contents of the DataFrame
print(df.to_string())
