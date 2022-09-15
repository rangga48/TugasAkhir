from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
from . import models
model = models.Model()
def index(request):
    data = model.getAllSiswa().getResult()
    return render(request, 'admin/kelas/index.html', {
        "data":data
    })

def tambah(request):
    if request.method == "POST":
        nama = request.POST.get("nama")
        wali_kelas = request.POST.get("wali_kelas")
        inputval = {
            "nama":nama,
            "wali_kelas":wali_kelas
        }
        model.postSiswa(inputval)
        return redirect("/admin/kelas")
    data = model.getGuru().getResult()
    args = {
        "data_wali_kelas":data
    }
    return render(request, 'admin/kelas/tambah.html', args)

def ubah(request, id_kelas):
    data = model.getSiswa({"id_kelas":id_kelas}).getResult()
    view_data = {
        "id_kelas":data['id_kelas'],
        "nama":data['nama'],
        "wali_kelas":data['wali_kelas']
    }
    if request.method == "POST":
        nama = request.POST.get("nama")
        wali_kelas = request.POST.get("wali_kelas")
        inputval = {
            "nama":nama,
            "wali_kelas":wali_kelas
        }
        print(inputval)
        model.patchSiswa(inputval, {
            "id_kelas":id_kelas
        })
        return redirect("/admin/kelas")
    data = model.getGuru().getResult()
    view_data['data_wali_kelas'] = data
    return render(request, 'admin/kelas/ubah.html', view_data)

def hapus(request, id_kelas):
    model.deleteSiswa({
        "id_kelas":id_kelas
    })
    return redirect("/admin/kelas")
