from django.urls import path
from .views import *

urlpatterns = [
    path("", homepage, name="home"),
    path("display1/", displaypage, name="display"),

    path("informations/", add_data, name="add_data1"),
    path("patient_data/",patient_data,name="patients_physical_data"),
    path("patient_display1/",display_patient,name="patient_display_physical"),
    path("update_information/<int:id>/", Update_information, name="update_information"),
    path("delete_information/<int:id>/",Delete_information, name="delete_information"),
    ##
    path("update_patient/<int:id>/",Update_patient, name="update_patient"),
    path("delete_patient/<int:id>/",Delete_patient, name="delete_patient"),
    path("hospital/", hospital_info, name="hospital_info"),
]
