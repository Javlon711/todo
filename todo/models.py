from django.db import models
class Task(models.Model):
    MUHIMLIK_CHOICES = [
        ('Yuqori', 'Yuqori'),
        ('O\'rta', 'O\'rta'),
        ('Past', 'Past'),
    ]

    HOLAT_CHOICES = [
        ('Bajarilmoqda', 'Bajarilmoqda'),
        ('Rejalashtirilgan', 'Rejalashtirilgan'),
        ('Boshlanmagan', 'Boshlanmagan'),
    ]

    nomi = models.CharField(max_length=100)
    tavsif = models.TextField()
    muhimlik = models.CharField(max_length=10, choices=MUHIMLIK_CHOICES)
    muddat = models.DateField()
    holat = models.CharField(max_length=20, choices=HOLAT_CHOICES, default='Boshlanmagan')

    def __str__(self):
        return self.nomi
