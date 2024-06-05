import pandas as pd

df = pd.read_csv('zomato_weather.csv')

mask = df.apply(lambda row: row.astype(str).str.contains('ZWL', case=False).any(), axis=1)
filtered_df = df[mask]
head_10 = filtered_df.head(10)
print(head_10)

def get_city_options():
    unique_cities = filtered_df['cityName'].unique()
    return unique_cities

def get_locality_options(city_name):
    filtered_df = df[df['cityName'] == city_name]
    
    # Extract unique locality names from the filtered dataframe
    localities = filtered_df['localityName'].unique()
    return localities

#locId from locName
def get_locid_from_locName(loc_name):
    locality_id = filtered_df.loc[filtered_df['localityName'] == loc_name, 'localityId'].iloc[0]
    return locality_id
