from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    detalle = models.CharField(max_length=800,null=True, blank=True)
    
    def __str__(self) -> str:   
        return self.nombre
    
    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
    
class Estudiante(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    nacimiento = models.DateField(null=True, blank=True)
    
    
    def __str__(self) -> str:
        return f"{self.nombre},{self.apellido},{self.nacimiento}"
    
    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"
        
        
class Profesor(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return f"{self.nombre},{self.apellido}"
    
    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"
        
