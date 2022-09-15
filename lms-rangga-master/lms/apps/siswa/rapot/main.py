from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, FileResponse
import json
from . import models
from django.urls import reverse
import uuid
import mimetypes
from services import upload
import requests
import io
from reportlab.pdfgen import canvas
from reportlab.platypus.tables import Table

from io import BytesIO
import base64
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')
model = models.Model()
hari_temp=["Senin", "Selasa","Rabu","Kamis","Jumat"]
def index(request):
    print(request.session)
    data = model.getAllKelas({
        "nis":str(request.session['user_role_id'])
    }).getResult()
    
    return render(request, 'siswa/rapot/index.html', {
        "data":data
    })



def detail(request, id_kelas):
    print(request.session)
    data = model.getAllNilai({
        "c.nis":str(request.session['user_role_id']),
        "a.id_kelas":id_kelas
    }).getResult()
    result = []
    plt.clf()
    for x in data:
        predict_data = requests.post('http://localhost:5000/get-nilai',json={
            "harian":str(int(x['nilai_harian_tugas'])),
            "uts":x['nilai_uts'],
            "uas":x['nilai_uas'],
            "keterampilan":x['nilai_keterampilan']
        },headers={
            "Content-Type":"application/json"
        })
        predict_data_svm = requests.post('http://localhost:5000/get-nilai-svm',json={
            "pengetahuan":str((int(x['nilai_harian_tugas'])+x['nilai_uts']+x['nilai_uas'])/3),
            "keterampilan":x['nilai_keterampilan']
        },headers={
            "Content-Type":"application/json"
        })
        if predict_data.status_code != 500 and predict_data_svm.status_code != 500:
            data_pred = json.loads(predict_data.text);
            x['nilai_predict'] = data_pred['hasil']
            x['label_predict'] = ""
            if x['nilai_predict'] >= 0.59:
                x['label_predict'] = "Lulus"
            else:
                x['label_predict'] = "Tidak Lulus"
            data_pred_svm = json.loads(predict_data_svm.text)
            print(data_pred_svm['hasil'])
            x['label_predict_svm'] = "Lulus" if data_pred_svm['hasil'] == "1" else "Tidak Lulus"
        else:
            x['nilai_predict'] = None
            x['label_predict'] = "Tidak Diketahui"
            x['label_predict_svm'] = "Tidak Diketahui"
        result.append(x)
    return render(request, 'siswa/rapot/detail.html', {
        "data":data,
        "id_kelas":id_kelas
    })

def detail_nilai(request, id_jadwal, id_kelas):
    
    data = model.getNilai({
        "c.nis":str(request.session['user_role_id']),
        "a.id_jadwal":id_jadwal,
        "a.id_kelas":id_kelas
    }).getResult()
    if data == None:
        data = {
            "nilai_harian_tugas":0,
            "nilai_uts":0,
            "nilai_uas":0,
            "nilai_keterampilan":0
        }
    data_tugas = model.getAllTugas(str(request.session['user_role_id']), id_jadwal).getResult()
    data['nilai_harian_tugas'] = 0 if data['nilai_harian_tugas'] == None else data['nilai_harian_tugas']
    data['nilai_uts'] = 0 if data['nilai_uts'] == None else data['nilai_uts']
    data['nilai_uas'] = 0 if data['nilai_uas'] == None else data['nilai_uas']
    data['nilai_keterampilan'] = 0 if data['nilai_keterampilan'] == None else data['nilai_keterampilan']
    nilai_pengetahuan = str((int(data['nilai_harian_tugas'])+data['nilai_uts']+data['nilai_uas'])/3)
    print(data_tugas)
    
    predict_data_svm = requests.post('http://localhost:5000/get-nilai-svm',json={
        "pengetahuan":nilai_pengetahuan,
        "keterampilan":data['nilai_keterampilan']
    },headers={
        "Content-Type":"application/json"
    })
    graphic = None
    status_lulus = "Tidak Diketahui"
    print(predict_data_svm.text)
    print(data['nilai_keterampilan'])
    
    if predict_data_svm.status_code != 500:
        data_pred = json.loads(predict_data_svm.text)
        if data_pred['hasil'] == "1":
            status_lulus = "Lulus"
        elif data_pred['hasil'] == "0":
            status_lulus = "Tidak Lulus"
        import numpy
        w = data_pred['coef']
        print(w)
        print(data_pred['hasil'])
        # get the y-offset for the linear equation
        a = -w[0] / w[1]

        # make the x-axis space for the data points
        XX = numpy.linspace(0, 100)
        print("A")
        # get the y-values to plot the decision boundary
        yy = a * XX - data_pred['intercept'] / w[1]
        print(XX)
        print(yy)
        #print([nilai_pengetahuan])
        #print(data['nilai_keterampilan'])
        
        plt.plot(XX, yy, 'k-')
        import matplotlib.colors
        cmap = matplotlib.colors.ListedColormap(["gold", "crimson"])
        #print(list(data_pred['support_vector']))
        scatter = plt.scatter([float(nilai_pengetahuan)]+[x[0] for x in data_pred['support_vector']], [float(data['nilai_keterampilan'])]+[x[1] for x in data_pred['support_vector']], cmap=cmap,c=[1]+[0 for x in  data_pred['support_vector']])
        plt.legend(handles=scatter.legend_elements()[0], labels=['Support Vector','Nilai Anda'])
        plt.text(numpy.average(XX)/2, numpy.average(yy)/2, 'Tidak Lulus', fontsize = 10)
        plt.text(numpy.average(XX)*1.5, numpy.average(yy)*1.5, 'Lulus', fontsize = 10)
        plt.tight_layout()
        plt.clf()
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()

        graphic = base64.b64encode(image_png)
        graphic = graphic.decode('utf-8')
        
    return render(request, 'siswa/rapot/detail_nilai.html', {
        "data":data,
        "id_kelas":id_kelas,
        "data_tugas":data_tugas,
        "nilai_pengetahuan":nilai_pengetahuan,
        "graphic":graphic,
        "status_lulus":status_lulus
    })

def cetak_rapot(request, id_kelas):
    print(request.session)
    data = model.getAllNilai({
        "c.nis":str(request.session['user_role_id']),
        "a.id_kelas":id_kelas
    }).getResult()
    result = []
    for x in data:
        predict_data = requests.post('http://localhost:5000/get-nilai',json={
            "harian":x['nilai_harian_tugas'],
            "uts":x['nilai_uts'],
            "uas":x['nilai_uas'],
            "keterampilan":x['nilai_keterampilan']
        },headers={
            "Content-Type":"application/json"
        })
        if predict_data.status_code != 500:
            data_pred = json.loads(predict_data.text);
            x['nilai_predict'] = data_pred['hasil']
            x['label_predict'] = ""
            if x['nilai_predict'] >= 0.59:
                x['label_predict'] = "Lulus"
            else:
                x['label_predict'] = "Tidak Lulus"
        else:
            x['nilai_predict'] = None
            x['label_predict'] = "Tidak Diketahui"
        result.append(x)
    result_table = []
    for x in result:
        result_table.append([x["nama_mata_pelajaran"],x['nilai_predict']])
    buffer = io.BytesIO()
    x = canvas.Canvas(buffer)
    x.drawString(220, 800, "Rapot Siswa")
    f = Table(result_table)
    f.wrapOn(x, 200, 200)
    f.drawOn(x, 100,600)
    x.showPage()
    x.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='attempt1.pdf')
# data = model.getAllNilai({
#         "id_kelas":id_kelas,
#         "nis":request.session['user_role_id']
#     }).getResult()