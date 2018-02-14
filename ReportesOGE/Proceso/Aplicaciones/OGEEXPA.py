from Constantes.ExtraerInformacionPodio import ExtraerInformacionPodio
from Librerias.pypodio2 import api
from Constantes.AplicacionesPodio import AplicacionesPodio
from Constantes.UsuarioPodio import UsuarioPodio

class OGEEXPA:
    IdOGE = None
    CodigoOGE = None
    objExtraerInformacionPodio = ExtraerInformacionPodio()
    def __init__(self):
        objAplicacionesPodio = AplicacionesPodio()
        self.IdOGE=objAplicacionesPodio.IdOGEEXPAWEB
        self.CodigoOGE=objAplicacionesPodio.CodigoOGEEXPAWEB

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
            if "status-interesado" in values.keys():
                if values["status-interesado"] in lstTrackLc.keys():
                    lstTrackLc[values["status-interesado"]]=lstTrackLc[values["status-interesado"]]+1
                else:
                    lstTrackLc[values["status-interesado"]]=1

            if "university" in values.keys():
                if "status" in values.keys():
                    if values['status'] == 'Approved' or values['status'] == 'Realized':
                        if values["university"] in lstUniversity.keys():
                            lstUniversity[str(values["university"])]=lstUniversity[str(values["university"])]+1
                        else:
                            lstUniversity[str(values["university"])]=1
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
                int(self.IdOGE),params
            )["items"]
        fields=[self.objExtraerInformacionPodio.makeDict(item,nested=Api,no_html=True) for item in data]

        return fields
