from django.urls import path
from api_rest.views import listado_Lineup,addLineUp,controlarLineUp
from api_rest.viewsLogin import login

urlpatterns = [
    path('listado_Lineup/',listado_Lineup,name="listado_Lineup"),
    path('addLineUp/',addLineUp,name="addLineUp"),
    path('controlarLineUp/<codigo>',controlarLineUp,name="controlarLineUp"),
    path('login/',login,name="login"),
]