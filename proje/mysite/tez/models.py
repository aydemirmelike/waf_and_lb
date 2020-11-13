from django.db import models

class yukDengeleyici(models.Model):
    ip = models.CharField(max_length=100)
    port = models.CharField(max_length=100)
    svr1 = models.CharField(max_length=100)
    svr2 = models.CharField(max_length=100)
    algoritma = models.CharField(max_length=100)

    def __str__(self):
        return self.ip

class guvenlikDuvari(models.Model):
    isim = models.CharField(max_length=100)
    xss = models.BooleanField(default=False)
    sql = models.BooleanField(default=False)
    traversal = models.BooleanField(default=False)

    def __str__(self):
        return self.isim