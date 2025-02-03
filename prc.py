import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

def fetch_weather_data(url):
    # Send a request to the weather website
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract data
    days = soup.find_all('span', class_='day-detail')  # Modify class based on actual website
    temps = soup.find_all('span', class_='temp')       # Modify class based on actual website
    
    weather_data = {
        'days': [day.get_text() for day in days],
        'temps': [int(temp.get_text().replace('°', '')) for temp in temps]
    }
    return weather_data

def plot_weather_data(weather_data):
    plt.figure(figsize=(10, 5))
    plt.plot(weather_data['days'], weather_data['temps'], marker='o')
    plt.title('Weekly Temperature Overview')
    plt.xlabel('Day of the Week')
    plt.ylabel('Temperature (°C)')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    url = 'https://www.weatherwebsite.com'  # Replace with actual URL
    weather_data = fetch_weather_data(url)
    plot_weather_data(weather_data)
