import requests

def get_weather_forecast(city_name, value):
    base_url = f"https://api.weatherapi.com/v1/current.json?key=db8a77d80571403785963644230611&q={city_name}&aqi={value}"

    try:
        response = requests.get(base_url)

        # Check for a successful response (status code 200)
        if response.status_code == 200:
            data = response.json()
            
            # Extract and display relevant information from the response body
            print("Weather forecast:")
            print(f"Location: {data['location']['name']}, {data['location']['region']}, {data['location']['country']}")
            print(f"Local Time: {data['location']['localtime']}")
            
            current_data = data['current']
            print(f"Temperature: {current_data['temp_c']}°C ({current_data['temp_f']}°F)")
            print(f"Condition: {current_data['condition']['text']}")
            print(f"Wind: {current_data['wind_kph']} kph, {current_data['wind_dir']}")
            print(f"Pressure: {current_data['pressure_mb']} mb")
            print(f"Humidity: {current_data['humidity']}%")

        else:
            print(f"Error: {response.status_code} - {response.text}\n")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    while True:
        try:
            city_name = input("Enter the name of city: ")
            value = "no"
            if city_name=='':
                print("Try again, city name cannot be blank")
                continue
            else:
                get_weather_forecast(city_name, value)
            ask=input("Do you want to find weather in another city (Yes/No)?\n").lower()
            if ask=="yes":
                continue
            else:
                print("Thank you, Have a nice day.")
                break
                            
        except ValueError:
            print("Try again")
