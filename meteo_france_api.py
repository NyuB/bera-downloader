from typing import List
from dataclasses import dataclass
import requests as http
import json

@dataclass
class DateYMD:
    year: int
    month: int
    day: int

    def repr_yyyymmdd(self):
        return "{:04d}{:02d}{:02d}".format(self.year, self.month, self.day)
    
@dataclass
class MassifDay:
    massif: str
    date: str

class MassifDayAvailabilty:
    def __init__(self, massif: str, available_dates: List[str]):
        self.massif = massif
        self.available_dates = sorted(available_dates)
    
    def get_latest_available(self) -> MassifDay:
        return MassifDay(self.massif, self.available_dates[-1])

    def __repr__(self) -> str:
        return "massif: {}, available_dates: {}".format(self.massif, self.available_dates)



class BERAClient:
    def __init__(self, meteo_france_base_url: str = "https://donneespubliques.meteofrance.fr"):
        last_url_char = meteo_france_base_url[-1]
        self.meteo_france_base_url = meteo_france_base_url[:-1] if last_url_char == '/' else meteo_france_base_url

    def get_latest_bera_for_massif_day(self, massif: str, day: DateYMD):
        all = self.get_massif_availabilities_for_day(day)
        [latest_bera] = [i.get_latest_available() for i in all if i.massif == massif.upper()]
        return self.get_bera_for_massif_day(latest_bera)

    def get_bera_for_massif_day(self, massif_day: MassifDay) -> bytes:
        url = self.build_bera_pdf_url(massif_day.massif, massif_day.date)
        response = http.get(url, headers={"Accept":"application/pdf"}, stream=True)
        return response.content
    
    def get_massif_availabilities_for_day(self, day: DateYMD) -> List[MassifDayAvailabilty]:
        url = self.build_bera_massifs_json_url(day)
        response = http.get(url).text
        parsed_json_response  = json.loads(response)
        return [ MassifDayAvailabilty(massif_json["massif"], massif_json["heures"]) for massif_json in parsed_json_response ]
    
    def build_bera_massifs_json_url(self, day: DateYMD) -> str:
        return '/'.join([
            self.meteo_france_base_url, 
            "donnees_libres/Pdf/BRA",
            "bra.{}.json".format(day.repr_yyyymmdd())
        ])

    def build_bera_pdf_url(self, massif: str, day_repr: str) -> str:
        return '/'.join([
            self.meteo_france_base_url,
            "donnees_libres/Pdf/BRA",
            "BRA.{}.{}.pdf".format(massif.upper(), day_repr)
        ])
