from django.contrib import admin  

# Register your modefrom django.contrib import admin
from .models import Faixas    # o modelo Faixas ( que possui titulo, descricao, etc) será importado
admin.site.register(Faixas) # será registrado no admin do site o "Faixas" para poder criar novas tasks

from .models import NarrativasDesenvolvidas  # o modelo NarrativasDesenvolvidas ( que possui titulo, descricao, etc) será importado
admin.site.register(NarrativasDesenvolvidas)# será registrado no admin do site o "NarrativasDesenvolvidas" para poder criar novas tasks
