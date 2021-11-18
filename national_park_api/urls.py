from django.urls import path
from . import views

urlpatterns = [
    path('api/national-parks', views.NationalParkList.as_view(), name='national_park_list'), 
    path('api/national-parks/<int:pk>', views.NationalParkDetail.as_view(), name='national_park_detail'),
]
