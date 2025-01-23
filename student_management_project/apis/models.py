from django.db import models
from django.contrib.auth.models import AbstractUser

class users(AbstractUser):
   department=models.CharField(max_length=100,blank=True,null=True)


class Task(models.Model):
   description = models.TextField()
   due_date = models.DateTimeField()
   status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed'), ('overdue', 'Overdue')], default='pending')
   student = models.ForeignKey(users, on_delete=models.CASCADE)
   def check_status(self):
         if self.due_date < datetime.now() and self.status != self.COMPLETED:
               self.status = self.OVERDUE
               self.save()
   def __str__(self):
      return f"Task: {self.description} - {self.status}"