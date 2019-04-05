from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.index, name='index'),
    path('index2/', views.index2, name='index2'),
    path('<str:mode>/step/<int:step_number>/patient/<str:patient_id>/', views.wizard_view,
         name='wizard'),
    path('<str:mode>/step/<int:step_number>/patient/<str:patient_id>/object/<int:object_id>/', views.wizard_view,
         name='wizard'),
    path('<str:mode>/patients/', views.patient_list, name='patient-list'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('advanced_filters/', include('advanced_filters.urls'))
]

handler403 = 'ns_record_web.views.index'
