from django.contrib import admin
from django.urls import path

from fire.views import HomePageView
from fire import views
from fire.views import HomePageView, ChartView, PieCountbySeverity, LineCountbyMonth, MultilineIncidentTop3Country, multipleBarbySeverity


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('dashboard_chart', ChartView.as_view(), name='dashboard-chart'),
    path('chart/', PieCountbySeverity, name='chart'),
    path('lineChart/', LineCountbyMonth, name='chart'),
    path('multilineChart/', MultilineIncidentTop3Country, name='chart'),
    path('multiBarChart/', multipleBarbySeverity, name='chart'),
    path('stations', views.map_station, name='map-station'),
    path('incidents', views.map_incident, name='map-incidents'),
    path('locations_list/', views.LocationList.as_view(), name='location-list'),
    path('locations_list/add', views.LocationCreateView.as_view(), name='location-add'),
    path('locations_list/<pk>', views.LocationUpdateView.as_view(), name='location-update'),
    path('locations_list/<pk>/delete', views.LocationDeleteView.as_view(), name='location-delete'),
    
    path('incident_list/', views.IncidentList.as_view(), name='incident-list'),
    path('incident_list/add', views.IncidentCreateView.as_view(), name='incident-add'),
    path('incident_list/<pk>', views.IncidentUpdateView.as_view(), name='incident-update'),
    path('incident_list/<pk>/delete', views.IncidentDeleteView.as_view(), name='incident-delete'),
    
    path('firestation_list/', views.FireStationList.as_view(), name='firestation-list'),
    path('firestation_list/add', views.FireStationCreateView.as_view(), name='firestation-add'),
    path('firestation_list/<pk>', views.FireStationUpdateView.as_view(), name='firestation-update'),
    path('firestation_list/<pk>/delete', views.FireStationDeleteView.as_view(), name='firestation-delete'),
    
    path('fire_fighter_list/', views.FirefighterList.as_view(), name='firefighter-list'),
    path('fire_fighter_list/add', views.FirefighterCreateView.as_view(), name='firefighter-add'),
    path('fire_fighter_list/<pk>', views.FirefighterUpdateView.as_view(), name='firefighter-update'),
    path('fire_fighter_list/<pk>/delete', views.FirefighterDeleteView.as_view(), name='firefighter-delete'),
    
    path('firetruck_list/', views.FiretruckList.as_view(), name='firetruck-list'),
    path('firetruck_list/add', views.FiretruckCreateView.as_view(), name='firetruck-add'),
    path('firetruck_list/<pk>', views.FiretruckUpdateView.as_view(), name='firetruck-update'),
    path('firetruck_list/<pk>/delete', views.FiretruckDeleteView.as_view(), name='firetruck-delete'),
    
    path('weathercondition_list/', views.WeatherCondition.as_view(), name='weathercondition-list'),
    path('weathercondition_list/add', views.WeatherConditionCreateView.as_view(), name='weathercondition-add'),
    path('weathercondition_list/<pk>', views.WeatherConditionUpdateView.as_view(), name='weathercondition-update'),
    path('weathercondition_list/<pk>/delete', views.WeatherConditionDeleteView.as_view(), name='weathercondition-delete'),
    
    
    
    
    
]
