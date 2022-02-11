import data_provaider as prov
import logger

def temperature_view(sensor):
    data = prov.get_temperature(sensor)
    logger.tempereture_logger(data)
    return data

def pressure_view(sensor):
    data = prov.get_pressure(sensor)
    logger.pressure_logger(data)
    return data

def wind_speed_view(sensor):
    data = prov.get_wind_speed(sensor)
    logger.wind_speed_logger(data)
    return data