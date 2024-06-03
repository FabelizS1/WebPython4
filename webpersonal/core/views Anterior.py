from django.shortcuts import render, HttpResponse

html_base= """
<h1>Mi web Personal</h1>
<ul>
    <li><a href="/">Portada</a></li>
    <li><a href="/about-me">Acerca de</a></li>
    <li><a href="/portfolio">Portafolio</a></li>
    <li><a href="/contact">Contacto</a></li>
</ul>
"""

# Create your views here.
def home(request):
    #html_response = "<h1>Mi web Personal</h1>"
    #for i in range(10):
    #    html_response += "<h2>Portada</h2>"
    #return HttpResponse(html_response)
    return HttpResponse(html_base + """
                        <h2>Portada</h2>
                        <p>Esto es la portada</p>
                        """)


def about(request):
   return HttpResponse(html_base + """
                       <h2>Acerca de</h2>
                       <p>Me llamo Fabeliz y soy programador</p>
                       """) 


def portfolio(request):
    return HttpResponse(
        html_base + """
                       <h2>Portafolio</h2>
                       <p>Algunos de mis trabajos</p>
                       """
    )



def contact(request):
    return HttpResponse(
              html_base + """
                       <h2>Contacto</h2>
                       <p>Aqui les dejo mi numero para preguntarme dudas al 0424-281.60.63</p>
                       """  
    )