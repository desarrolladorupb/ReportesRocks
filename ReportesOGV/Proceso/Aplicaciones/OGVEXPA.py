from Librerias.pypodio2 import api
from Constantes.AplicacionesPodio import AplicacionesPodio
from Constantes.ExtraerInformacionPodio import ExtraerInformacionPodio
from Constantes.UsuarioPodio import UsuarioPodio

class OGVEXPA:
    IdOGVManagementOGVExpa = None
    CodigoOGVManagementOGVExpa = None
    IdOGVManagementEmbajadores = None
    CodigoOGVManagementEmbajadores = None
    objExtraerInformacionPodio=ExtraerInformacionPodio()

    def __init__(self):
        objAplicacionesPodio=AplicacionesPodio()
        self.IdOGVManagementOGVExpa=objAplicacionesPodio.IdOGVManagementOGVExpa
        self.CodigoOGVManagementOGVExpa=objAplicacionesPodio.CodigoOGVManagementOGVExpa
        self.IdOGVManagementEmbajadores=objAplicacionesPodio.IdOGVManagementEmbajadores
        self.CodigoOGVManagementEmbajadores=objAplicacionesPodio.CodigoOGVManagementEmbajadores

    def ConsultarDatos(self,CodigoComite):
        intOffSet=0
        objUsuarioPodio=UsuarioPodio()
        ApiOgvManager= api.OAuthClient(objUsuarioPodio.api_key
                                       ,objUsuarioPodio.CodigoSecretoUsuario
                                       ,objUsuarioPodio.login
                                       ,objUsuarioPodio.password)
        intNumeroLista=500
        lstTotal=[]
        while intNumeroLista>=500:
            lstParcial=self.__ConsultarDatosOGV(ApiOgvManager,intOffSet,CodigoComite)
            lstTotal=lstTotal+lstParcial
            intNumeroLista=len(lstParcial)
            intOffSet=intOffSet+500
        return lstTotal


    def ProcesarExpaWeb(self, lstDatos, lstStatus, lstSegumiento, lstEpMeeting, lstUniversity,lstConversion):

        lstComitesDatos={}
        for Dato in lstDatos:
            values = Dato["values"]
            Repetido=False
            #Lista de status



            if "seguimiento" in values.keys():
                 if values["seguimiento"]=="Repetido":
                     Repetido=True
            if not Repetido:
                if "status" in values.keys():
                    if values["status"] in lstStatus.keys():
                        lstStatus[values["status"]]=lstStatus[values["status"]]+1
                    else:
                        lstStatus[values["status"]]=1
                if "seguimiento" in values.keys():
                    if values["seguimiento"] in lstSegumiento.keys():
                        lstSegumiento[values["seguimiento"]]=lstSegumiento[values["seguimiento"]]+1
                    else:
                        lstSegumiento[values["seguimiento"]]=1
                if "ep-meeting" in values.keys() :
                    if values["ep-meeting"] in lstEpMeeting.keys():
                        lstEpMeeting[values["ep-meeting"]]=lstEpMeeting[values["ep-meeting"]]+1
                    else:
                        lstEpMeeting[values["ep-meeting"]] =1
                if "university" in values.keys():
                    if values['status'] == 'Approved' or values['status'] == 'Realized':
                        if values["university"] in lstUniversity.keys():
                            lstUniversity[values["university"]]=lstUniversity[values["university"]]+1
                        else:
                            lstUniversity[values["university"]]=1
                if values['status'] == 'Approved' or values['status'] == 'Realized':
                    lstConversion["Approved"] = lstConversion["Approved"]+1
                lstConversion["Open"] = lstConversion["Open"]+1

        return lstStatus, lstSegumiento, lstEpMeeting, lstUniversity, lstConversion





    def __ConsultarDatosOGV(self,Api,intOffSet,CodigoComite):
        params={
                    'limit': 500,
                    "offset":intOffSet,
                    'filters':[
                                {
                                    "key":"lc",
                                    "values":int(CodigoComite)
                                }
                               ],
                }

        data=Api.Item.filter(
                int(self.IdOGVManagementOGVExpa),params
            )["items"]
        fields=[self.objExtraerInformacionPodio.makeDict(item,nested=Api) for item in data]

        return fields





