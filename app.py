from email import message
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from geo import Geo
from utilities import Utilities
from weather import Weather

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        # use the grid geometry management
        self.pack()
        self.create_widgets()

        self.utilities = Utilities()
        self.weather = Weather()

    def create_widgets(self):
        # create a frame to contain the search widgets
        self.search_frame = ttk.Frame(self)
        # create a label for location entry
        self.location_label = ttk.Label(self.search_frame, text = 'Location: ')
        self.location_label.grid(column=0, row=0)

        # create an entry widget to capture user zip code
        self.location_entry = ttk.Entry(self.search_frame)
        self.location_entry.grid(column=1, row=0)

        # Create the application variable.
        self.location_var = tk.StringVar()
        
        # Create the search button
        self.search_button = ttk.Button(self.search_frame, text = 'Search', command = self.button_search)
        self.search_button.grid(column=2, row=0)

        # set the search frame to the overall grid
        self.search_frame.grid(column=0,row=0)

    def update_widgets_current_weather(self, weather):
        # create the current weather frame
        self.current_weather_frame = ttk.Frame(self)

        # current temp
        self.current_temp_label = ttk.Label(self.current_weather_frame, text = 'Current Temperature: {}'.format(weather.current.temp))
        self.current_temp_label.grid(column=0, row=0)

        # current humidity
        self.current_humidity_label = ttk.Label(self.current_weather_frame, text = 'Current Humidity: {}'.format(weather.current.humidity))
        self.current_humidity_label.grid(column=0, row=1)

        # current weather icon
        icon = weather.current.weather.image
        self.current_icon_label = ttk.Label(self.current_weather_frame, image = icon)
        self.current_icon_label.grid(column=1, row=0, rowspan=2)
        self.current_icon_label.image = icon

        # grid the frame
        self.current_weather_frame.grid(column=0, row=1)

    def update_widgets_hourly(self, weather):
        # create the hourly frame
        self.forecast_hourly_frame = ttk.Frame(self)
        
        # create the hourly temps
        self.hour_one_time = ttk.Label(self.forecast_hourly_frame, text = weather.next_12_hours[0].time_only)
        self.hour_one_time.grid(column=0, row=0)
        self.hour_one_temp_label = ttk.Label(self.forecast_hourly_frame, text = weather.next_12_hours[0].temp)
        self.hour_one_temp_label.grid(column=0, row=1)
        hour_one_icon = weather.next_12_hours[0].weather.image
        self.hour_one_icon_label = ttk.Label(self.forecast_hourly_frame, image = hour_one_icon)
        self.hour_one_icon_label.grid(column=0, row=2)
        self.hour_one_icon_label.image = hour_one_icon

        separator1 = ttk.Separator(self.forecast_hourly_frame, orient='vertical')
        separator1.grid(column=1, row=0, rowspan=3, sticky='ns')

        self.hour_two_time = ttk.Label(self.forecast_hourly_frame, text = weather.next_12_hours[1].time_only)
        self.hour_two_time.grid(column=2, row=0)
        self.hour_two_temp_label = ttk.Label(self.forecast_hourly_frame, text = weather.next_12_hours[1].temp)
        self.hour_two_temp_label.grid(column=2, row=1)
        hour_two_icon = weather.next_12_hours[1].weather.image
        self.hour_two_icon_label = ttk.Label(self.forecast_hourly_frame, image = hour_two_icon)
        self.hour_two_icon_label.grid(column=2, row=2)
        self.hour_two_icon_label.image = hour_two_icon

        separator2 = ttk.Separator(self.forecast_hourly_frame, orient='vertical')
        separator2.grid(column=3, row=0, rowspan=3, sticky='ns')

        self.hour_three_time = ttk.Label(self.forecast_hourly_frame, text = weather.next_12_hours[2].time_only)
        self.hour_three_time.grid(column=4, row=0)
        self.hour_three_temp_label = ttk.Label(self.forecast_hourly_frame, text = weather.next_12_hours[2].temp)
        self.hour_three_temp_label.grid(column=4, row=1)
        hour_three_icon = weather.next_12_hours[2].weather.image
        self.hour_three_icon_label = ttk.Label(self.forecast_hourly_frame, image = hour_three_icon)
        self.hour_three_icon_label.grid(column=4, row=2)
        self.hour_three_icon_label.image = hour_three_icon

        separator3 = ttk.Separator(self.forecast_hourly_frame, orient='vertical')
        separator3.grid(column=5, row=0, rowspan=3, sticky='ns')

        self.hour_four_time = ttk.Label(self.forecast_hourly_frame, text = weather.next_12_hours[3].time_only)
        self.hour_four_time.grid(column=6, row=0)
        self.hour_four_temp_label = ttk.Label(self.forecast_hourly_frame, text = weather.next_12_hours[3].temp)
        self.hour_four_temp_label.grid(column=6, row=1)
        hour_four_icon = weather.next_12_hours[3].weather.image
        self.hour_four_icon_label = ttk.Label(self.forecast_hourly_frame, image = hour_four_icon)
        self.hour_four_icon_label.grid(column=6, row=2)
        self.hour_four_icon_label.image = hour_four_icon

        separator4 = ttk.Separator(self.forecast_hourly_frame, orient='vertical')
        separator4.grid(column=7, row=0, rowspan=3, sticky='ns')

        self.hour_five_time = ttk.Label(self.forecast_hourly_frame, text = weather.next_12_hours[4].time_only)
        self.hour_five_time.grid(column=8, row=0)
        self.hour_five_temp_label = ttk.Label(self.forecast_hourly_frame, text = weather.next_12_hours[4].temp)
        self.hour_five_temp_label.grid(column=8, row=1)
        hour_five_icon = weather.next_12_hours[4].weather.image
        self.hour_five_icon_label = ttk.Label(self.forecast_hourly_frame, image = hour_five_icon)
        self.hour_five_icon_label.grid(column=8, row=2)
        self.hour_five_icon_label.image = hour_five_icon

        # grid the frame
        self.forecast_hourly_frame.grid(column=0, row=2)

    def update_widgets_forecast_weather(self, forecast_weather):
        # create the forecast weather frame
        self.forecast_weather_frame = ttk.Frame(self)



    def button_search(self):
        # retrieve user input from self.location_entry
        user_input = self.location_entry.get()
        # set the application variable self.location_var to ther user_input
        self.location_var.set(user_input)
        # validate user inputs
        if self.utilities.validate_user_input(user_input):
            g = Geo()
            geo = g.search_for_location(user_input)
            if geo:
                w = Weather()
                wd = w.get_weather_data(geo.lat, geo.lon)
                if wd:
                    self.update_widgets_current_weather(wd)
                    self.update_widgets_hourly(wd)
            else:
                messagebox.showerror("Error", "Weather data could not be retrieved.")
        else:
            messagebox.showerror("Error", "Please enter valide location.\r\nCity format: Seattle, WA\r\nUS Zip Code: 00000")