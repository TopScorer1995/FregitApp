from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
import json

# from samples.static.WorkSpace import  List_Workspace

import os
import shutil
import re

from datetime import datetime
import configparser


def home(request):
    return render(request, 'index.html', {'item': 'home'})


def dashboard(request):
    return render(request, 'dashboard.html', {'item': 'dashboard'})


def add_new_tab(request):
    return render(request, 'add_new_tab.html', {'item': 'add_new_tab'})


def showtab(request):
    return render(request, 'showtab.html', {'item': 'showtab'})


def clearance_page(request):
    return render(request, 'clearance_process.html', {'item': 'clearance', 'subitem': 'clearance_page'})


def clearance_input(request):
    return render(request, 'clearance_process_input.html', {'item': 'clearance', 'subitem': 'clearance_input'})


def client_registration(request):
    return render(request, 'client_registration.html', {'item': 'client_registration'})


def shipment_page(request):
    return render(request, 'shipment_page.html', {'item': 'shipment_page'})


# def haulage(request):
#     return render(request, 'haulage.html', {'item': 'haulage'})


def haulage_registervehicle(request):
    return render(request, 'haulage_registervehicle.html', {'item': 'haulage', 'subitem': 'registervehicle'})


def haulage_deliverydetails(request):
    return render(request, 'haulage_deliverydetails.html', {'item': 'haulage', 'subitem': 'deliverydetails'})


def haulage_packaging(request):
    return render(request, 'haulage_packaging.html', {'item': 'haulage', 'subitem': 'packaging'})


def reports(request):
    return render(request, 'issues_challenges.html', {'item': 'reports'})


def shipment_registration(request):
    return render(request, 'shipment_registration.html', {'item': 'shipment_registration'})


def shipment_registration_air(request):
    return render(request, 'shipment_registration_air.html', {'item': 'shipment_registration', 'subitem': 'shipment_registration_air'})


def shipment_registration_ocean(request):
    return render(request, 'shipment_registration_ocean.html', {'item': 'shipment_registration', 'subitem': 'shipment_registration_ocean'})


def payment(request):
    return render(request, 'payment.html', {'item': 'payment'})


def documentation(request):
    return render(request, 'documentation.html', {'item': 'documentation'})