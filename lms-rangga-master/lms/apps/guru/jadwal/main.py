from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json

from ..tugas.main import tambah
from . import models
model = models.Model()
hari_temp=["Senin", "Selasa","Rabu","Kamis","Jumat"]
def index(request):
    data = model.getAllJadwal({
        "a.id_guru":request.session['user_role_id']
    }).getResult()
    data = [
        {
            **x,
            "hari":hari_temp[x['hari']]
        } for x in data
    ]
    return render(request, 'guru/jadwal/index.html', {
        "data":data
    })

def agenda(request, id_jadwal):
    
    data = model.getAllAgenda({
        "id_jadwal":id_jadwal
    }).getResult()
    tambah_activated = True
    if len(data)>=5:
        tambah_activated = False
    return render(request, 'guru/jadwal/agenda.html', {
        "data":data,
        "id_jadwal":id_jadwal,
        "tambah_activated":tambah_activated
    })

def agenda_tambah(request, id_jadwal):
    print("ASS")
    print(id_jadwal)
    return render(request, 'guru/jadwal/agenda_tambah.html', {
        "id_jadwal":id_jadwal
    })

def agenda_tambah_action(request, id_jadwal):
    if request.method == "POST":
        tema_pertemuan = request.POST.get("tema_pertemuan")
        inputval = {
            "id_jadwal":id_jadwal,
            "tema_pertemuan":tema_pertemuan
        }
        model.postAgenda(inputval)
        return redirect("/guru/jadwal/agenda/"+id_jadwal)
    
    return render(request, 'guru/jadwal/agenda.html', {
        "data":data
    })