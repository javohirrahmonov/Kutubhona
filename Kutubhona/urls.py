from django.contrib import admin
from django.urls import path
from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('salom/', salomlash),
    path('', bosh_sahifa),
    path('men/', salom),
    path('talabalar/', talabalar),
    path('kitoblar/', kitoblar),
    path('mualliflar/', mualliflar),
    path('bitiruvchilar/', bitiruvchilar),
    path('kitob_bor/', kitobbor),
    path('talaba/<int:son>/', bitta_talaba),
    path('a_li/', talaba_a),
    path('record/<int:son>', record),
    path('muallif/<int:son>/', muallif),
    path('kitob/<int:son>/', bitta_kitob),
    path('ochirish/<int:son>/', talaba_ochir),
    path('recordlar/',recordlar),
    path('tirik_muallif/',tirik_muallif),
    path('sahifasi_kop3/',sahifa_gt),
    path('kitobi_kop3/',kitob_soni_gt),
    # path('ohirgi_record/',ohirgi),
    path('trik_kitobi/',trik_kitob),
    path('badiiy/',badiiy),
    path('kitob_ochir/<int:son>/',kitob_ochir),
]
