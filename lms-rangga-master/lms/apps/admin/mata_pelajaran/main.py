from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
from . import models
model = models.Model()
def index(request):
    data = model.getAllSiswa().getResult()
    return render(request, 'admin/mata_pelajaran/index.html', {
        "data":data
    })

def tambah(request):
    if request.method == "POST":
        nama = request.POST.get("nama")
        inputval = {
            "nama":nama
        }
        model.postSiswa(inputval)
        return redirect("/admin/mata_pelajaran")
    return render(request, 'admin/mata_pelajaran/tambah.html')

def ubah(request, id_mata_pelajaran):
    data = model.getSiswa({"id_mata_pelajaran":id_mata_pelajaran}).getResult()
    view_data = {
        "id_mata_pelajaran":data['id_mata_pelajaran'],
        "nama":data['nama']
    }
    if request.method == "POST":
        nama = request.POST.get("nama")
        inputval = {
            "nama":nama
        }
        model.patchSiswa(inputval, {
            "id_mata_pelajaran":id_mata_pelajaran
        })
        return redirect("/admin/mata_pelajaran")
    print(view_data)
    return render(request, 'admin/mata_pelajaran/ubah.html', view_data)

def hapus(request, id_mata_pelajaran):
    model.deleteSiswa({
        "id_mata_pelajaran":id_mata_pelajaran
    })
    return redirect("/admin/mata_pelajaran")
