from django.conf.urls import url
from ReportesOGT.views import index,consult_data


urlpatterns = [
    url(r'^$', index),
    url(r'^/data$', consult_data),

]
