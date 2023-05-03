import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
from config.token import APIKEY

api_key = APIKEY

class WeatherApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.city_label = QLabel('Enter City:', self)
        self.city_label.move(50, 50)

        self.city_edit = QLineEdit(self)
        self.city_edit.move(150, 50)

        self.temp_label = QLabel('Temperature:', self)
        self.temp_label.move(50, 100)

        self.temp_display = QLabel(self)
        self.temp_display.move(150, 100)

        self.get_button = QPushButton('Get Weather', self)
        self.get_button.move(150, 150)
        self.get_button.clicked.connect(self.get_weather)

        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('Weather App')
        self.show()

    def get_weather(self):
        city = self.city_edit.text()
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        data = response.json()
        try:
            temp = data['main']['temp']
            self.temp_display.setText(f'{temp} °C')
        except:
            error = ("There was an Error with you API key, sometimes the API key needs a hour to be activated")
            self.temp_display.setText("Error")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    sys.exit(app.exec_())
