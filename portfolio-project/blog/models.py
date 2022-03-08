from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    content = models.TextField()
    image = models.ImageField(upload_to='images/')

    def content_part(self):
        return self.content[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %Y %d')

    def __str__(self):
        return self.title
