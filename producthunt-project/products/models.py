from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    content = models.TextField()
    url = models.URLField()
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    votes_total = models.IntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %d %Y')

    def summary(self):
        return self.content[:100]

    def __str__(self):
        return self.title
