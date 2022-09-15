from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
from . import models
model = models.Model()
hari_temp=["Senin", "Selasa","Rabu","Kamis","Jumat"]
def index(request, id_agenda):
    data = model.getAllMateri({
        "id_agenda":id_agenda
    }).getResult()
    return render(request, 'guru/materi/index.html', {
        "data":data,
        "id_agenda":id_agenda
    })

def tambah(request, id_agenda):
    if request.method == "POST":
        konten = request.POST.get("konten")
        attachment = request.POST.get("attachment")
        inputval = {
            "id_agenda":id_agenda,
            "konten":konten,
            "attachment":attachment
        }
        model.postMateri(inputval)
        return redirect("/guru/materi/"+id_agenda)
    return render(request, 'guru/materi/tambah.html', {
        "id_agenda":id_agenda
    })

def ubah(request, id_agenda, id_materi):
    data = model.getMateri({
        "id_materi":id_materi
    }).getResult()
    if request.method == "POST":
        konten = request.POST.get("konten")
        attachment = request.POST.get("attachment")
        inputval = {
            "id_agenda":id_agenda,
            "konten":konten,
            "attachment":attachment
        }
        model.patchMateri(inputval, {
            "id_materi":id_materi
        })
        return redirect("/guru/materi/"+id_agenda)
    return render(request, 'guru/materi/ubah.html', {
        "id_agenda":id_agenda,
        "id_materi":id_materi,
        "data":data
    })

def hapus(request, id_agenda, id_materi):
    inputval = {
        "id_materi":id_materi
    }
    model.deleteMateri(inputval)
    return redirect("/guru/materi/"+id_agenda)
        
