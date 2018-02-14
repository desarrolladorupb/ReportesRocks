# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from Librerias.pypodio2 import api
from Constantes.AplicacionesPodio import AplicacionesPodio
from Constantes.ExtraerInformacionPodio import ExtraerInformacionPodio
from Constantes.UsuarioPodio import UsuarioPodio

class OGTEXPA:
    IdOGT = None
    CodigoOGT = None
    objExtraerInformacionPodio = ExtraerInformacionPodio()

    def __init__(self):
        objAplicacionesPodio = AplicacionesPodio()
        self.IdOGT=objAplicacionesPodio.IdOGTEXPAWEB
        self.CodigoOGT=objAplicacionesPodio.CodigoOGTEXPAWEB

    def ConsultarDatos(self,Comite):
        intOffSet=0
        objUsuarioPodio=UsuarioPodio()
        ApiOgvManager= api.OAuthClient(objUsuarioPodio.api_key
                                       ,objUsuarioPodio.CodigoSecretoUsuario
                                       ,objUsuarioPodio.login
                                       ,objUsuarioPodio.password)
        intNumeroLista=500
        lstTotal=[]
        while intNumeroLista>=500:
            lstParcial=self.__ConsultarDatosOGT(ApiOgvManager,intOffSet,Comite)
            lstTotal=lstTotal+lstParcial
            intNumeroLista=len(lstParcial)
            intOffSet=intOffSet+500
        return lstTotal

    def ProcesarExpaWeb(self, lstDatos, lstStatus, lstTrackLc,  lstUniversity,lstConversion):
        for Dato in lstDatos:
            values = Dato["values"]
            #Lista de status
            if "status" in values.keys():
                if values["status"] in lstStatus.keys():
                    lstStatus[values["status"]]=lstStatus[values["status"]]+1
                else:
                    lstStatus[values["status"]]=1
            if "track-lc" in values.keys():
                if values["track-lc"] in lstTrackLc.keys():
                    lstTrackLc[values["track-lc"]]=lstTrackLc[values["track-lc"]]+1
                else:
                    lstTrackLc[values["track-lc"]]=1

            if "university" in values.keys() and "status" in values.keys():
                if values['status'] == 'Approved' or values['status'] == 'Realized':
                    if values["university"] in lstUniversity.keys():
                        lstUniversity[values["university"]]=lstUniversity[values["university"]]+1
                    else:
                        lstUniversity[values["university"]]=1
            if "status" in values.keys():
                if values['status'] == 'Approved' or values['status'] == 'Realized':
                    lstConversion["Approved"] = lstConversion["Approved"]+1
                lstConversion["Open"] = lstConversion["Open"]+1

        return lstStatus, lstTrackLc,  lstUniversity, lstConversion


    def __ConsultarDatosOGT(self,Api,intOffSet,Comite):
        params={
                    'limit': 500,
                    "offset":intOffSet,
                    'filters':[
                                {
                                    "key":"lc",
                                    "values":int(Comite)
                                }
                               ],
                }

        data=Api.Item.filter(
                int(self.IdOGT),params
            )["items"]
        fields=[self.objExtraerInformacionPodio.makeDict(item,nested=Api,no_html=False) for item in data]

        return fields