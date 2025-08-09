from django.db import models

class Announcement(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.title
