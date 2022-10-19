from distutils.command.build_scripts import first_line_re
from pyexpat import model
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from JPApp.models import *
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.urls import is_valid_path, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

def Home(request):
    return render(request, 'JPApp/inicio.html')


def Iniciar_sesion(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():

            usuario = form.cleaned_data.get("username")
            clave = form.cleaned_data.get("password")

            user = authenticate(username=usuario, password=clave)
        
            if user:

                login(request, user)

                return render(request, "JPApp/inicio.html", {"mensaje" : f'"Hola {user}!"'})
            
            else:

                return render(request, "JPApp/inicio/.html", {"mensaje": f'Datos incorrectos. Intenta de nuevo.'})
    
    else:

        form = AuthenticationForm()
    
    return render(request, "JPApp/login.html", {"form1":form})


def Registro_usuarios(request):

    if request.method == "POST":

        formu = UserCreationForm(request.POST)

        if formu.is_valid():

            NombreUsuario = formu.cleaned_data["username"]

            formu.save()

            return render(request, "JPApp/inicio.html", {"mensaje" : f'" Usuario {NombreUsuario} creado. "'})
    else:
        
        formu = UserCreationForm()

    return render(request, "JPApp/registrousuario.html", {"form2": formu})



class RegistroInvestigaciones(LoginRequiredMixin, CreateView):

    model = investigations
    template_name = "JPApp/Registroinvestigacion.html"
    success_url = "/JPApp/RegistroInvestigacion"
    fields = ['domain_name', 'investigation_owner', 'investigation_name','investigation_date','investigation_overview','investigation_media', 'investigation_link']



class RegistroErrores(LoginRequiredMixin, CreateView):

    model = bugs
    template_name = "JPApp/Registroerror.html"
    success_url = "/JPApp/RegistroError"
    fields = ['bugs_domain', 'bugs_date', 'bugs_owner', 'bugs_name', 'bugs_description', 'bugs_blocking', 'bugs_media', 'bugs_image']



class RegistroRefuerzos(LoginRequiredMixin, CreateView):

    model = tips
    template_name = "JPApp/Registrorefuerzo.html"
    success_url = "/JPApp/RegistroRefuerzo"
    fields = ['tips_owner', 'tips_name', 'tips_description', 'tips_date', 'tips_email', 'tips_media', 'tips_link']


class ListaInvestigaciones(ListView):
    model = investigations
    template_name = "JPApp/Investigaciones.html"


class ListaBugs(ListView):
    model = bugs
    template_name = "JPApp/Errores.html"


class ListaRefuerzos(ListView):
    model = tips
    template_name = "JPApp/Refuerzos.html"