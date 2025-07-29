from django.urls import path
from apps.dashboard import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tables/', views.tables, name="tables"),
    path('billing/', views.billing, name="billing"),
    path('notifications/', views.notifications, name="notifications"),
    path('profile/', views.profile, name="profile"),
    path('map/', views.map, name="map"),
    path('icons/', views.icons, name="icons"),
    path('typography/', views.typography, name="typography"),
    path('template/', views.template, name="template"),
]
