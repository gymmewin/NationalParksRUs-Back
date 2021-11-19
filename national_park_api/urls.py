from django.urls import path
from . import views

urlpatterns = [
    path('api/national-parks', views.NationalParkList.as_view(), name='national_park_list'),
    path('api/national-parks/<int:pk>', views.NationalParkDetail.as_view(), name='national_park_detail'),
    path('api/attractions', views.AttractionList.as_view(), name='attraction_list'),
    path('api/attractions/<int:pk>', views.AttractionList.as_view(), name='attraction_detail'),
]
