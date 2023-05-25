from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=100)
    
    MEDIA_CHOICES = (
        ('Low','Low'),    
        ('Medium','Medium'),    
        ('High','High'),    
    )
    
    priority = models.CharField(
        max_length=10,
        choices=MEDIA_CHOICES,
        default='Low',
    )
    
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}.{}".format(self.id, self.title)
