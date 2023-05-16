from django.db import models        #para importar do Django os models --> mapeia para uma unica tabela o banco de dados

class Faixas(models.Model):       #É especificado, usando a classe, diversos atributos,como o titulo da música e sua descrição, que irão virar (cada um) uma coluna no banco de dados.
  title = models.CharField(max_length = 70)
  description = models.TextField()
  due_date=models.DateField()
  done=models.BooleanField(default=False)
  
class NarrativasDesenvolvidas(models.Model):     #É especificado, usando a classe, diversos atributos, como o titulo das narrativas desenvolvidas e sua descrição, que irão virar (cada um) uma coluna no banco de dados.
  title = models.CharField(max_length = 70)
  description = models.TextField()
  due_date=models.DateField()
  done=models.BooleanField(default=False)
