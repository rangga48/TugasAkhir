from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
from . import models
model = models.Model()
hari_temp=["Senin", "Selasa","Rabu","Kamis","Jumat"]
def index(request):
    data = model.getAllJadwal().getResult()
    data = [
        {
            **x,
            "hari":hari_temp[x['hari']]
        } for x in data
    ]
    return render(request, 'admin/jadwal/index.html', {
        "data":data
    })

def tambah(request):
    data_guru = model.getAllGuru().getResult()
    data_kelas = model.getAllKelas().getResult()
    data_mata_pelajaran = model.getAllMataPelajaran().getResult()
    if request.method == "POST":
        id_guru = request.POST.get("id_guru")
        id_kelas = request.POST.get("id_kelas")
        id_mata_pelajaran = request.POST.get("id_mata_pelajaran")
        waktu = request.POST.get("waktu")
        hari = request.POST.get("hari")
        inputval = {
            "id_guru":id_guru,
            "id_kelas":id_kelas,
            "id_mata_pelajaran":id_mata_pelajaran,
            "waktu":waktu,
            "hari":hari
        }
        model.postJadwal(inputval)
        return redirect("/admin/jadwal")
    return render(request, 'admin/jadwal/tambah.html',{
        "data_guru":data_guru,
        "data_kelas":data_kelas,
        "data_mata_pelajaran":data_mata_pelajaran,
        "hari":hari_temp
    })


def hapus(request, id_jadwal):
    model.deleteJadwal({
        "id_jadwal":id_jadwal
    })
    return redirect("/admin/jadwal")
