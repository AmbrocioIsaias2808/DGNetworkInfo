from django.db import models

# Create your models here.
class info_chart(models.Model):
    concept_number=models.IntegerField(default=0)
    concepto=models.CharField(max_length=200)
    sig_en=models.CharField(max_length=200)
    sig_es=models.CharField(max_length=200)
    capa=models.CharField(max_length=200, default="NA")
    puerto=models.CharField(max_length=200, default="NA")
    description= models.TextField()

    def alta(self):
        self.save()

    def __str__(self):
        return  self.concepto
