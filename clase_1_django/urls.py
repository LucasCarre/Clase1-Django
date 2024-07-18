"""URL configuration for clase_1_django project."""
from django.contrib import admin
from django.urls import path
from clase_1_django.views import Saludo, Lucas, Fecha, Probando_template
from AppCoder.views import curso


urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', Saludo),
    path('lucas/',Lucas),
    path('dia/<dia_personalizado>',Fecha),
    path('probando_template/',Probando_template),
    path('curso/<nombre>/<numero>/',curso),
]
