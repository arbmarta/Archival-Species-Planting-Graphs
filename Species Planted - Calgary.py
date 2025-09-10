import pandas as pd
import matplotlib.pyplot as plt

# Load the data from Excel
df = pd.read_excel('Calgary.xlsx')

# Filter the DataFrame to include only years between 1913 and 1941
df_filtered = df[(df['Year'] >= 1913) & (df['Year'] <= 1941)]

# Set the figure size
plt.figure(figsize=(15, 8), frameon=False)

# Columns for different tree types
tree_columns = ['Poplars (incl. Cottonwoods)', 'Spruce', 'Ash', 'Elm', 'Birch', 'Maple', 'Other', 'Unknown']

# Define a dictionary with a specific color for each tree type
color_dict = {
    'Poplars (incl. Cottonwoods)': 'CornflowerBlue',
    'Spruce': 'DarkGreen',
    'Ash': 'olivedrab',
    'Elm': 'Sienna',
    'Birch': 'GoldenRod',
    'Maple': 'Crimson',
    'Other': 'LightSalmon',
    'Unknown': 'LightGray'
}

# Prepare data for stacking
data_for_plotting = [df_filtered[col] for col in tree_columns]

# Extract colors for the columns based on the dictionary
colors = [color_dict[col] for col in tree_columns]

# Create a stack plot using the color dictionary
plt.stackplot(df_filtered['Year'], data_for_plotting, labels=tree_columns, colors=colors, alpha=0.5)

# Set x-axis and y-axis scales and limits
plt.xlim(1913, 1941)
plt.ylim(0, df_filtered[tree_columns].max().max() * 1.1)  # Adjusting y limit for better visibility

# Formatting x and y axis labels with increased size and bold font
plt.xlabel('Year', fontsize=16, fontweight='bold')
plt.ylabel('Number of Trees', fontsize=16, fontweight='bold')

plt.tick_params(axis='x', labelsize=14)  # Set x-axis tick label size
plt.tick_params(axis='y', labelsize=14)  # Set y-axis tick label size

# Adding vertical lines with dots and custom annotations
important_years = {
    1922: ("Maple More than 50% \nof Annual Planting", 2500),
    1925: ("Ash More than 20% \nof Annual Planting", 1500),
    1929: ("First Year Elm \nis Planted", 2500),
    1935: ("Poplar Less than 30% \nof Annual Planting", 1000)
}

for year, (text, y_value) in important_years.items():
    plt.vlines(x=year, ymin=0, ymax=y_value, colors='black', linestyles='-')
    plt.plot(year, y_value, 'ko')  # 'ko' means black dot
    plt.annotate(text, xy=(year, y_value), xytext=(5, 5), textcoords='offset points', fontsize=13)

# Configure legend to be inside the plot at the top right
plt.legend(title='Species Planted', title_fontsize=16, fontsize=13,
           loc='upper right', frameon=True)

# Save the figure
plt.savefig('Species Planted - Calgary.png', dpi=450)

# Display plot
plt.show()
