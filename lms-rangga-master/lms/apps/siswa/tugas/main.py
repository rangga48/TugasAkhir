from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
from . import models
from django.urls import reverse
import uuid
import mimetypes
from services import upload
model = models.Model()
hari_temp=["Senin", "Selasa","Rabu","Kamis","Jumat"]
def index(request, id_jadwal):
    data = model.getAllTugasByJadwal(request.session['user_role_id'],id_jadwal).getResult()
    
    return render(request, 'siswa/tugas/index.html', {
        "data":data,
        "id_jadwal":id_jadwal
    })

def submit(request, id_agenda, id_tugas, id_jadwal):
    if request.method == "POST":
        tugas_pengerjaan = model.getTugasPengerjaan({
            "id_tugas":id_tugas,
            "nis":request.session['user_role_id']
        }).getResult()
        attachment_file = "tugas_pengerjaan"+str(request.session['user_role_id'])+"_"+str(id_tugas)+"_"+str(id_jadwal)+"_"+str(uuid.uuid4())+mimetypes.guess_extension(request.FILES['file'].content_type)
        data = {
            "konten":request.POST.get("konten"),
            "attachment":attachment_file
        }
        if tugas_pengerjaan != None:
            model.patchTugasPengerjaan(data, where={
                "id_tugas_pengerjaan":tugas_pengerjaan['id_tugas_pengerjaan']
            })
        else:
            data['id_tugas'] = id_tugas
            data['nis'] = request.session['user_role_id']
            model.postTugasPengerjaan(data)
        print(dir(request.FILES['file']))
        print(mimetypes.guess_extension(request.FILES['file'].content_type))
        upload.handle_uploaded_file(request.FILES['file'], attachment_file)
        return redirect(reverse("siswa:tugas:index", kwargs={"id_jadwal":id_jadwal}))
    return render(request, "siswa/tugas/submit.html",{
        "id_tugas":id_tugas,
        "id_agenda":id_agenda,
        "id_jadwal":id_jadwal
    })

