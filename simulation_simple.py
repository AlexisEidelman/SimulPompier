# -*- coding: utf-8 -*-
"""
Created on Fri May 08 18:59:23 2015

@author: alexis
"""

import numpy as np
from datetime import datetime
from core.capacite import Capacite, Moyens
from core.evenement import Event

# on définit deux véhicule sur deux positions.
capa1 = Capacite('vehicule', lieu = (-1,0), etat='dispo')
capa2 = Capacite('vehicule', lieu = ( 1,0), etat='dispo')
moyens = Moyens([capa1, capa2])

# génération d'évenement
eve1 = Event(datetime(2012,1,1,1,1,1), 
             'victime', lieu=(0,5), 
             suite =(50.1,(0,5))
             )

## réponse
lieu = eve1.lieu
date = eve1.date

moyens.update(date)


# on décide qui prend en charge
temps_arrivee = []
# choix de la capacité
for capa in moyens.dispo():
    # calcul des temps d'arrivée
    arrivee = (capa.lieu[0] - lieu[0])**2 + (capa.lieu[1] - lieu[1])**2
    temps_arrivee.append(arrivee)
# selection
id_min = np.asarray(temps_arrivee).argmin()

moyens.stats_de_base()
# prise en charge
moyens.occupe(id_min, 'occupé', eve1.date_fin)
moyens.stats_de_base()
# génération d'évenement
eve1 = Event(datetime(2012,1,1,1,1,1), 
             'victime', lieu=(0,5), 
             suite =(50.1,(0,5))
             )
