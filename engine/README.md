# Alembic handleiding

## Inleiding
Deze readme is puur voor als je iets wil leren over migrations en ORM gerelateerde
dingen dan kan je deze handleiding volgen en ook als je geen zin
hebt om dit te leren het kan super handig zijn omdat die je code super
schoon houdt en het heel kort en krachtig houdt.

## Prerequisites 
Als eerst moet je de volgende dependencies hebben geinstalleerd, dit kan je
doen door de volgende command te runnen in je PyCharm terminal:
`pip install sqlalchemy && pip install alembic`

## Handleiding
alembic bestaat eigenlijk uit 3 delen, je hebt de tabellen, ORM en de CLI (command line interface)

**Sidenote**

De eerste 2 delen van deze handleiding zijn voor als je nieuwe
tabellen wilt genereren. Wanneer je dat al hebt gedaan en je iets wil aanpassen
in je tabel dan kan je dat in het python bestand doen en direct naar het gedeelte
`CLI` gaan.z
###Tabellen
Dit is een format voor een tabel, als je dit volgt kan je altijd makkelijk
tabellen maken (De comments geven commentaar op de code eronder)
```python
#Dit zijn de type kollomen die je kan importeren, denk aan Integers,
# Strings enzovoort. Elk datatype in MySQL zit ook in sqlalchemy
# Column heb je altijd nodig want die zorgt er voor
# dat er een kolom komt wordt gegenereerd
from sqlalchemy import Column, String, Integer
#Dit moet je altijd importeren omdat dit een basis
#Maakt voor je python code naar MySQL
from sqlalchemy.ext.declarative import declarative_base

#Dit is dus je base, dit heb je altijd nodig om een tabel te maken
Base = declarative_base()

#Een class met de naam van de tabel, de naam moet in 1 woord
#vertellen wat het is, je importeert in de class de Base want daardoor
#Weet alembic van 'hey dit is een tabel'
class Order(Base):
#De tabelnaam hoe die te zien is in MySQL
    __tablename__ = "orders"
#Dit is dus een kolom, het maakt gebruik van het volgende formaat:
# naamKolom = Column(type, primarykey=T/F)
# Primarykey hoef je maar 1 keer in te vullen
    id = Column(Integer(), primarykey=True)
    #Bij een string moet je altijd aangeven hoelang de string is,
    #Wanneer je niet weet hoelang de string is gewoon 255 als lente gebruiken 
    orderNaam = Column(String(255))
```

Zonder comments ziet het er zo uit:
```python
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer(), primary_key=True)
    orderNaam = Column(String(255))
```

###ORM
Zoals je ziet in de directory `engine/alembic` zit er een env.py bestand,
in dit bestand moet je alle tabellen importen zodat alembic ze automatisch
kan genereren.

Je moet naar `regel 21` gaan om je tabel te importeren naar alembic. Wat je hier
doet is het volgende:
- boven `target_metadata = []` staat `from engine.migrations import bestandsnaam`
- Wanneer dat er niet staat dan zet je `from engine.migrations import bestandsnaam ` neer
- Als het er wel al staat dan doe voeg je jouw bestandsnaam er achter aan toe,
voorbeeld: `from engine.migrations import file1, file2, file3` enzovoort
- Daarna voeg je bij de array van target_metadata het volgende toe:
`target_metadata = [bestandsnaam.Base.metadata]`
- Voor elk bestand voeg je het toe aan de array van target_metadata.
Elke keer met dit format: `bestandsnaam.Base.metadata`

Wat doet dit nou eigenlijk? Alembic kan hierdoor nu je tabellen
vinden en zal die daardoor ook gaan autogenereren. Als je dit niet doet
kan alembic ze niet vinden en worden er ook geen tabellen aangemaakt.

### CLI
Nu het laatste deel, dit deel is zeer kort en hier kan veel fout gaan.

wanneer je de vorige stappen heb gedaan of als je iets hebt aangepast
in je tabel. Dan doe je de volgende command:

`alembic revision --autogenerate -m "message"`

Dit zorgt ervoor dat de bestanden worden omgezet van alembic naar ORM

Hierna doe je de volgende command:

`alembic upgrade head`

Hierdoor update je de database op de server. Wanneer je dit hebt gedaan moet je
meteen een git commit doen anders krijgen de rest van de teamleden
een error dat ze niet dezelfde versies hebben.

# Contact
Vragen?

fabio.dijkshoorn@student.hu.nl
