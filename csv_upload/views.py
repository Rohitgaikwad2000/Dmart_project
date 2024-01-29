from django.shortcuts import render, redirect, HttpResponse
import csv
from .models import EleProduct
from.forms import CsvUploadForm
# Create your views here.


def handle_csv_file(csv_file):
    decode_file = csv_file.read().decode('utf-8').splitlines()
    csv_reader = csv.reader(decode_file)
    headers = next(csv_reader)
    # print(headers)               # for print header
    for row in csv_reader:
            employee_data = dict(zip(headers, row))
            # print("employee_data:-", employee_data)             # print all the data in terminal
            EleProduct.objects.create(**employee_data)



def upload_csv(request):
    if request.method == "POST":
        form = CsvUploadForm(request.POST, request.FILES)
        if form.is_valid():
            handle_csv_file(request.FILES["csv_file"])
            return HttpResponse("File uploaded succesfully....")
    else:
        form = CsvUploadForm()
    return render(request, 'upload_csv.html', {"form":form})
        
