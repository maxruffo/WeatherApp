# WeatherApp

Sure, here's an example README.md file for your weather app project:

# Weather App

A simple weather app built with Python and PyQt5 that displays the current temperature for a specified city using the OpenWeatherMap API.

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/your-username/WeatherApp.git
   ```

2. Install the required packages:

   ```
   cd WeatherApp
   pip install -r requirements.txt
   ```

3. Create the a 'config' folder in the root, than create a 'token.py' file in this folder

4. Get an API key from [OpenWeatherMap](https://openweathermap.org/api) and add it to `config.py`:

   ```python
   # config.py

   API_KEY = 'your_api_key'
   ```

5. Run the app:

   ```
   python main.py
   ```

## Usage

1. Enter a city name in the input field.
2. Click the "Get Weather" button to retrieve the current temperature for the specified city.
3. The temperature will be displayed in Celsius.

## Contributing

Contributions are welcome! If you find a bug or want to suggest a new feature, please open an issue or submit a pull request.

