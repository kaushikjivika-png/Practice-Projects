# ==========================================================
# Project : Weather Data Analysis using NumPy
# Author  : Jivika Kaushik
# Language: Python
# Library : NumPy
# Dataset : Global Weather Repository Dataset
# ==========================================================

# Import libraries
import numpy as np
import os

# File Path
current_folder = os.path.dirname(__file__)
data_folder = os.path.join(current_folder,"01_Dataset")

file_path = os.path.join(data_folder,"GlobalWeatherRepository.csv")

# Read Headers
headers = np.genfromtxt(
    file_path,
    delimiter=",",
    max_rows=1,
    dtype=str,
    encoding="utf-8"
)

# Uncomment the below lines to view all dataset headers.
# print(headers)

# for i,column in enumerate(headers):
#     print(i,":",column)

# Selected columns used for analysis
usecols = (
    0,  # country
    1,  # Location_name
    7,  # temperature_celsius
    9,  # condition_text
    11, # wind_kph
    14, # pressure_mb
    18, # humidity
    19, # cloud
    20, # feels_like_celsius
    22, # visibility_km
    24, # uv_index
    26  # gust_kph
)

# Load first 5000 records from the dataset
weather_data = np.genfromtxt(
    file_path,
    delimiter=",",
    usecols=usecols,
    skip_header=1,
    max_rows=5000,
    dtype=str,
    encoding="utf-8"
)
print("\nWeather Dataset Loaded Successfully!")

# =====================================
# DATA UNDERSTANDING
# =====================================
print("\n========== DATASET OVERVIEW ==========")
rows,columns = weather_data.shape
print("Total Rows : ",rows)
print("Total Columns : ",columns)

# Unique Countries
print("\n========== COUNTRY INFORMATION ==========")
countries = np.unique(weather_data[:,0])
print("Total Unique Countries : ",len(countries))

# City information
print("\n========== CITY INFORMATION ==========")
cities = np.unique(weather_data[:,1])
print("Total Unique Cities : ",len(cities))

# Weather conditions
print("\n========== WEATHER CONDITIONS ==========")
conditions = np.unique(weather_data[:,3])
print("Total Weather Conditions : ",len(conditions))
print("\nAvailable Weather Conditions:",conditions)

# Missing values
print("\n========== MISSING VALUES ==========")
missing_values = np.sum(weather_data == "")
print("Total Missing Values : ",missing_values)

# Duplicate values
print("\n========== DUPLICATE VALUES ==========")
unique_rows = np.unique(weather_data,axis= 0)
duplicate_rows = rows-len(unique_rows)
print("Total Duplicate Rows : ",duplicate_rows)

# Duplicate records
print("\n========== DUPLICATE RECORDS ==========")
unique_rows, counts = np.unique(weather_data, axis=0, return_counts = True)
duplicate_data = unique_rows[counts > 1]
print(duplicate_data)

# Remove duplicate records
print("\n========== DATA AFTER CLEANING ==========")
weather_data = np.unique(weather_data, axis=0)
print("Rows After Removing Duplicates :", weather_data.shape[0])

# =====================================
# BASIC STATISTICS
# =====================================

temperature = weather_data[:,2].astype(float)
wind_speed = weather_data[:, 4].astype(float)
pressure = weather_data[:, 5].astype(float)
humidity = weather_data[:, 6].astype(int)
cloud = weather_data[:, 7].astype(int)
feels_like = weather_data[:, 8].astype(float)
visibility = weather_data[:, 9].astype(float)
uv_index = weather_data[:, 10].astype(float)
gust_speed = weather_data[:, 11].astype(float)

print("\n========== TEMPERATURE STATISTICS ==========")
print("Minimum Temperature : ", np.min(temperature), "°C")
print("Maximum Temperature : ", np.max(temperature), "°C")
print("Average Temperature : ", round(np.mean(temperature),2), "°C")

print("\n========== HUMIDITY STATISTICS ==========")
print("Minimum Humidity : ", np.min(humidity),"%")
print("Maximum Humidity : ", np.max(humidity),"%")
print("Average Humidity : ", round(np.mean(humidity),2),"%")

print("\n========== WIND SPEED STATISTICS ==========")
print("Minimum wind speed : ", np.min(wind_speed), "km/h")
print("Maximum wind speed : ", np.max(wind_speed), "km/h")
print("Average wind speed : ", round(np.mean(wind_speed),2), "km/h")

print("\n========== PRESSURE STATISTICS ==========")
print("Minimum Pressure : ", np.min(pressure), "mb")
print("Maximum Pressure : ", np.max(pressure), "mb")
print("Average Pressure : ", round(np.mean(pressure),2), "mb")

print("\n========== VISIBILITY STATISTICS ==========")
print("Minimum Visibility :", np.min(visibility), "km")
print("Maximum Visibility :", np.max(visibility), "km")
print("Average Visibility :", round(np.mean(visibility), 2), "km")

print("\n========== UV INDEX STATISTICS ==========")
print("Minimum UV Index :", np.min(uv_index))
print("Maximum UV Index :", np.max(uv_index))
print("Average UV Index :", round(np.mean(uv_index), 2))

print("\n========== GUST SPEED STATISTICS ==========")
print("Minimum Gust Speed :", np.min(gust_speed), "km/h")
print("Maximum Gust Speed :", np.max(gust_speed), "km/h")
print("Average Gust Speed :", round(np.mean(gust_speed), 2), "km/h")

print("\n========== HOTTEST CITY ==========")
hottest_index = np.argmax(temperature)

print("Country      : ",weather_data[hottest_index,0])
print("City         : ", weather_data[hottest_index,1])
print("Temperature  : ",temperature[hottest_index], "°C")
print("Condition    :", weather_data[hottest_index,3])
print("Feels Like   :", feels_like[hottest_index], "°C")

print("\n========== COLDEST CITY ==========")
coldest_index = np.argmin(temperature)

print("Country      : ", weather_data[coldest_index,0])
print("City         : ", weather_data[coldest_index,1])
print("Temperature  :", temperature[coldest_index], "°C")
print("Condition    :", weather_data[coldest_index,3])
print("Feels Like   :", feels_like[coldest_index], "°C")

print("\n========== HIGHEST HUMIDITY CITY ==========")
humidity_index = np.argmax(humidity)

print("Country     :", weather_data[humidity_index, 0])
print("City        :", weather_data[humidity_index, 1])
print("Humidity    :", humidity[humidity_index], "%")
print("Condition   :", weather_data[humidity_index,3])
print("Feels Like  :", feels_like[humidity_index], "°C")

print("\n========== HIGHEST WIND SPEED CITY ==========")
wind_index = np.argmax(wind_speed)

print("Country     :", weather_data[wind_index, 0])
print("City        :", weather_data[wind_index, 1])
print("Wind Speed  :", wind_speed[wind_index], "km/h")
print("Condition   :", weather_data[wind_index,3])
print("Feels Like  :", feels_like[wind_index], "°C")

print("\nWeather Data Analysis Completed Successfully!")