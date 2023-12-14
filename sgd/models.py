from django.db import models
from django.contrib.auth.models import User

class Correspondence(models.Model):
    title = models.CharField('Titulo',max_length=100)
    cod = models.CharField('Codigo', max_length=50, null=False, blank=False)
    
    content = models.TextField('Descripción', max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_correspondence')
    tracked_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tracked_correspondence', null=True, blank=True)
    tracked_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Agregar campo para el estado de la correspondencia
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
        ('ON_HOLD', 'On Hold'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')

    def __str__(self):
        return self.subject

class Comment(models.Model):    
    correspondence = models.ForeignKey(Correspondence, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.correspondence.subject}"




class CorrespondenceAssignment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    correspondence = models.ForeignKey(Correspondence, on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True)

    # Otros campos si es necesario

    def __str__(self):
        return f"{self.user.username} - {self.correspondence.subject}"


