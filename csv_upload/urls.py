from django.urls import path
from.views import *

urlpatterns = [
    path('upload_csv/', upload_csv , name = "upload_csv"),

]
