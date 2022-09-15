import json
import os
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
import importlib
class MainViewProcess:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
    def process_view(request, view_func, view_args, view_kwargs,a):
        app_name = view_func.resolver_match.app_names
        modeler = importlib.import_module("apps."+app_name[0]+".apps")
        if modeler.require_login != None and modeler.require_login == True:
            try:
                print(view_func.session)
                if "user_role_id" in view_func.session:
                    return None
                else:
                    if modeler.require_login == True:
                        return redirect("/login/")
                    else:
                        return None
            except Exception as err:
                print(err)
        else:
            return None

    