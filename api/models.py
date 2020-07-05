from django.db import models


class Banks(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Branches(models.Model):
    bank_id = models.ForeignKey(Banks, related_name='bank_data', on_delete=models.CASCADE, )
    ifsc = models.CharField(max_length=255, primary_key=True)
    branch = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    state = models.CharField(max_length=255)

    def __str__(self):
        return str(self.bank_id_id)
