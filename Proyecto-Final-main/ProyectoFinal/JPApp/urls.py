from django.urls import path
from JPApp.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', Home, name = "Inicio"),
    path("login/", Iniciar_sesion, name="Login"),
    path("registro/", Registro_usuarios, name="RegistroUsuario"),

    #CRUD 
    path("RegistroError/", RegistroErrores.as_view(), name = "BugsForm"),
    path("RegistroInvestigacion/",RegistroInvestigaciones.as_view(), name = "InvestigationForm"),
    path("RegistroRefuerzo/", RegistroRefuerzos.as_view(), name = "RefuerzosForm"),
    path("ListadoDeInvestigaciones/", ListaInvestigaciones.as_view(), name = "ListaInvestigacion"),
    path("ListadoDeErrores/", ListaBugs.as_view(), name = "ListaErrores"),
    path("ListadoDeRefuerzos/", ListaRefuerzos.as_view(), name = "ListaRefuerzos"),
    path("logout/", LogoutView.as_view(template_name="JPApp/logout.html"), name="Logout"),
]