from django import forms

from . import models

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = models.Estudiante
        fields = ["nombre","apellido","nacimiento"]
        
class ProfesorForm(forms.ModelForm):
    class Meta:
        model = models.Profesor
        fields = ["nombre","apellido"]