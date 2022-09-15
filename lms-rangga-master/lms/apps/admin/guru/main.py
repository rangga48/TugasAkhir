from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
from . import models
model = models.Model()
def index(request):
    data = model.getAllSiswa().getResult()
    return render(request, 'admin/guru/index.html', {
        "data":data
    })

def tambah(request):
    if request.method == "POST":
        nama = request.POST.get("nama")
        tanggal_lahir = request.POST.get("tanggal_lahir")
        jenis_kelamin = request.POST.get("jenis_kelamin")
        inputval = {
            "nama":nama,
            "jenis_kelamin":jenis_kelamin,
            "tanggal_lahir":tanggal_lahir
        }
        model.postSiswa(inputval)
        return redirect("/admin/guru")
    return render(request, 'admin/guru/tambah.html')

def ubah(request, id_guru):
    data = model.getSiswa({"id_guru":id_guru}).getResult()
    view_data = {
        "id_guru":data['id_guru'],
        "nama":data['nama'],
        "tanggal_lahir":data['tanggal_lahir'],
        "jenis_kelamin":data['jenis_kelamin']
    }
    if request.method == "POST":
        nama = request.POST.get("nama")
        tanggal_lahir = request.POST.get("tanggal_lahir")
        jenis_kelamin = request.POST.get("jenis_kelamin")
        inputval = {
            "nama":nama,
            "jenis_kelamin":jenis_kelamin,
            "tanggal_lahir":tanggal_lahir
        }
        print(inputval)
        model.patchSiswa(inputval, {
            "id_guru":id_guru
        })
        return redirect("/admin/guru")
    print(view_data)
    return render(request, 'admin/guru/ubah.html', view_data)

def hapus(request, id_guru):
    model.deleteSiswa({
        "id_guru":id_guru
    })
    return redirect("/admin/guru")
