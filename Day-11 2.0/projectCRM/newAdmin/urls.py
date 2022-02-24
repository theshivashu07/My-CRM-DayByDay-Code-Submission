from django.urls import path
from . import views

urlpatterns=[
		path('',views.index,name='index'),
		path('mapsgmap/',views.mapsgmap,name='mapsgmap'),
		path('mapsvector/',views.mapsvector,name='mapsvector'),

]





