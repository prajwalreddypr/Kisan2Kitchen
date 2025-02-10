# import pandas as pd
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.preprocessing import LabelEncoder

# # Load the Excel file
# df = pd.read_excel('glcm_features.xlsx')

# # Separate the data into training and prediction sets
# train_df = df.dropna(subset=['Label'])
# predict_df = df[df['Label'].isna()]

# # Encode the labels as integers
# label_encoder = LabelEncoder()
# train_df['Label'] = label_encoder.fit_transform(train_df['Label'])

# # Split the data into features and labels
# X_train = train_df.drop('Label', axis=1)
# y_train = train_df['Label']
# X_predict = predict_df.drop('Label', axis=1)

# # Train the KNN classifier
# knn = KNeighborsClassifier(n_neighbors=3)
# knn.fit(X_train, y_train)

# # Predict the labels for the empty entries
# y_predict = knn.predict(X_predict)

# # Decode the predicted labels back to their original values
# predicted_labels = label_encoder.inverse_transform(y_predict)

# # Add the predicted labels to the original dataframe
# df.loc[df['Label'].isna(), 'Label'] = predicted_labels

# # Save the updated dataframe to a new Excel file
# df.to_excel('updated_excel_file.xlsx', index=False)


import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
import sys

# Get the input excel file name from the command line arguments
input_file = sys.argv[1]

# Load the Excel file
df = pd.read_excel(input_file)

# Separate the data into training and prediction sets
train_df = df.dropna(subset=['Label'])
predict_df = df[df['Label'].isna()]

# Encode the labels as integers
label_encoder = LabelEncoder()
train_df['Label'] = label_encoder.fit_transform(train_df['Label'])

# Split the data into features and labels
X_train = train_df.drop('Label', axis=1)
y_train = train_df['Label']
X_predict = predict_df.drop('Label', axis=1)

# Train the KNN classifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Predict the labels for the empty entries
y_predict = knn.predict(X_predict)

# Decode the predicted labels back to their original values
predicted_labels = label_encoder.inverse_transform(y_predict)

# Add the predicted labels to the original dataframe
df.loc[df['Label'].isna(), 'Label'] = predicted_labels

# Save the updated dataframe to a new Excel file
output_file = 'updated_new_excel_file.xlsx'
df.to_excel(output_file, index=False)

# Print the output file name to the console
print(output_file)
