from django.urls import path
from . import views

urlpatterns=[
		path('',views.index,name='index'),
		path('index/',views.index,name='index'),

		path('onlysum1/',views.onlysum1,name='onlysum1'),
		path('onlysum1/onlysum2/',views.onlysum2,name='onlysum2'),

		path('checkprime1/',views.checkprime1,name='checkprime1'),
		path('checkprime1/checkprime2/',views.checkprime2,name='checkprime2'),

		path('middleno1/',views.middleno1,name='middleno1'),
		path('middleno1/middleno2/',views.middleno2,name='middleno2'),

		path('largestno1/',views.largestno1,name='largestno1'),
		path('largestno1/largestno2/',views.largestno2,name='largestno2'),

		path('markseetstudent1/',views.markseetstudent1,name='markseetstudent1'),
		path('markseetstudent1/markseetstudent2/',views.markseetstudent2,name='markseetstudent2'),
		#path('/',views.,name=''),
		#path('//',views.,name=''),

]


