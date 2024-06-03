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
    path('locations_list/', views.LocationList.as_view(), name='location-list'),
    path('locations_list/add', views.LocationCreateView.as_view(), name='location-add'),
    path('locations_list/<pk>', views.LocationUpdateView.as_view(), name='location-update'),
    path('locations_list/<pk>/delete', views.LocationDeleteView.as_view(), name='location-delete'),
    
    
    
]
