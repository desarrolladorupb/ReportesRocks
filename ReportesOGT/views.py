# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.shortcuts import render
from ReportesOGT.Proceso.Aplicaciones.OGTEXPA import OGTEXPA
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'ReportesOGT/index.html')

def consult_data(request):
    Comite = request.GET.get('Comite', None)
    objOGTEXPA=OGTEXPA()
    lstDatos={}
    lstStatus={}
    lstTrackLc={}
    lstUniversity={}
    lstConversion={"Open": 0, "Approved": 0}
    lstDatos=objOGTEXPA.ConsultarDatos(Comite)

    lstStatus, lstTrackLc, lstUniversity, lstConversion=objOGTEXPA.ProcesarExpaWeb(lstDatos,
                                                                                   lstStatus,
                                                                                   lstTrackLc,
                                                                                   lstUniversity,
                                                                                   lstConversion)
    jsonData = {"lstStatus": lstStatus
        , "lstTrackLc": lstTrackLc
        , "lstUniversity": lstUniversity
        , "lstConversion": lstConversion}
    return HttpResponse(json.dumps(jsonData), content_type="application/json")

