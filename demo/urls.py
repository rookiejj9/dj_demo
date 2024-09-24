from django.urls import path
from . import views

app_name = 'demo'
urlpatterns = {
    path('', views.IndexView.as_view(),name='index'),
}