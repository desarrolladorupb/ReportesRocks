import json

from ReportesOGT.Proceso.Aplicaciones.OGTEXPA import OGTEXPA

objOGTEXPA=OGTEXPA()

lstDatos = objOGTEXPA.ConsultarDatos(34)
lstDatos={}
lstStatus={}
lstTrackLc={}
lstUniversity={}
lstConversion={"Open": 0, "Approved": 0}
lstStatus, lstTrackLc,lstUniversity,lstConversion = objOGTEXPA.ProcesarExpaWeb(lstDatos,
                                                   lstStatus,
                                                   lstTrackLc,
                                                   lstUniversity,
                                                   lstConversion)
jsonData = {"lstStatus": lstStatus
    , "lstTrackLc": lstTrackLc
    , "lstUniversity": lstUniversity
    , "lstConversion": lstConversion}
print(json.dumps(jsonData))


