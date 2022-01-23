from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1' # Solo para eliminar el mensaje en consola de pygame
import pygame, sys, time, requests, os
from dotenv import load_dotenv

    
load_dotenv()
pygame.init()
size = (375,667)
s_width = 375
s_height = 667
margin_left = 50

# Variables globales
margin_left=40

# Definimos colores:
BLACK = (0,0,0)
WHITE = (255,255,255)

# Creamos una ventana
screen = pygame.display.set_mode(size)

# Añadimos el icono y cambiamos el titulo de la ventana 
icon_screen = pygame.image.load('icon.png')
pygame.display.set_icon(icon_screen)
pygame.display.set_caption('Weather App - Harold Ormeño')

# Controlar FPS
clock = pygame.time.Clock()

# Variables para fondo (Día y noche)
background_day = pygame.image.load("after_noon.jpg")
background_night = pygame.image.load("night.jpg")

# Traemos la hora actual
time_hour = int(time.strftime("%H", time.localtime()))
background_day_draw = False
background_night_draw = False

if time_hour < 18:
    background_day_draw = True
    background_night_draw = False
    margin_top_icon = 0
    margin_left_icon = s_width/2-(132/2)
    icon_select = 'sunny'

elif time_hour > 18:
    background_day_draw = False
    background_night_draw = True
    icon_select = 'night'
    margin_left_icon = s_width/2-(132/2)
    margin_top_icon = 0



# Definimos las variables necesarias para crear nuestro input
# <--------                     -------->

#Creamos la fuente del texto
base_font = pygame.font.SysFont("segoeui", 32) #
screen_user_text = 'Your city' # Input vacio - almacena el country

# Creamos el rect para el input
input_rect = pygame.Rect(margin_left,600,240,48)
color_rect_input_active = pygame.Color('#FF968C') #FF968C
color_rect_input_passive = pygame.Color('#ffffff')
color_rect_input = color_rect_input_passive

active = False
first_bucle = True
last_letter_deleted = []
user_text = ''

# Variables para mostrar info en pantalla

temperature = 'N/A'
wind_speed = 'N/A'
humidity = 'N/A'
general_condition = 'N/A'
error_text = ''
temp_label_text = pygame.font.SysFont("segoeui", 64)
text_small_font = pygame.font.SysFont("segoeui", 12)

# Variables para la parte mejoras del input
end_time = 0
delay_deleted = 150


def get_weather(country=None):
    try:
        if country == None:
            raise KeyError

    except KeyError:
        return None

    datos_dicc = {}
    API_key = os.environ.get('API_KEY')
    URL = "https://api.openweathermap.org/data/2.5/weather"
    parameters = {"APPID": API_key, "q": country, "units": "metric"}
    res = requests.get(URL, params = parameters)
    data = res.json()
    try:
        temp = data["main"]["temp"]
        wind_speed = data["wind"]["speed"]
        humidity = data["main"]["humidity"]
        main = data["weather"][0]["main"]
        description = data["weather"][0]["description"]
        icon = data["weather"][0]["icon"]
        datos_dicc['temp'] = temp
        datos_dicc['wind_speed'] = wind_speed
        datos_dicc['humidity'] = humidity
        datos_dicc['main'] = main
        datos_dicc['description'] = description
        datos_dicc['icon'] = icon
    except KeyError:
        datos_dicc['temp'] = 'N/A'
        datos_dicc['wind_speed'] = 'N/A'
        datos_dicc['humidity'] = 'N/A'
        datos_dicc['main'] = 'N/A'
        datos_dicc['description'] = 'N/A'
        datos_dicc['icon'] = '03d'
        icon = "sunny.png"
        return datos_dicc
    return datos_dicc


