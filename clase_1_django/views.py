from datetime import datetime as dt
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader

def Saludo(request):
    return HttpResponse("Hola mundo!, Hola coder! Buenas noches Lucas")

def Lucas(request):
    texto = "Hola soy Lucas<br>EL creador"
    return HttpResponse(texto)

def Fecha(request, dia_personalizado):
    dia = dt.now()
    dia=dia.strftime("%Y/%m/%d")
    dia= dia[:-2] + dia_personalizado
    texto=f'Hoy es:<br>{dia}'
    return HttpResponse(texto)

def Probando_template(request):
    nombre= "Lola"
    apellido= "Robredo"
    diccionario={"nombre":nombre, "apellido":apellido, "notas":[4, 8, 9, 10, 7, 8]}
    
    #Abrimos el archivo Html
    #mi_html = open('./clase_1_django/plantillas/index.html')
    
    #Creamos el template haciendo uso de la clase Template
    #plantilla = Template(mi_html.read())
    
    #Cerramos el archivo que creamos previamente, ya que lo tenemos cargado en la variable plantilla
    #mi_html.close()
    
    #Creamos un contexto con los datos del diccionario
    #mi_contexto = Context(diccionario)
    
    #Terminamos de construir el template renderizando con nuestra plantilla
    #documento= plantilla.render(mi_contexto)

#Con estas lineas me ahorro todos los pasos de la funcion anterior
    plantilla=loader.get_template("index.html")
    documento=plantilla.render(diccionario)
    return HttpResponse(documento)