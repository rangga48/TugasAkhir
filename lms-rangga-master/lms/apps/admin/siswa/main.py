from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
from . import models
model = models.Model()
def index(request):
    data = model.getAllSiswa().getResult()
    return render(request, 'admin/siswa/index.html', {
        "data":data
    })

def tambah(request):
    if request.method == "POST":
        nis = request.POST.get("nis")
        nama = request.POST.get("nama")
        tanggal_lahir = request.POST.get("tanggal_lahir")
        jenis_kelamin = request.POST.get("jenis_kelamin")
        inputval = {
            "nis":nis,
            "nama":nama,
            "jenis_kelamin":jenis_kelamin,
            "tanggal_lahir":tanggal_lahir
        }
        model.postSiswa(inputval)
        return redirect("/admin/siswa")
    return render(request, 'admin/siswa/tambah.html')

def ubah(request, nis):
    data = model.getSiswa({"nis":nis}).getResult()
    view_data = {
        "nis":data['nis'],
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
            "nis":nis
        })
        return redirect("/admin/siswa")
    print(view_data)
    return render(request, 'admin/siswa/ubah.html', view_data)

def hapus(request, nis):
    model.deleteSiswa({
        "nis":nis
    })
    return redirect("/admin/siswa")
