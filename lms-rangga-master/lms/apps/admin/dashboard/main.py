from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
def index(request):
    return render(request, 'admin/dashboard/index.html')