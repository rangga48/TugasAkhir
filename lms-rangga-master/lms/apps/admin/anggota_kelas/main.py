from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
from . import models
model = models.Model()
def index(request, id_kelas):
    data = model.getAllAnggotaKelas({
        "c.id_kelas":id_kelas
    }).getResult()
    return render(request, 'admin/anggota_kelas/index.html', {
        "data":data,
        "id_kelas":id_kelas
    })



def tambah(request, id_kelas):
    if request.method == "POST":
        nis = request.POST.get("nis")
        inputval = {
            "id_kelas":id_kelas,
            "nis":nis
        }
        model.postAnggotaKelas(inputval)
        return redirect("/admin/anggota_kelas/"+id_kelas)
    data_siswa = model.getSiswa().getResult()
    return render(request, 'admin/anggota_kelas/tambah.html',{
        "data_siswa":data_siswa,
        "id_kelas":id_kelas
    })

def hapus(request, nis, id_anggota_kelas, id_kelas):
    inputval = {
        "nis":nis,
        "id_anggota_kelas":id_anggota_kelas
    }
    model.deleteAnggotaKelas(inputval)
    return redirect("/admin/anggota_kelas/"+id_kelas)