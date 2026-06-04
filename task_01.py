import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
# World Bank CSV files have 4 extra lines before the actual header, so we use skiprows=4
df = pd.read_csv("API_SP.POP.TOTL_DS2_en_csv_v2_282912.csv", skiprows=4)

# Remove empty column if present
df = df.loc[:, ~df.columns.str.contains("Unnamed")]

# Select countries for visualization
selected_countries = [
    "India",
    "China",
    "United States",
    "Indonesia",
    "Pakistan",
    "Brazil",
    "Nigeria",
    "Bangladesh",
    "Russian Federation",
    "Mexico"
]

# Filter dataset for selected countries
population_data = df[df["Country Name"].isin(selected_countries)]

# Select year for visualization
year = "2023"

# Sort data by population
population_data = population_data.sort_values(by=year, ascending=False)

# Print selected data
print("Population data for selected countries in", year)
print(population_data[["Country Name", year]])

# Create bar chart
plt.figure(figsize=(12, 6))
plt.bar(population_data["Country Name"], population_data[year])

plt.title("Population Distribution of Selected Countries in 2023")
plt.xlabel("Country")
plt.ylabel("Population")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

# Save chart as image
plt.savefig("population_distribution_2023.png")

# Show chart
plt.show()