from django.urls import path
from . import views

# register our namespace
app_name = 'core'

urlpatterns = [
    path('', views.BookListView.as_view(), name='index'),
]
