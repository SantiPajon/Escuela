from django import forms

from . import models

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = models.Estudiante
        fields = ["nombre","apellido","nacimiento","materia"]
        
class ProfesorForm(forms.ModelForm):
    class Meta:
        model = models.Profesor
        fields = ["nombre","apellido","materia"]
        
class CursoForm(forms.ModelForm):
    class Meta:
        model = models.Curso
        fields = ["nombre","detalle"]
        widgets = {
            'detalle': forms.Textarea(attrs={'rows': 10, 'cols': 60}),  # Ajusta rows y cols según sea necesario
        }