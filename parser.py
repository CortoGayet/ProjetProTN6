
import requests
import re
import json
#part 1 de la création du soup object
from bs4 import BeautifulSoup



URL = "https://reservation.imt-atlantique.fr/day.php?room=22&pview=1/"
page = requests.get(URL)

# part 2 de la création du soup object
# l'objet soup prend page.content as input
# content plutot que text, on évide les soucis d'encodage
# html.parser = class constructor
soup = BeautifulSoup(page.content, "html.parser")


#on cherche la balise <a> & l'élément id=afficherBoutonSelection1 pour récupérer le n° de la salle
salle = soup.find('a', id='afficherBoutonSelection1')
numero_salle = salle.get_text()

#on cherche tous les éléments avec le mot "type." (le . c'est pour n'importe quel caractère) pour récupérer la classe de la réservation
elements = soup.find_all(
    class_=re.compile(r'\btype.\b')
)

#Objet unique pour la salle 
data_json = {
    "salle": {
        "numero": numero_salle
    },
    "reservations": []
}
#array pour les réservations
for data in elements:
    reservation = {
        "heure": data.contents[0],
        # "service": data.contents[2],
        "nom": data.contents[4],
        # "outil": data.contents[6],
    }
#Ajout des données nom et heures extraite de la page dans mon data_python
data_json["reservations"].append(reservation)
#JSONification, bang bang gang gang.
#print(data_json)
