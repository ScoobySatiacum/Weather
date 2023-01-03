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
        self.configure(background="black")

        self.style = ttk.Style(self)
        self.style.configure("TButton", background="black")
        self.style.configure("TFrame", background="black")
        self.style.configure("TLabel", background="black", foreground="white")

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

    def update_widgets_forecast_weather(self, weather):

        # create the forecast weather frame
        self.forecast_weather_frame = ttk.Frame(self)

        # day 1
        self.day_one_frame = ttk.Frame(self.forecast_weather_frame)

        self.day_one_time = ttk.Label(self.day_one_frame, text = weather.daily_list[0].date)
        self.day_one_time.grid(column=0, row=0)
        self.day_one_temp_min_label = ttk.Label(self.day_one_frame, text = 'Min: ' + str(weather.daily_list[0].temp.min))
        self.day_one_temp_min_label.grid(column=1, row=0)
        self.day_one_temp_max_label = ttk.Label(self.day_one_frame, text = 'Max: ' + str(weather.daily_list[0].temp.max))
        self.day_one_temp_max_label.grid(column=2, row=0)
        day_one_icon = weather.daily_list[0].weather.image
        self.day_one_icon_label = ttk.Label(self.day_one_frame, image = day_one_icon)
        self.day_one_icon_label.grid(column=3, row=0)
        self.day_one_icon_label.image = day_one_icon

        self.day_one_frame.grid(column=0, row=0)

        separator1 = ttk.Separator(self.forecast_weather_frame, orient='horizontal')
        separator1.grid(column=0, row=1, sticky='ew')

        # day 2
        self.day_two_frame = ttk.Frame(self.forecast_weather_frame)

        self.day_two_time = ttk.Label(self.day_two_frame, text = weather.daily_list[1].date)
        self.day_two_time.grid(column=0, row=0)
        self.day_two_temp_min_label = ttk.Label(self.day_two_frame, text = 'Min: ' + str(weather.daily_list[1].temp.min))
        self.day_two_temp_min_label.grid(column=1, row=0)
        self.day_two_temp_max_label = ttk.Label(self.day_two_frame, text = 'Max: ' + str(weather.daily_list[1].temp.max))
        self.day_two_temp_max_label.grid(column=2, row=0)
        day_two_icon = weather.daily_list[1].weather.image
        self.day_two_icon_label = ttk.Label(self.day_two_frame, image = day_two_icon)
        self.day_two_icon_label.grid(column=3, row=0)
        self.day_two_icon_label.image = day_two_icon

        self.day_two_frame.grid(column=0, row=2)
        
        separator2 = ttk.Separator(self.forecast_weather_frame, orient='horizontal')
        separator2.grid(column=0, row=3, sticky='ew')

        # day 3
        self.day_three_frame = ttk.Frame(self.forecast_weather_frame)

        self.day_three_time = ttk.Label(self.day_three_frame, text = weather.daily_list[2].date)
        self.day_three_time.grid(column=0, row=0)
        self.day_three_temp_min_label = ttk.Label(self.day_three_frame, text = 'Min: ' + str(weather.daily_list[2].temp.min))
        self.day_three_temp_min_label.grid(column=1, row=0)
        self.day_three_temp_max_label = ttk.Label(self.day_three_frame, text = 'Max: ' + str(weather.daily_list[2].temp.max))
        self.day_three_temp_max_label.grid(column=2, row=0)
        day_three_icon = weather.daily_list[2].weather.image
        self.day_three_icon_label = ttk.Label(self.day_three_frame, image = day_three_icon)
        self.day_three_icon_label.grid(column=3, row=0)
        self.day_three_icon_label.image = day_three_icon

        self.day_three_frame.grid(column=0, row=4)
        
        separator3 = ttk.Separator(self.forecast_weather_frame, orient='horizontal')
        separator3.grid(column=0, row=5, sticky='ew')

        # day 4
        self.day_four_frame = ttk.Frame(self.forecast_weather_frame)

        self.day_four_time = ttk.Label(self.day_four_frame, text = weather.daily_list[3].date)
        self.day_four_time.grid(column=0, row=0)
        self.day_four_temp_min_label = ttk.Label(self.day_four_frame, text = 'Min: ' + str(weather.daily_list[3].temp.min))
        self.day_four_temp_min_label.grid(column=1, row=0)
        self.day_four_temp_max_label = ttk.Label(self.day_four_frame, text = 'Max: ' + str(weather.daily_list[3].temp.max))
        self.day_four_temp_max_label.grid(column=2, row=0)
        day_four_icon = weather.daily_list[3].weather.image
        self.day_four_icon_label = ttk.Label(self.day_four_frame, image = day_four_icon)
        self.day_four_icon_label.grid(column=3, row=0)
        self.day_four_icon_label.image = day_four_icon

        self.day_four_frame.grid(column=0, row=6)
        
        separator3 = ttk.Separator(self.forecast_weather_frame, orient='horizontal')
        separator3.grid(column=0, row=7, sticky='ew')

        # day 5
        self.day_five_frame = ttk.Frame(self.forecast_weather_frame)

        self.day_five_time = ttk.Label(self.day_five_frame, text = weather.daily_list[4].date)
        self.day_five_time.grid(column=0, row=0)
        self.day_five_temp_min_label = ttk.Label(self.day_five_frame, text = 'Min: ' + str(weather.daily_list[4].temp.min))
        self.day_five_temp_min_label.grid(column=1, row=0)
        self.day_five_temp_max_label = ttk.Label(self.day_five_frame, text = 'Max: ' + str(weather.daily_list[4].temp.max))
        self.day_five_temp_max_label.grid(column=2, row=0)
        day_five_icon = weather.daily_list[4].weather.image
        self.day_five_icon_label = ttk.Label(self.day_five_frame, image = day_five_icon)
        self.day_five_icon_label.grid(column=3, row=0)
        self.day_five_icon_label.image = day_five_icon

        self.day_five_frame.grid(column=0, row=8)
        
        separator3 = ttk.Separator(self.forecast_weather_frame, orient='horizontal')
        separator3.grid(column=0, row=9, sticky='ew')

        self.forecast_weather_frame.grid(column=0, row=3)

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
                    self.update_widgets_forecast_weather(wd)
            else:
                messagebox.showerror("Error", "Weather data could not be retrieved.")
        else:
            messagebox.showerror("Error", "Please enter valide location.\r\nCity format: Seattle, WA\r\nUS Zip Code: 00000")