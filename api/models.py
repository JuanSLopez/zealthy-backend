import uuid
from django.db import models


# Create your models here.
class Tickets(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=8)
    email = models.EmailField(max_length=254)
    description = models.TextField()
    status = models.CharField(max_length=254,default="new")
    
class Comment(models.Model):
    ticket = models.ForeignKey(Tickets, on_delete=models.CASCADE, related_name='comments')
    timestamp = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def __str__(self):
        return f"Comment by {self.ticket.name} on {self.timestamp}"