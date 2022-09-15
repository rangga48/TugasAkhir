
from django.core.files.storage import default_storage
from django.urls import resolve, reverse
import json
from .context_model import Model
model = Model()
def navigation_context(request):
    context_data = dict()
    if "role" in request.session:
        if request.session['role'] == "admin":
            context_data['profile_name'] = "Administrator"
        elif request.session['role'] == "siswa":
            data = model.getSiswa({
                "nis":request.session['user_role_id']
            }).getResult()
            data_2 = model.getAllTugas(request.session['user_role_id']).getResult()
            context_data['profile_name'] = data['nama']
            context_data['notifikasi_tugas_alert'] = len(data_2)
        elif request.session['role'] == "guru":
            data = model.getGuru({
                "id_guru":request.session['user_role_id']
            }).getResult()
            context_data['profile_name'] = data['nama']
    return context_data