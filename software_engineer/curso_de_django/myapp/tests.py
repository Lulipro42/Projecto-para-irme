from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Task,Project
from .services import TaskService

User = get_user_model()

class TaskServiceTestCase(TestCase):
    
    def setUp(self):
        """Preparamos el entorno de prueba con datos ficticios"""
        # 1. Creamos un usuario de prueba
        self.user = User.objects.create_user(username="ulises_dev", password="password123")
    
        # 2. !Creo el proytecto obligatiorio que pide mi ForeingKey!
        self.proyecto = Project.objects.create(name="Proyecto para irme con Kaori", user=self.user)
    
        #3. Creamos una tarea inicial asignada a ese usuario
        self.tarea = Task.objects.create(
            user=self.user,
            project=self.proyecto,
            title="Aprender testing",
            description="Nota vieja",
        )

    def test_update_user_task_limpia_notas_null(self):
        """Verifica que el servicio acutalize los datos y limpie el string 'null'"""
        
        # Datos que simulan venir del frontend con el string 'null' tramposo
        datos_frontend = {
            "project": self.proyecto.id,
            "title":"Aprender Testing de Verdad",
            "description":"null"
        }
        
        # Ejecutamos TU SERVICIO
        resultado = TaskService.update_user_task(
            task_id=self.tarea.id,
            user=self.user,
            data=datos_frontend
        )
        
        # --- LAS ASERCIONES (Comprobaciones) ---
        # Si el serializer tira error, esto nos va a mostrar en la consola EXACTAMENTE qué campo falta
        self.assertTrue(
            resultado.get("success") or resultado.get("succes"), 
            msg=f"El servicio falló. Errores del serializer: {resultado.get('errors')}"
        )
        
        # 2. Refrescamos la tarea desde la base de datos de prueba para ver si impactó
        self.tarea.refresh_from_db()
        
        # 3. Comprobamos que el título cambió correctamente
        self.assertEqual(self.tarea.title, "Aprender Testing de Verdad")
        
        # 4. LA PRUEBA REINA: Comprobamos que el 'null' se convirtió en un string vacío ""
        self.assertEqual(self.tarea.description, "")