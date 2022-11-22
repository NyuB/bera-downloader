from meteo_france_api import BERAClient, DateYMD
from enum import Enum
import typer
import sys

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

def main(massif: MassifArgument, year: int, month: int, day: int, output_name: str = typer.Option("BERA.pdf", help = "Path of the output file to write bera to"), silent: bool = typer.Option(False, help = "Exit normally even when failing to retrieve the required BERA")):
    typer.echo("Getting BERA for {}".format(massif))
    try:
        client = BERAClient()
        bytes = client.get_latest_bera_for_massif_day(massif.value, DateYMD(year, month, day))
        with open(output_name, 'wb') as file:
            file.write(bytes)
    except Exception as e:
        print(e)
        if silent:
            sys.exit(-1)
        else:
            sys.exit(0)

if __name__ == "__main__":
    typer.run(main)