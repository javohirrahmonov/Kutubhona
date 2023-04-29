from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

def salomlash(request):
    return HttpResponse("<h1>Salom, Dunyo!</h1>")

def bosh_sahifa(request):
    return render(request, 'home.html')

def salom(request):
    content = {
        "kitoblar":["Ufq","Qo'rqma","O'tkan kunlar","Odamiylik mulki"],
        "ism":"Javohir"
    }
    return render(request,'mashquchun.html', content)

def talabalar(request):
    soz = request.GET.get('qidiruv')
    if soz == "" or soz is  None:
        content = {
            "students": Talaba.objects.all()
        }
    else:
        content = {
            "students": Talaba.objects.filter(ism__icontains=soz)
        }

    return render(request,'talabalar.html',content)

def bitiruvchilar(request):
    content={
        "students": Talaba.objects.filter(kurs=4)
    }
    return render(request,'bitiruvchilar.html',content)

def kitobbor(request):
    content={
        "students": Talaba.objects.filter(kitob_soni__gt=0)
    }
    return render(request,'kitobibor.html',content)

def bitta_talaba(request,son):
    content={
        "talaba":Talaba.objects.get(id=son)
    }

    return render(request,'bitta_talaba.html',content)

def talaba_a(request):
    content={
        "students": Talaba.objects.filter(ism__icontains='a')
    }
    return render(request,'a_li.html',content)

def record(request,son):
    content={
        "record":Record.objects.get(id=son)
    }

    return render(request,'bitta_record.html',content)

def mualliflar(request):
    content = {
        "mualliflar": Muallif.objects.all()
    }
    return render(request,'mualliflar.html',content)

def muallif(request,son):
    content={
        "muallif":Muallif.objects.get(id=son)
    }

    return render(request,'bitta_muallif.html',content)

def kitoblar(request):
    soz = request.GET.get('qidiruv')
    if soz == "" or soz is None :
        content = {
            "kitoblar": Kitob.objects.all()
        }
    else:
        content = {
            "kitoblar": Kitob.objects.filter(nom__icontains=soz)
        }
    return render(request,'kitoblar.html',content)

def bitta_kitob(request,son):
    content={
        "kitob": Kitob.objects.get(id=son)
    }

    return render(request,'bitta_kitob.html',content)

def recordlar(request):
    content = {
        "record": Record.objects.all()
    }
    return render(request,'recordlar.html',content)

def tirik_muallif(request):
    content={
        "muallif": Muallif.objects.filter(trik= True)
    }
    return render(request,'tiriklar.html',content)

def sahifa_gt(request):
    content={
        "kitob": Kitob.objects.all().order_by("-sahifa")[0:3]
    }
    return render(request,'sahifasi_kop.html',content)

def kitob_soni_gt(request):
    content={
        "muallif": Muallif.objects.all().order_by("-kitoblar_soni")[0:3]
    }
    return render(request,'kitobi_kop.html',content)

def trik_kitob(request):
    content={
        "kitob": Kitob.objects.filter(muallif__trik=True)
    }
    return render(request,'trik_kitobi.html',content)

def badiiy(request):
    content = {
        "kitoblar": Kitob.objects.filter(janr='Badiiy')
    }
    return render(request,'badiiy.html',content)

def talaba_ochir(request,son):
    Talaba.objects.filter(id=son).delete()
    return redirect("/talabalar/")

def kitob_ochir(request,son):
    Kitob.objects.filter(id=son).delete()
    return redirect("/kitoblar/q")