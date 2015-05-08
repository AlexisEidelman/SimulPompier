# -*- coding: utf-8 -*-
"""
Modele simple

Created on Fri May 08 17:38:26 2015

@author: alexis
"""

capacites_possibles = ['vehicule', 'ambulance']
etats_possibles = ['dispo', 'occupé']
event_possible = ['victime', 'incendit']

class Capacite(object):
    ''' un capacité est définie par :
            - un type
            - un lieu
            - un état
            
    # Dans un second temps les capacités devraient être 
    # la rencontre d'un véhicule et d'un nombre de personnels
    # mais c'est du niveau 2
    '''
    
    def __init__(typ, lieu=(0,0), etat='dipso'):
        assert typ in capacites_possibles
        assert etat in etats_possibles
        self.type = typ
        self.lieu = lieu
        self.etat = etat
        
    
class Event(object):
    ''' un evenement (basique) c'est un lieu, une durée et 
        un lieu de fin.
    '''
        
    def __init__(date, typ, lieu=(0,0), suite):
        assert typ in event_possibles
        assert isinstance(suite, tuple)
        assert len(suite) == 2
        duree = suite[0]
        date_fin = date + duree
        lieu_fin = suite[1]
        
        self.date = date
        self.type = typ
        self.lieu = lieu
        self.date_fin = date_fin
        self.lieu_fin = lieu_fin        


        
    