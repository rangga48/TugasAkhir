from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
from . import models
model = models.Model()
hari_temp=["Senin", "Selasa","Rabu","Kamis","Jumat"]
def index(request, id_agenda):
    data = model.getAllDataAbsen(id_agenda).getResult()
    print(data)
    return render(request, 'guru/absensi/index.html', {
        "data":data,
        "id_agenda":id_agenda
    })

def absensi(request, id_agenda):
    
    model.postAbsen({
        "nis":request.POST.get("nis"),
        "status":request.POST.get("status"),
        "id_agenda":id_agenda
    }).getResult()
    
    return redirect("/guru/absensi/"+id_agenda)