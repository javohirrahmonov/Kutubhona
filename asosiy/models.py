from django.db import models

class Talaba(models.Model):
    ism = models.CharField(max_length=40)
    kitob_soni = models.PositiveSmallIntegerField()
    kurs = models.SmallIntegerField(default=3)
    def __str__(self):
        return self.ism

class Muallif(models.Model):
    tanlov = [("Erkak","Erkak"),("Ayol","Ayol")]
    ism = models.CharField(max_length=40)
    kitoblar_soni = models.PositiveSmallIntegerField()
    jins = models.CharField(choices=tanlov, max_length=10)
    tugilgan_yil = models.DateField()
    trik=models.BooleanField(default=True)
    def __str__(self):
        return self.ism

class Kitob(models.Model):
    tanlov = [("Badiiy","Badiiy"),("Ilmiy","Ilmiy"),("Detektiv","Detektiv")
              ,("Asar","Asar"),("Roman","Roman"),("Adabiiy","Adabiiy")]
    nom = models.CharField(max_length=45)
    muallif = models.ForeignKey(Muallif,on_delete=models.CASCADE)
    sahifa = models.PositiveSmallIntegerField()
    janr = models.CharField(choices=tanlov,max_length=50,verbose_name="Boshqalarini kiritishingiz mumkun")
    def __str__(self):
        return self.nom

class Admin(models.Model):
    ism = models.CharField(max_length=55)
    ish_vaqti = models.CharField(max_length=40,verbose_name="Boshlanish va tugash vaqtlari")

class Record(models.Model):
    talaba = models.ForeignKey(Talaba,on_delete=models.CASCADE)
    kitob = models.ForeignKey(Kitob,on_delete=models.CASCADE)
    admin = models.ForeignKey(Admin,on_delete=models.CASCADE)
    olingan_sana =models.DateField()
    qaytarish_sanasi = models.DateField()
    qaytardi = models.BooleanField(default=False)

