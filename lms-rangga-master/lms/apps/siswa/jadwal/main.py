from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
from . import models
model = models.Model()
hari_temp=["Senin", "Selasa","Rabu","Kamis","Jumat"]
def index(request):
    data = model.getAllJadwal({
        "b.nis":request.session['user_role_id']
    }).getResult()
    data = [
        {
            **x,
            "hari":hari_temp[x['hari']]
        } for x in data
    ]
    return render(request, 'siswa/jadwal/index.html', {
        "data":data
    })

