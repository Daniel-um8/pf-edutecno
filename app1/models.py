from django.db import models

class ContactMessage(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)  # Fecha y hora de creación

    def __str__(self):
        return f"Mensaje de {self.nombre} - {self.email}"
