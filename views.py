from django.shortcuts import render,redirect
from .models import Faixas 
from .models import NarrativasDesenvolvidas


def home(request):
  faixas= Faixas.objects.all()
  narrativas= NarrativasDesenvolvidas.objects.all()
  context={'faixas':faixas, 'narrativas':narrativas}
  return render(request,'home.html', context=context)

def create_faixas(request):
  # Se o usuário submeter o formulário, ele cai no if abaixo
  if request.method == "POST":
    print(request.POST)
    Faixas.objects.create(
      title=request.POST["title"],
      description=request.POST["description"],
      due_date=request.POST["due-date"],
      done=False
    )
    return redirect("principal")
  
  return render(request, "faixas_form.html")

def update_faixas(request,faixa_id):
  faixa=Faixas.objects.get(id=faixa_id)
  faixa.due_date=faixa.due_date.strftime('%Y-%m-%d') 
  if request.method == "POST":
    faixa.title=request.POST["title"]
    faixa.description=request.POST["description"]
    faixa.due_date=request.POST["due-date"]
    if "done" not in request.POST:
      faixa.done= False
    else: 
      faixa.done=True
    faixa.save()
    return redirect("principal")
  return render(request, "faixas_form.html", context={"faixa": faixa})

def delete_faixas(request,faixa_id):
  faixa=Faixas.objects.get(id=faixa_id)
  if request.method == "POST":
    if "confirm" in request.POST:
      faixa.delete()
    return redirect("principal") 
  return render(request, "delete_faixas_form.html", context={"faixa": faixa})

def create_narrativas(request):
  # Se o usuário submeter o formulário, ele cai no if abaixo
  if request.method == "POST":
    print(request.POST)
    NarrativasDesenvolvidas.objects.create(
      title=request.POST["title"],
      description=request.POST["description"],
      due_date=request.POST["due-date"],
      done=False
    )
    return redirect("principal")
  
  return render(request, "narrativas_form.html")

def update_narrativas(request,narrativa_id):
  narrativa=NarrativasDesenvolvidas.objects.get(id=narrativa_id)
  narrativa.due_date=narrativa.due_date.strftime('%Y-%m-%d')
  if request.method == "POST":
    narrativa.title=request.POST["title"]
    narrativa.description=request.POST["description"]
    narrativa.due_date=request.POST["due-date"]
    if "done" not in request.POST:
      narrativa.done= False
    else: 
      narrativa.done=True
    narrativa.save()
    return redirect("principal")
  return render(request, "narrativas_form.html", context={"narrativa": narrativa})

def delete_narrativa(request,narrativa_id):
  narrativa=NarrativasDesenvolvidas.objects.get(id=narrativa_id)
  if request.method == "POST":
    if "confirm" in request.POST:
      narrativa.delete()
    return redirect("principal") 
  return render(request, "delete_narrativas_form.html", context={"narrativa": narrativa})
