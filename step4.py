import pandas as pd

# Load the Excel file
df = pd.read_excel('final.xlsx')

# Set the price based on the Label and Quality values
price = []
for label, quality in zip(df['Label'], df['Quality']):
    if label == 'good':
        price.append(100 * quality / 100)  # good price -100
    elif label == 'avg':
        price.append(75 * quality / 100)  # avg price - 75
    elif label == 'bad':
        price.append(50 * quality / 100)  # bad price - 50
    else:
        price.append(0)

# Add the price column to the dataframe
df['Price'] = price

# Save the updated dataframe to a new Excel file
df.to_excel('price_final.xlsx', index=False)
