# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.shortcuts import render
from django.http import HttpResponse
from ReportesOGV.Proceso.Aplicaciones.OGVEXPA import OGVEXPA
# Create your views here.
def index(request):
    return render(request,'ReportesOGV/index.html')

def consult_data(request):
    Comite = request.GET.get('Comite', None)
    objOGVEXPA=OGVEXPA()
    lstStatus = {}
    lstSegumiento = {}
    lstEpMeeting = {}
    lstUniversity = {}
    lstConversion={"Open": 0, "Approved": 0}
    lstDatos = objOGVEXPA.ConsultarDatos(Comite)
    lstStatus, lstSegumiento, lstEpMeeting, lstUniversity,lstConversion = objOGVEXPA.ProcesarExpaWeb(lstDatos, lstStatus,
                                                                                       lstSegumiento, lstEpMeeting,
                                                                                       lstUniversity
                                                                                       ,lstConversion)
    jsonData= {"lstStatus": lstStatus
        ,"lstSegumiento": lstSegumiento
        ,"lstEpMeeting": lstEpMeeting
        ,"lstUniversity": lstUniversity
        ,"lstConversion": lstConversion}
    return HttpResponse(json.dumps(jsonData), content_type  =  "application/json")

def ConsultarComites(request):
    lstComites=[{'Comite': "ANDES", 'ValorPodio': 1},
     {'Comite': "APC", 'ValorPodio': 2},
     {'Comite': "Armenia", 'ValorPodio': 3},
     {'Comite': "Bogota", 'ValorPodio': 4},
     {'Comite': "BUCARAMANGA", 'ValorPodio': 5},
     {'Comite': "CALI", 'ValorPodio': 6},
     {'Comite': "CARTAGENA", 'ValorPodio': 7},
     {'Comite': "CENTRAL", 'ValorPodio': 8},
     {'Comite': "CUCUTA", 'ValorPodio': 9},
     {'Comite': "EAFIT", 'ValorPodio': 10},
     {'Comite': "EAN", 'ValorPodio': 11},
     {'Comite': "ECI", 'ValorPodio': 12},
     {'Comite': "EXTERNADO", 'ValorPodio': 13},
     {'Comite': "FLORENCIA", 'ValorPodio': 14},
     {'Comite': "JAVERIANA", 'ValorPodio': 15},
     {'Comite' :"JAVERIANA CALI", 'ValorPodio': 16},
    {'Comite': "MANIZALES", 'ValorPodio': 17},
    {'Comite' :"MC CO", 'ValorPodio': 18},
    {'Comite': "MONTERIA", 'ValorPodio': 19},
    {'Comite': "NEIVA", 'ValorPodio': 20},
    {'Comite': "PASTO", 'ValorPodio': 21},
    {'Comite': "PEREIRA", 'ValorPodio': 22},
    {'Comite': "Popayan", 'ValorPodio': 23},
    {'Comite': "Riohacha", 'ValorPodio': 24},
    {'Comite': "ROSARIO", 'ValorPodio': 25},
    {'Comite' :"SAN GIL", 'ValorPodio': 26},
    {'Comite' :"Santa Marta", 'ValorPodio': 27},
    {'Comite': "SINCELEJO", 'ValorPodio': 28},
    {'Comite': "TOLIMA", 'ValorPodio': 29},
    {'Comite': "TULUA", 'ValorPodio': 30},
    {'Comite': "TUNJA", 'ValorPodio': 31},
    {'Comite': "UdeA", 'ValorPodio': 32},
    {'Comite': "UNIATLANTICO", 'ValorPodio': 33},
    {'Comite': "UNINORTE", 'ValorPodio': 34},
    {'Comite': "UPB", 'ValorPodio': 35},
    {'Comite': "VALLEDUPAR", 'ValorPodio': 36},
    {'Comite': "Villavicencio", 'ValorPodio': 3}]

    return HttpResponse(json.dumps(lstComites), content_type="application/json")
