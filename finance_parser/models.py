from django.db import models


class Symbol(models.Model):
    name = models.CharField(max_length=200)
    symbol = models.CharField(max_length=100)
    IPOYear = models.CharField(max_length=200)
    sector = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    summary_quote = models.URLField(max_length=500)

    def __str__(self):
        return self.name

