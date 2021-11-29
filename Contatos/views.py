from django.shortcuts import get_object_or_404, render
from django.views.generic.base import View

from Contatos.models import Psicologo
from Contatos.forms import ContatoModel2Form
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy

# Create your views here.

#Lista todos psicologos

class PsicologoListView(View):
    def get(self,request,*args,**kwargs):
        # buscar todos profissionais no banco de dados
        psicologos = Psicologo.objects.all()
        #enviar ele para o template
        context = {'psicologos':psicologos,}
        return render(request,'contatos/listaPsi.html', context)

# Inclui novo cadastro
class PsicologoCreateView(View):
    def get(self,request,*args,**kwargs):
        context={'formulario': ContatoModel2Form,}
        return render(request, "contatos/criaCadastro.html",context)

    def post(self,request,*args,**kwargs):
        formulario = ContatoModel2Form(request.POST);
        if formulario.is_valid():
            contato = formulario.save()
            contato.save()
            return HttpResponseRedirect(reverse_lazy('contatos:lista-psicologos'))
        pass

class PsicologoUpdateView(View):
    def get(self,request,pk,*args,**kwargs):
        psicologo = Psicologo.objects.get(pk=pk)
        formulario = ContatoModel2Form(instance=psicologo)
        context = {'formulario': formulario,}
        return render(request,'contatos/atualizaCadastro.html', context)
    def post(self,request,pk,*args,**kwargs):
        psicologo = get_object_or_404(Psicologo, pk=pk)
        formulario = ContatoModel2Form(request.POST, instance=psicologo)
        if formulario.is_valid():
            contato = formulario.save()
            contato.save()
            return HttpResponseRedirect(reverse_lazy('contatos:lista-psicologos'))
        else:
            context = {'formulario': formulario,}
            return render(request,'contatos/atualizaCadastro.html', context)
        
    
class PsicologoDeleteView(View):
    def get(self,request,pk,*args,**kwargs):
        psicologo = Psicologo.objects.get(pk=pk)
        context= {'psicologo': psicologo, }
        return render(request,'contatos/apagaCadastro.html', context)
        pass
    def post(self,request,pk,*args,**kwargs):
        psicologo = Psicologo.objects.get(pk=pk)
        psicologo.delete()
        return HttpResponseRedirect(reverse_lazy('contatos:lista-psicologos'))
    