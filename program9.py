import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv(r"C:\Users\2BSCCSB31\Downloads\sample_visualization_dataset.csv")
print(data.head())

# Select a column
column_data = data['Temperature']

# Create plots
plt.figure(figsize=(16,5))

# Line plot
plt.subplot(1,3,1)
plt.plot(column_data)
plt.title('Line Plot')
plt.xlabel('Index')
plt.ylabel('Temperature')

# Box plot
plt.subplot(1,3,2)
sns.boxplot(y=column_data)
plt.title('Box Plot')

# Histogram
plt.subplot(1,3,3)
plt.hist(column_data, bins=10)
plt.title('Histogram')
plt.xlabel('Temperature')
plt.ylabel('Frequency')

# Show output
plt.tight_layout()
plt.show()
