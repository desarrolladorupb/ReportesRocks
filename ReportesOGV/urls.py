from django.conf.urls import url
from ReportesOGV.views import index,consult_data,ConsultarComites


urlpatterns = [
    url(r'^$', index),
    url(r'^/data$',consult_data),
    url(r'^/comites',ConsultarComites)
]
