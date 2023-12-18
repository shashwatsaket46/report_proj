from django.urls import path
from .views import (
    home_view,
    SalesListView,
    SalesDetailView,
)

app_name='salesr'

urlpatterns =[
    path('',home_view,name='home'),
    path('salesr/',SalesListView.as_view(),name='list'),
    path('salesr/<pk>/',SalesDetailView.as_view(),name='detail'),
]