from django.db import models

# Create your models here.
class JobOffer(models.Model):
    company_name = models.CharField(max_length=100)
    company_email = models.EmailField(max_length=100)
    job_title = models.CharField(max_length=100)
    job_description = models.TextField()
    salary = models.DecimalField(max_digits=20, decimal_places=2)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{ self.company_name } - { self.job_title }"
