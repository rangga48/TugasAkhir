from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
from . import models
model = models.Model()
hari_temp=["Senin", "Selasa","Rabu","Kamis","Jumat"]
def index(request, id_jadwal):
    data = model.getAllMateriByJadwal(id_jadwal).getResult()
    return render(request, 'siswa/materi/index.html', {
        "data":data,
        "id_jadwal":id_jadwal
    })
        
