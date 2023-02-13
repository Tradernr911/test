import matplotlib.pyplot as plt

# Define the asset classes
asset_classes = ['Stock', 'Bond', 'Real Estate', 'Cash']

# Create a dictionary to store the values of each asset class
assets = {}

# Loop through each asset class and ask the user for the value of each asset
for asset_class in asset_classes:
    value = float(input(f'Enter the value of your {asset_class} assets: '))
    assets[asset_class] = value

# Calculate the total value of all assets
total_value = sum(assets.values())

# Calculate the percentage of each asset class
percentages = {asset_class: value / total_value for asset_class, value in assets.items()}

# Plot the pie chart
plt.pie(percentages.values(), labels=percentages.keys(), autopct='%1.1f%%')
plt.axis('equal')
plt.title('Asset Allocation by Percentage')
plt.show()
