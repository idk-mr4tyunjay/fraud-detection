from django.shortcuts import render, redirect

import requests
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import ApiCodeSerializer
from .forms import CustomUserForm


def home(request):
    ak = "3e9e926f-9dcd-4b1f-9df6-f74365275f1a"
    gURL = "http://13.48.136.54:8000/api/api-code/"
    headers = {
        "Authorization": f"Bearer {ak}"
    }
    response = requests.post(gURL, headers=headers)

    if response.status_code == 200:
        api_code = response.json().get('api_code', "No api code received")
    else:
        api_code = "Error in retrieving api code"
    context = {"api_code": api_code}
    return render(request, 'base/home.html', context)


class ApiCodeViewSet(viewsets.ViewSet):
    def retrieve(self, request):
        ak = "3e9e926f-9dcd-4b1f-9df6-f74365275f1a"
        gURL = "http://13.48.136.54:8000/api/api-code/"
        headers = {
            "Authorization": f"Bearer {ak}"
        }
        response = requests.post(gURL, headers=headers)

        if response.status_code == 200:
            api_code = response.json().get('api_code', "No api code received")
        else:
            api_code = "Error in retrieving api code"
        
        serializer = ApiCodeSerializer({'api_code': api_code})
        return Response(serializer.data)

def register_user(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = CustomUserForm()

    context = {
        'form': form,
    }

    return render(request, '', )