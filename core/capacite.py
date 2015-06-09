# -*- coding: utf-8 -*-
"""
Created on Sat May 09 17:21:07 2015

@author: alexis
"""

from datetime import datetime

capacites_possibles = ['vehicule', 'ambulance']
etats_possibles = ['dispo', 'occupé']


class Capacite(object):
    ''' un capacité est définie par :
            - un type
            - un lieu
            - un état

    # Dans un second temps les capacités devraient être
    # la rencontre d'un véhicule et d'un nombre de personnels
    # mais c'est du niveau 2
    '''

    def __init__(self, typ, lieu=(0,0), etat='dipso',
                 retour_dispo=None):
#        import pdb; pdb.set_trace()
        assert typ in capacites_possibles
        assert etat in etats_possibles
        if etat == 'dispo':
            assert retour_dispo is None
        else:
            assert isinstance(retour_dispo, datetime)

        self.type = typ
        self.lieu = lieu
        self.etat = etat
        self.retour_dispo = retour_dispo

    def devient_dispo(self):
        self.retour_dispo = None
        self.etat = 'dispo'

    def devient_occupe(self, etat, date_fin):
        self.etat = etat
        self.retour_dispo = date_fin


class Moyens(object):
    ''' les moyens sont un ensemble de capacités '''

    def __init__(self, capacites):
        assert isinstance(capacites, list)
        capacites_par_etat = {}
        for etat in etats_possibles:
            capacites_par_etat[etat] = []
        for capacite in capacites:
            assert isinstance(capacite, Capacite)
            etat = capacite.etat
            capacites_par_etat[etat].append(capacite)
        self.capacites = capacites_par_etat

    def update(self, date):
        ''' regarde si de nouvelles capacités sont disponibles à la date '''
        capacites = self.capacites.keys()
        capacites.remove('dispo')
        new_dispo = []
        for etat in capacites:
            occupes = self.capacites[etat]
            new_dispo += [occupe for occupe in occupes
                          if occupe.retour_dispo <= date]
            self.capacites[etat] = [occupe for occupe in occupes
                                    if occupe not in new_dispo]

        new_dispo = [capacite.devient_dispo() for capacite in new_dispo]
        self.capacites[etat] += new_dispo

    def dispo(self):
        return self.capacites['dispo']

    def stats_de_base(self):
        capacites = self.capacites
        taille = {}
        taille_tot = 0.0
        for etat, liste in capacites.iteritems():
            taille[etat] = len(liste)
            taille_tot += len(liste)

        for etat in capacites:
            print('    pourcentage de véhicule ' + etat)
            print(100*taille[etat]/taille_tot)


    def occupe(self, idx, etat, date_fin):
        '''change l'élement numéro idx de la liste des capacités dispos
            et le passe dans l'état en lui mettant une date de retour fin
        '''
        assert etat in etats_possibles
        assert etat != 'dispo'

        capacite = self.capacites['dispo'][idx]
        capacite.devient_occupe(etat, date_fin)
        self.capacites[etat].append(capacite)
        self.capacites['dispo'].pop(idx)
