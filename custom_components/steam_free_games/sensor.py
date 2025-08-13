import requests
from datetime import datetime
from dateutil import parser as _p
from homeassistant.components.sensor import SensorEntity
from .const import GIVEAWAYS_URL, DOMAIN, UPDATE_INTERVAL

PHRASES = [
    "🔥 T’as plus qu’à ajouter et oublier comme 90% des joueurs.",
    "🎉 Gratuit = meilleur prix. Ton banquier valide.",
    "👾 Ça se refuse pas, même pour un jeu tout claqué.",
    "🎮 Go agrandir ta bibliothèque Steam inutile.",
    "💸 0€, zéro effort, 100% satisfaction (ou pas).",
    "🧠 Ton cerveau dit non, mais ta collection dit OUI.",
    "📥 Clique, télécharge, n’y joue jamais. Classique.",
    "🕹️ T’as un SSD pour ça, non ?",
    "🔔 Ding dong ! C’est Steam avec un cadeau chelou.",
    "🐉 Spoiler : tu le finiras jamais."
]

def setup_platform(hass, config, add_entities, discovery_info=None):
    add_entities([SteamFreeGamesSensor()], True)

class SteamFreeGamesSensor(SensorEntity):
    def __init__(self):
        self._name = "Steam Free Games"
        self._state = None
        self._attributes = {}

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def extra_state_attributes(self):
        return self._attributes

    def update(self):
        try:
            r = requests.get(GIVEAWAYS_URL, params={"platform": "steam", "type": "game"}, timeout=10)
            r.raise_for_status()
            data = r.json()

            games = []
            for entry in data:
                if entry.get("status", "").lower() != "active":
                    continue

                ends = entry.get("end_date")
                try:
                    ends = _p.parse(ends) if ends and ends.upper() != "N/A" else None
                except:
                    ends = None

                games.append({
                    "title": entry.get("title", "").strip(),
                    "url": entry.get("open_giveaway_url") or entry.get("url") or "",
                    "end_date": ends.strftime('%d/%m/%Y %H:%M') if ends else "Inconnue",
                    "phrase": PHRASES[len(games) % len(PHRASES)]
                })

            if games:
                last_game = games[0]
                self._state = last_game["title"]
                self._attributes = {
                    "url": last_game["url"],
                    "end_date": last_game["end_date"],
                    "phrase": last_game["phrase"],
                    "all_games": games
                }
            else:
                self._state = "Aucun jeu gratuit"
                self._attributes = {}

        except Exception as e:
            self._state = "Erreur"
            self._attributes = {"error": str(e)}
