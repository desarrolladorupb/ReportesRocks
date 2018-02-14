# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from ReportesOGE.Proceso.Aplicaciones.OGEEXPA import  OGEEXPA
from django.http import HttpResponse
import json
# Create your views here.

def index(request):
    return render(request,'ReportesOGE/index.html')

def consult_data(request):
    Comite = request.GET.get('Comite', None)
    objOGEEXPA=OGEEXPA()
    lstDatos={}
    lstStatus={}
    lstTrackLc={}
    lstUniversity={}
    lstConversion={"Open": 0, "Approved": 0}
    lstDatos=objOGEEXPA.ConsultarDatos(Comite)

    lstStatus, lstTrackLc, lstUniversity, lstConversion=objOGEEXPA.ProcesarExpaWeb(lstDatos,
                                                                                   lstStatus,
                                                                                   lstTrackLc,
                                                                                   lstUniversity,
                                                                                   lstConversion)
    jsonData = {
        "lstStatus": lstStatus
        , "lstTrackLc": lstTrackLc
        , "lstUniversity": lstUniversity
        , "lstConversion": lstConversion
    }
    return HttpResponse(json.dumps(jsonData), content_type="application/json")