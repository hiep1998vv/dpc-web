from django.urls import path
from . import views

urlpatterns = [

    # path('today/', views.plot_liveOPR_byday, name= 'today'),
    # path('thismonth/', views.plotview, name= 'thismonth'),
    path('', views.index, name= 'test'),
    
    ]