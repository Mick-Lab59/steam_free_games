from homeassistant.helpers.discovery import load_platform
from .const import DOMAIN

def setup(hass, config):
    if DOMAIN not in config:
        return True
    hass.data[DOMAIN] = config[DOMAIN]
    load_platform(hass, "sensor", DOMAIN, {}, config)
    return True
