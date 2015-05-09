# -*- coding: utf-8 -*-
"""
Created on Sat May 09 17:20:05 2015

@author: alexis
"""

from datetime import timedelta

event_possibles = ['victime', 'incendit']


class Event(object):
    ''' un evenement (basique) c'est un lieu, une durée et
        un lieu de fin.
    '''

    def __init__(self, date, typ, lieu=(0,0), suite =(None,None)):
        assert typ in event_possibles
        assert isinstance(suite, tuple)
        assert len(suite) == 2
        duree = timedelta(minutes=suite[0])
        date_fin = date + duree
        # lieu_fin peut être l'hopital mais c'est peut être
        # inutile si on pense que la fin, c'est le retour à la caserne
        lieu_fin = suite[1]

        self.date = date
        self.type = typ
        self.lieu = lieu
        self.date_fin = date_fin
        self.lieu_fin = lieu_fin
