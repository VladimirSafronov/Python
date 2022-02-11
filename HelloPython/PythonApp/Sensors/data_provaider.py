from random import randint

def get_temperature(sensor):
    if sensor:
        return randint(-20, 0)
    else:
        return randint(0, 20)

def get_pressure(sensor):
    if sensor:
        return randint(720, 750)
    else:
        return randint(750, 770)

def get_wind_speed(sensor):
    if sensor:
        return randint(0, 10)
    else:
        return randint(10, 30)