def main(screen):
    global active, user_text, screen_user_text, color_rect_input, first_bucle, text_surface, temperature,wind_speed,humidity,general_condition, end_time,delay_deleted, icon_select, margin_top_icon, margin_left_icon, error_text
    collision_time = True
    while True:
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                sys.exit()
            # Detectamos si el place del input está seleccionado
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                    if collision_time == True:
                        screen_user_text = ''
                        collision_time = False
                else:
                    active = False
            # Registramos las teclas(letras) de entrada brindados por el usuario
            if event.type == pygame.KEYDOWN:
                if active == True:
                    if event.key == pygame.K_RETURN:
                        the_weather = get_weather(user_text)
                        try:
                            temperature = int(round(the_weather["temp"],0))
                            wind_speed = the_weather["wind_speed"]
                            humidity = the_weather["humidity"]
                            general_condition = the_weather["main"]
                            icon_select = the_weather['icon']
                            margin_top_icon = 44
                            margin_left_icon = s_width/2-(100/2)
                            error_text = ''

                        except TypeError:
                            icon_select = ''
                            temperature = 'N/A'
                            wind_speed = 'N/A'
                            humidity = 'N/A'
                            general_condition = 'N/A'
                            error_text = 'City not found'
                            if background_night_draw == True:
                                margin_top_icon = 0
                                margin_left_icon = s_width/2-(132/2)
                                icon_select = 'night'
                            else:
                                icon_select = 'sunny'
                                margin_top_icon = 0
                                margin_left_icon = s_width/2-(132/2)

                    elif event.key != pygame.K_RETURN and event.key != pygame.K_BACKSPACE:
                        screen_user_text += event.unicode
                        user_text += event.unicode

        # Borrado continuo (input label)
        if active == True:
            if keys[pygame.K_BACKSPACE]:
                now_time = pygame.time.get_ticks()
                if now_time - end_time >= delay_deleted:
                    end_time = now_time
                    try:
                        user_text = user_text[:-1]
                        screen_user_text = screen_user_text[:-1]
                        last_letter = last_letter_deleted.pop()
                        screen_user_text = f"{last_letter}{screen_user_text}"
                        delay_deleted -= 10
                    except IndexError:
                        pass
            else:
                delay_deleted = 150


        # --- LOGICA PARA CAMBIAR COLOR DEL LABEL INPUT
        if active:
            color_rect_input = color_rect_input_active
        else:
            color_rect_input = color_rect_input_passive

        # --- LOGICA PARA CAMBIAR COLOR DEL LABEL INPUT

        screen.fill(BLACK)
        if background_night_draw == True:
            screen.blit(background_night,(0,0))
        elif background_day_draw == True:
            screen.blit(background_day,(0,0))

        if first_bucle == False:
            if text_surface.get_width()+10 > 240:
                last_letter_deleted.append(screen_user_text[0]) # Añade a la lista el primer caracter después del limite
                screen_user_text = screen_user_text[1:]

        text_surface = base_font.render(screen_user_text, True, (255,255,255))
        if first_bucle == True:
            first_bucle = False
        
        ## ----- ZONA DE DIBUJO

        pygame.draw.line(screen, color_rect_input, (margin_left,648), (margin_left+248, 648)) # Linea de decoración para el titulo
        temp_surface = temp_label_text.render(str(temperature)+'°', True,WHITE)

        #Para la información pequeña:
        wind_speed_text = text_small_font.render(f"Wind Speed: {wind_speed}", True,WHITE)
        humidity_text = text_small_font.render(f"Humidity: {humidity}", True,WHITE)
        main_text = text_small_font.render(f"General: {general_condition}", True,WHITE)
        error_label = text_small_font.render(f"{error_text}", True, WHITE)

        # Para el icono del clima
        icon_weather = pygame.image.load(f".\Icons\{icon_select}.png").convert_alpha()

        screen.blit(error_label,(margin_left+10,588))
        screen.blit(wind_speed_text,(s_width-(margin_left/2+wind_speed_text.get_width()), 10))
        screen.blit(humidity_text,(s_width-(margin_left/2+humidity_text.get_width()), 25)) 
        screen.blit(main_text,(s_width-(margin_left/2+main_text.get_width()), 40)) 
        
        screen.blit(text_surface,(margin_left+10, input_rect.y))
        screen.blit(icon_weather,(margin_left_icon,margin_top_icon))
        screen.blit(temp_surface,((s_width/2-(temp_surface.get_width()/2))+25/2,130)) 

        ## ----- ZONA DE DIBUJO

        #Actualizar pantalla
        pygame.display.flip()
        #Controlamos los FPS
        clock.tick(60)


def main_menu(screen):
    get_weather()
    main(screen)


main_menu(screen)