from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
import json
from . import models
model = models.Model()
hari_temp=["Senin", "Selasa","Rabu","Kamis","Jumat"]
def index(request, id_agenda):
    data = model.getAllTugas({
        "id_agenda":id_agenda
    }).getResult()
    tugas_enabled = True
    if len(data)>=1:
        tugas_enabled = False
    return render(request, 'guru/tugas/index.html', {
        "data":data,
        "id_agenda":id_agenda,
        "tugas_enabled":tugas_enabled
    })

def tambah(request, id_agenda):
    if request.method == "POST":
        konten = request.POST.get("konten")
        attachment = request.POST.get("attachment")
        title = request.POST.get("title")
        inputval = {
            "id_agenda":id_agenda,
            "title":title,
            "konten":konten,
            "attachment":attachment
        }
        model.postTugas(inputval)
        return redirect("/guru/tugas/"+id_agenda)
    return render(request, 'guru/tugas/tambah.html', {
        "id_agenda":id_agenda
    })

def ubah(request, id_agenda, id_tugas):
    data = model.getTugas({
        "id_tugas":id_tugas
    }).getResult()
    if request.method == "POST":
        konten = request.POST.get("konten")
        attachment = request.POST.get("attachment")
        title = request.POST.get("title")
        inputval = {
            "id_agenda":id_agenda,
            "konten":konten,
            "attachment":attachment,
            "title":title
        }
        model.patchTugas(inputval, {
            "id_tugas":id_tugas
        })
        return redirect("/guru/tugas/"+id_agenda)
    return render(request, 'guru/tugas/ubah.html', {
        "id_agenda":id_agenda,
        "id_tugas":id_tugas,
        "data":data
    })

def hapus(request, id_agenda, id_tugas):
    inputval = {
        "id_tugas":id_tugas
    }
    model.deleteTugas(inputval)
    return redirect("/guru/tugas/"+id_agenda)

def pengerjaan(request, id_tugas):
    data = model.getAllTugasPengerjaan({
        "id_tugas":id_tugas
    }).getResult()
    return render(request, 'guru/tugas/pengerjaan.html', {
        "data":data
    })

def approve(request, id_tugas_pengerjaan, id_tugas):
    model.patchTugasPengerjaan({
        "is_approved":1,
        "nilai":request.POST.get("nilai")
    },{
        "id_tugas_pengerjaan":id_tugas_pengerjaan
    })
    return redirect(reverse("guru:tugas:pengerjaan", kwargs={"id_tugas":id_tugas}))
