from django.db import models

# Create your models here.
class ActiveObjectsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(state=True)


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    state = models.BooleanField('Estado', default=True)
    created_date = models.DateField('Fecha creacion', auto_now_add=True)
    modified_date = models.DateField('fecha modificada', auto_now=True)
    deleted_date = models.DateField('Fecha de Eliminación', auto_now=True)
    
    # Acá se lo asignás
    objects = ActiveObjectsManager()
    
    class Meta:
        abstract = True