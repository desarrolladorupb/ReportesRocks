from django.conf.urls import url
from ReportesOGE.views import index,consult_data


urlpatterns = [
    url(r'^$', index),
    url(r'^/data$', consult_data),


]
