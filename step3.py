# import pandas as pd
# from sklearn.cluster import KMeans
# from sklearn.preprocessing import MinMaxScaler

# # Load the Excel file
# df = pd.read_excel('updated_new_excel_file.xlsx')

# # Drop any rows with missing values
# df = df.dropna()

# # Extract the feature columns and scale them
# X = df[['Entropy', 'Variance', 'Energy', 'Contrast', 'Homogeneity']]
# scaler = MinMaxScaler()
# X = scaler.fit_transform(X)

# # Use KMeans to cluster the data into 3 groups
# kmeans = KMeans(n_clusters=3, random_state=42)
# kmeans.fit(X)

# # Calculate the distance vectors for each entry
# distances = kmeans.transform(X)
# df['Distance'] = distances.min(axis=1)

# # Calculate the quality percentage for each entry
# df['Quality'] = 100 - ((df['Distance'] - distances.min()) /
#                        (distances.max() - distances.min())) * 100

# # Add the cluster labels to the dataframe
# df['Cluster'] = kmeans.labels_

# # Save the updated dataframe to a new Excel file
# df.to_excel('step3_output_file.xlsx', index=False)


import sys
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler

# Get input and output file paths from arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# Load the Excel file
df = pd.read_excel(input_file)

# Drop any rows with missing values
df = df.dropna()

# Extract the feature columns and scale them
X = df[['Entropy', 'Variance', 'Energy', 'Contrast', 'Homogeneity']]
scaler = MinMaxScaler()
X = scaler.fit_transform(X)

# Use KMeans to cluster the data into 3 groups
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)

# Calculate the distance vectors for each entry
distances = kmeans.transform(X)
df['Distance'] = distances.min(axis=1)

# Calculate the quality percentage for each entry
df['Quality'] = 100 - ((df['Distance'] - distances.min()) /
                       (distances.max() - distances.min())) * 100

# Add the cluster labels to the dataframe
df['Cluster'] = kmeans.labels_

# Save the updated dataframe to a new Excel file
df.to_excel(output_file, index=False)
