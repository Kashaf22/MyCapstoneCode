# -*- coding: utf-8 -*-
"""ExtractActualTrajectory.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gDmPzVFb50mN0Dzha08fOEI6FculHBQD
"""

import pandas as pd

# Load the CSV file
df = pd.read_csv('/content/sample_data/filtered_accelerations.csv')

# Find the row with the maximum value in the 'Filtered X' column
max_row = df[df['Filtered X'] == df['Filtered X'].max()]

# Extract the maximum x and corresponding y value
max_x = max_row['Filtered X'].iloc[0]
corresponding_y = max_row['Filtered Y'].iloc[0]

# Print the results
print("Maximum value in x column:", max_x)
print("Corresponding value in y column when x is max:", corresponding_y)

# Save the results to a new CSV file
results = pd.DataFrame({'max_x': [max_x], 'corresponding_y': [corresponding_y]})
results.to_csv('max_x_corresponding_y.csv', index=False)