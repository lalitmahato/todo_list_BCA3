from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(null=True, max_length=200)
    email = models.EmailField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_datetime = models.DateTimeField(auto_now_add=True, null=True)
    completion_status = models.BooleanField(null=True, blank=True, default=False)

    def __str__(self):
        return self.title
