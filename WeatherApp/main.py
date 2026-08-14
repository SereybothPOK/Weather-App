import sys
import requests
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_mainwindow import Ui_MainWindow
from PySide6.QtGui import QPixmap

class WeatherApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.getWeather_button.clicked.connect(self.search_weather)

        self.ui.temperature_label.hide()
        self.ui.weatherInfo_label.hide()
        self.ui.error_label.hide()
        self.ui.weather_icon.hide()

    def initUi():
        self.ui.sets

    def search_weather(self):
        self.ui.temperature_label.clear()
        self.ui.weatherInfo_label.clear()
        self.statusBar().clearMessage()
        self.ui.error_label.clear()
        self.ui.weather_icon.clear()
        city = self.ui.city_lineEdit.text()

        api_key = "d8869c11c36faf6531e8382dec36e9ff"

        url = "https://api.openweathermap.org/data/2.5/weather"

        params = {
            "q": city,
            "appid": api_key,
            "units": "metric",
        }

        try:
            response = requests.get(url, params=params, timeout=5)
            response.raise_for_status()

            data = response.json()

            temperature = str(data["main"]["temp"])
            weather = data["weather"][0]["description"]
            icon_id = data["weather"][0]["icon"]

            icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
            print(icon_url)

            image_data = requests.get(icon_url).content
            pixmap = QPixmap()
            pixmap.loadFromData(image_data)
            self.ui.weather_icon.show()
            self.ui.weather_icon.setPixmap(pixmap)


            self.ui.temperature_label.show()
            self.ui.weatherInfo_label.show()
            self.ui.temperature_label.setText(f"{temperature}°C")
            self.ui.weatherInfo_label.setText(weather)

            print(data["weather"])


        except requests.exceptions.HTTPError as e:
            self.ui.error_label.show()
            self.ui.error_label.setText("City Not Found: \n Please input the correct location")
            status_code = e.response.status_code
            reason = e.response.reason

            self.statusBar().showMessage(f"Error {status_code}:{reason}")

        except requests.exceptions.ConnectionError:
            self.ui.error_label.show()
            self.ui.error_label_setText("Error: No network connection")
            self.statusBar().showMessage("Error: No network connection")

        except requests.exceptions.Timeout:
            self.ui.error_label.show()
            self.ui.error_label_setText("Error: Request timed out")
            self.statusBar().showMessage("Error: Request timed out")

        except requests.exceptions.RequestException as e:
            self.statusBar().showMessage(f"Error: [{e}]")



app = QApplication(sys.argv)
weatherApp = WeatherApp()
weatherApp.show()
sys.exit(app.exec())

