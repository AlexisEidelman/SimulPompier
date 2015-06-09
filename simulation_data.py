# -*- coding: utf-8 -*-
"""
Created on Thu Jun 04 13:39:37 2015

@author: Alexis Eidelman
"""

import read_bspp
from core.capacite import Capacite, Moyens
from core.evenement import Event


#
#tab = read_bspp.read()
#
#### initialisation
#
##### capacité
#vehicule = read_bspp.vehicule_table(tab)
#list_capa = []
#for ident, zone in vehicule.iterrows():
#    capacite = Capacite('vehicule', lieu=zone[0], etat='dispo')
#    list_capa += [capacite]
#
#moyens = Moyens(list_capa)
#
##### évenements
#intervention = read_bspp.intervention_table(tab)
#list_events = []
#for ident, serie in intervention.iterrows():
#    event = Event(serie['date'], serie['motif'], lieu=serie['zone'],
#                  suite=(serie['date_fin'] - serie['date'], serie['zone_fin']))

## réponse
#passage = read_bspp.vehicule_by_intervention(tab)
#passage = passage.join(intervention[['motif', 'motif_ini']])
#passage.groupby(['motif']).sum()
#
#un_motif = passage[passage.motif == 111]
#un_motif = un_motif.loc[:, (un_motif.sum(axis=0) != 0)]
## => rien de clair sur les véhicules



## réponse

### on décide qui prend en charge
#### on fait comme c'était simplement


#### on cherche la capacité utilisée dans la zone


# selection


#moyens.stats_de_base()
## prise en charge
#moyens.occupe(id_min, 'occupé', eve1.date_fin)
#moyens.stats_de_base()

## aucune simulation, juste les stats
dispo = list(vehicule.index.values)
n_vehicule = float(len(dispo))
indispo = []
# TODO: travailler avec des sets depuis le début
for temps, event in tab.iterrows():
    id_vehicule = event['id_vehicule']
    if event['statut'] == 'Disponible':
        if id_vehicule in indispo:
            indispo.pop(indispo.index(id_vehicule))
            dispo += [id_vehicule]
    else:
        if id_vehicule in dispo:
            dispo.pop(dispo.index(id_vehicule))
            indispo += [id_vehicule]

    assert len(set(dispo) & set(indispo)) == 0
    assert len(set(dispo) | set(indispo)) == n_vehicule
    print 100*len(dispo)/n_vehicule
