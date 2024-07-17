import pandas as pd
import matplotlib.pyplot as plt
import zipfile
import requests
import io

# URL for the World Bank dataset on total population
url = "http://api.worldbank.org/v2/en/indicator/SP.POP.TOTL?downloadformat=csv"

# Download the data
response = requests.get(url)
with zipfile.ZipFile(io.BytesIO(response.content)) as z:
    # Extract and read the CSV file
    with z.open('API_SP.POP.TOTL_DS2_en_csv_v2_5367607.csv') as f:
        population_data = pd.read_csv(f, skiprows=4)

# Preview the dataset
print(population_data.head())

# Process the data
# Drop columns that are not needed
population_data = population_data.drop(['Indicator Name', 'Indicator Code'], axis=1)
population_data = population_data.set_index('Country Name')

# Select data for a specific year, e.g., 2020
population_data_2020 = population_data[['2020']].dropna()

# Rename the column for easier access
population_data_2020 = population_data_2020.rename(columns={'2020': 'Population'})

# Plotting the data
# Create a bar chart of the population in 2020 for the top 10 most populous countries
top_10_countries = population_data_2020.sort_values(by='Population', ascending=False).head(10)

# Bar Chart
plt.figure(figsize=(12, 6))
plt.bar(top_10_countries.index, top_10_countries['Population'], color='skyblue')
plt.xlabel('Country')
plt.ylabel('Population in 2020')
plt.title('Top 10 Most Populous Countries in 2020')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Histogram
# Create a histogram of the population distribution in 2020
plt.figure(figsize=(10, 6))
plt.hist(population_data_2020['Population'], bins=30, color='skyblue', edgecolor='black')
plt.xlabel('Population')
plt.ylabel('Number of Countries')
plt.title('Distribution of Country Populations in 2020')
plt.tight_layout()
plt.show()
