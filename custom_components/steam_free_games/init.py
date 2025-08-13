from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.discovery import async_load_platform
from .const import DOMAIN

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    hass.data.setdefault(DOMAIN, {})
    await hass.async_add_executor_job(
        async_load_platform, hass, "sensor", DOMAIN, {}, entry
    )
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    return True
