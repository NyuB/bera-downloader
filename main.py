from meteo_france_api import BERAClient, DateYMD
import typer
from enum import Enum

class MassifArgument(Enum):
    ARRAVIS = "ARRAVIS"
    BELLEDONNE = "BELLEDONNE"
    CHARTREUSE = "CHARTREUSE"
    OISANS = "OISANS"
    VANOISE = "VANOISE"
    VERCORS = "VERCORS"

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self)

def main(massif: MassifArgument, year: int, month: int, day: int, output_name: str = typer.Option("BERA.pdf", help = "Path of the output file to write bera to")):
    typer.echo("Getting BERA for {}".format(massif))
    client = BERAClient()
    bytes = client.get_latest_bera_for_massif_day(massif.value, DateYMD(year, month, day))
    with open(output_name, 'wb') as file:
        file.write(bytes)

if __name__ == "__main__":
    typer.run(main)