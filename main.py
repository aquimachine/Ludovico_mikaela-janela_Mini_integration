import os
import requests
import xml.etree.ElementTree as ET
from lxml import etree

# Integration of API using OpenWeatherAPI
API_KEY = "29a96c07b0ebd3116f55d3d549166139" 
CITY = "Manila"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

print("Step 1: Data Fetching of Live Data from the API")
try:
    response = requests.get(URL)
    if response.status_code == 200:
        weather_data = response.json()
        print("Successfully fetched live data!")
    else:
        print(f"Missing/Invalid API (Status: {response.status_code}). Sample data loading...")
        weather_data = {
            "name": "Manila",
            "sys": {"country": "Ph"},
            "main": {"temp": 30.5, "feels_like": 35, "humidity": 72, "presure": 1013},
            "weather": [{"main": "Cloudy", "description": "cloudy skies"}],
            "wind": {"speed": 4.1}
        }
except Exception as e:
    print(f"Connection error ({e}). Sample data loading... ")
    weather_data = {
        "name": "Manila",
            "sys": {"country": "Ph"},
            "main": {"temp": 30.5, "feels_like": 35, "humidity": 72, "presure": 1013},
            "weather": [{"main": "Cloudy", "description": "cloudy skies"}],
            "wind": {"speed": 4.1}
    }

# Data Conversion
print("\nStep 2: Data conversion into XML")
root = ET.Element("WeatherData")

city_elem = ET.SubElement(root, "City")
city_elem.text = weather_data["name"]

country_elem = ET.SubElement(root,"Country")
country_elem.text = weather_data["sys"]["country"]

temp_elem = ET.SubElement(root, "Temperature")
temp_elem.text = str(weather_data["main"]["temp"])

humidity_elem = ET.SubElement(root, "Humidity")
humidity_elem.text = str(weather_data["main"]["humidity"])

condition_elem = ET.SubElement(root, "Condition")
condition_elem.text = weather_data["weather"][0]["main"]

desc_elem = ET.SubElement(root, "Description")
desc_elem.text = weather_data["weather"][0]["description"]

wind_elem = ET.SubElement(root, "WindSpeed")
wind_elem.text = str(weather_data["wind"]["speed"])

xml_bytes = ET.tostring(root, encoding="utf-8")
with open("data.xml", "wb") as f:
    f.write(xml_bytes)
print("File saved successfully! [data.xml]")

# Data Transformation
print("\nStep 3: XML transformation into HTML from XSLT")
if not os.path.exists("transform.xslt"):
    print("Error! transform.xslt file not found.")
else:
    xml_tree = etree.fromstring(xml_bytes)
    xslt_tree = etree.parse("transform.xslt")

    processor = etree.XSLT(xslt_tree)
    output_html = processor(xml_tree)

    with open("output.html", "wb") as f:
        f.write(output_html)
    print("Successful! output.html file saved")
