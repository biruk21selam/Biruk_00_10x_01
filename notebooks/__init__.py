import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the datasets
df1 = pd.read_csv('../data/benin-malanville.csv')
df2 = pd.read_csv('../data/sierraleone-bumbuna.csv')
df3 = pd.read_csv('../data/togo-dapaong_qc.csv')

# Combine the datasets into one DataFrame
data = pd.concat([df1, df2, df3], ignore_index=True)

# Generate summary statistics
summary_stats = data.describe()
print(summary_stats)

# Check for missing values
missing_values = data.isnull().sum()
print("Missing Values:\n", missing_values)

# Convert Timestamp column to datetime format
data['Timestamp'] = pd.to_datetime(data['Timestamp'])

# Plot GHI over time
plt.figure(figsize=(12, 6))
plt.plot(data['Timestamp'], data['GHI'], label='GHI')
plt.title('Global Horizontal Irradiance Over Time')
plt.xlabel('Date')
plt.ylabel('GHI (W/m²)')
plt.legend()
plt.show()
