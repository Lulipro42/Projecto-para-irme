from django import forms
from .models import Project, Task # IMPORTO MIS MODELOS

# Definimos una clase que hereda de ModelForm para crear tareas
class CreateNewTask(forms.ModelForm):
    # La clase Meta le dice a Django qué modelo usar y cómo configurar el formulario
    class Meta:
        model = Task  # Vincula este formulario con el modelo 'Task'
        fields = ['title', 'description','project', 'user', 'deadline', 'priority'] # Define qué campos del modelo aparecerán en el HTML
        
        # 'widgets' permite personalizar el HTML de cada campo (clases CSS, placeholders, etc.)
        widgets = {
            # Crea un <input type="text"> con clase CSS y un texto de ayuda
            'title': forms.TextInput(attrs={'class': 'input-estilo', 'placeholder': ' Titulo de tarea'}),
            # Crea un <textarea> para textos largos
            'description': forms.Textarea(attrs={'class': 'input-estilo', 'placeholder': 'Descripcion...'}),
            # Crea un <select> para elegir entre los proyectos existentes
            'project': forms.Select(attrs={'class': 'input-estilo'}),
            # Crea un <select> un usuario correcto 
            'user': forms.Select(attrs={'class': 'input-estilo'}),
            
            # 🆕 LE AGREGAMOS ESTO: El selector de calendario con tus estilos
            'deadline': forms.DateInput(attrs={
                'type':'data',
                'class':'input-estilo'
            }),
            
            'priority': forms.Select(attrs={
                'class':'input-estilo'
            })
            
        }

# Definimos una clase para crear proyectos nuevos
class CreateNewProject(forms.ModelForm):
    # Configuración del formulario de Proyecto
    class Meta:
        model = Project # Vincula con el modelo 'Project'
        fields = ['name'] # Solo necesitamos el campo 'name'
        
        # Personalización del diseño del campo 'name'
        widgets = {
            # Añade clase CSS para diseño y un placeholder
            'name' : forms.TextInput(attrs={'class': 'input-estilo', 'placeholder': 'Nombre del proyecto'})
        }
    