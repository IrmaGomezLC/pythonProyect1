from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    edad = models.TextField()

class Receta(models.Model):
    titulo = models.CharField(max_length=50)
    ingredientes = models.TextField()
    preparacion = models.TextField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
    Autor = models.CharField(max_length=50)
    contenido = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return f"Comentario de {self.autor} en {self.receta.titulo}"


