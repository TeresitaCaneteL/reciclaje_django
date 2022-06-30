from django.urls import path
from services.views import ServicesView

app_name="services"

urlpatterns=[

    path('services/', ServicesView.as_view(), name="services"),

]