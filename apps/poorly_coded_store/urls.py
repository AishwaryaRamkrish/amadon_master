from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^checkout$', views.checkout),
    url(r'^process_order/(?P<prod_id>\d+)$',views.process_order)
]