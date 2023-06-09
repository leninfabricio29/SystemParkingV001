from django.urls import path
from .views import registro_auto_espacio,home_view, registro_tarifa, registro_espacio, detalles_view, view_contable_home, registro_ingreso


urlpatterns = [
    path('registrar/', registro_auto_espacio, name="page-registrar"),
    path('', home_view, name="page-home"),

    path('nueva-tarifa/',registro_tarifa,name="page-nueva-tarifa"),
    path('nuevo-espacio/',registro_espacio,name="page-nuevo-espacio"),
    path('detalles/', detalles_view,name="page-detalles"),
    path('contable/',view_contable_home,name="page-contable"),
    path('nuevo-ingreso/', registro_ingreso,name='page-ingreso')

]
