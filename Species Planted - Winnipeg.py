import pandas as pd
import matplotlib.pyplot as plt

# Load the data from Excel
df = pd.read_excel('Winnipeg.xlsx')

# Filter the DataFrame to include only years between 1913 and 1941
df_filtered = df[(df['Year'] >= 1945) & (df['Year'] <= 1971)]

# Set the figure size
plt.figure(figsize=(15, 8), frameon=False)

# Columns for different tree types
tree_columns = ['Elm', 'Ash', 'Birch', 'Linden/Basswood', 'Cherries, Apples, and Plums', 'Ornamental', 'Other', 'Unknown']


# Define a dictionary with a specific color for each tree type
color_dict = {
    'Elm': 'Sienna',
    'Ash': 'olivedrab',
    'Birch': 'GoldenRod',
    'Linden/Basswood': 'lightgreen',
    'Cherries, Apples, and Plums': 'Crimson',
    'Ornamental': 'CornflowerBlue',
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
plt.xlim(1945, 1971)
plt.ylim([0, None])  # Adjusting y limit for better visibility

# Formatting x and y axis labels with increased size and bold font
plt.xlabel('Year', fontsize=16, fontweight='bold')
plt.ylabel('Number of Trees', fontsize=16, fontweight='bold')

# Adding vertical lines with dots and custom annotations
important_years = {
    1946: ("Six Ash Trees \nPlanted", 1000),
    1949: ("230 Ash Trees \nPlanted", 800),
    1958: ("First Year Ornamental \nSpecies are Planted", 2500),
    1960: ("Ornamental Species \nDifferentiated", 2300),
    1966: ("First DED-Resistant \nElm Species Planted", 2000),
    1970: ("49 Siberian \nElm Planted", 1200)
}

for year, (text, y_value) in important_years.items():
    plt.vlines(x=year, ymin=0, ymax=y_value, colors='black', linestyles='-')
    plt.plot(year, y_value, 'ko')  # 'ko' means black dot
    if year == 1958:
        # Special case for 1958, align text to the left of the dot
        plt.annotate(text, xy=(year, y_value), xytext=(-5, 5), textcoords='offset points', fontsize=13,
                     ha='right')
    elif year == 1970:
        # Special case for 1958, align text to the left of the dot
        plt.annotate(text, xy=(year, y_value), xytext=(-5, 5), textcoords='offset points', fontsize=13,
                     ha='right')
    else:
        plt.annotate(text, xy=(year, y_value), xytext=(5, 5), textcoords='offset points', fontsize=13)

# Configure legend to be inside the plot at the top right
plt.legend(title='Species Planted', title_fontsize=16, fontsize=13, loc='upper left', frameon=True)

plt.tick_params(axis='x', labelsize=14)  # Set x-axis tick label size
plt.tick_params(axis='y', labelsize=14)  # Set y-axis tick label size

# Save the figure
plt.savefig('Species Planted - Winnipeg.png', dpi=450)

# Display plot
plt.show()
