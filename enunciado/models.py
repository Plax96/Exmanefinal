from django.db import models

class Grado(models.Model):
    nombre = models.CharField(max_length=50)
    seccion= models.CharField(max_length=2)
    def __str__(self):
        return self.nombre

class Alumno(models.Model):
    nombre = models.CharField(max_length=50)
    apellido =models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido =models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Materia(models.Model):
    nombre = models.CharField(max_length=30,blank=True, null=True)
    estado = models.CharField(max_length=2,default="1")
    alumno = models.ForeignKey(Alumno, on_delete = models.CASCADE, blank=True, null=True)
    profesor = models.ForeignKey(Profesor, on_delete = models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.nombre

class Nota(models.Model):
    nombre = models.CharField(max_length=30,blank=True, null=True)
    punteo = models.IntegerField(null=True)
    materia = models.ForeignKey(Materia, on_delete = models.CASCADE,blank=True, null=True)
    alumno = models.ForeignKey(Alumno, on_delete = models.CASCADE,blank=True, null=True)
    def __str__(self):
        return self.nombre

class Gestion_grado(models.Model):
    grado = models.ForeignKey(Grado, on_delete = models.CASCADE, blank=True, null=True)
    materia = models.ForeignKey(Materia, on_delete = models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.grado.nombre




# Create your models here.
