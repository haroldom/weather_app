#  Weather App with Python ☀️☔️
This is a weather application made with Python using Pygame.

![](https://img.shields.io/github/repo-size/haroldom/weather_app?style=for-the-badge) ㅤ
[![Made with python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://github.com/itsvinayak/weather-app)

------------


![Alt Text](https://s10.gifyu.com/images/weather_app.gif)

*An example of how to use the weather application.*

------------


### Pygame

Pygame is a set of Python modules designed for writing video games. Pygame adds functionality on top of the excellent SDL library. This allows you to create fully featured games and multimedia programs in the python language.

You can read more about Pygame, <a href="https://www.pygame.org/wiki/about" >here</a>.


####  What is virtual environment?
A virtual environment is a Python environment such that the Python interpreter, libraries and scripts installed into it are isolated from those installed in other virtual environments, and (by default) any libraries installed in a "system" Python, i.e., one which is installed as part of your operating system.

You can read more about virtual environments, <a href="https://docs.python.org/3/library/venv.html#:~:text=A%20virtual%20environment%20is%20a,part%20of%20your%20operating%20system." >here</a>.

## Setup

- Install dependencies
   
  - `pip install -r requirements.txt`
- Add environment variables
  - Create a file with the name **.env**.
   `touch .env`
  
  - Write in the **.env** file the **API_KEY**
   `API_KEY="################################";`. The API_KEY is the API key received from registering at [openweathermap.org](https://openweathermap.org/current "openweathermap.org")

- Run
  - If you are on Mac or linux
   `python main.py`
  -  If you are on Windows
   `py main.py`
   
Note: each application contains its own requirements

## Functionality
It asks for the name of the city and country as input and then uses https://openweathermap.org/current to get information on what the weather is like in that specific location. We get a file in JSON format and then display this information using pygame functions.

To work on this locally clone the repo, request and add an API key (locally) from openweathermap and then run main.py

[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
