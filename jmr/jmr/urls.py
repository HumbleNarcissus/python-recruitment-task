from django.urls import path

from . import views

app_name = 'jmr'
urlpatterns = [
    path('', views.index, name='index'),
    path('<shortcut>', views.redirect_to_base_url, name='redirect')
]