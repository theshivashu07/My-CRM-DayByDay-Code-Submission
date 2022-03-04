from django.urls import path
from . import views,views20210608for03,views20210608for05
from dailyTasks.views20210608for03 import assignment1,assignment2,assignment2sep,assignment3,assignment4,feedback,onlysum,checkprime,factorial,middleno,middleno,largestno,markseetstudent


urlpatterns=[
		path('',views.index,name='index'),
		path('index/',views.index,name='index'),
		path('showRegistrations20210611/',views.showRegistrations20210611,name='showRegistrations20210611'),
		path('addCourse20210615/',views.addCourse20210615,name='addCourse20210615'),
		path('viewCourse20210615/',views.viewCourse20210615,name='viewCourse20210615'),
		path('addStudent20210615/',views.addStudent20210615,name='addStudent20210615'),
		path('viewStudent20210615/',views.viewStudent20210615,name='viewStudent20210615'),



#--------------------------------------------------------------------------------------------------------------------------



		path('assignment120210608/',assignment1.as_view()),
		path('assignment220210608/',assignment2.as_view()),
		path('assignment2sep20210608/',assignment2sep.as_view()),
		path('assignment320210608/',assignment3.as_view()),
		path('assignment420210608/',assignment4.as_view()),
		path('feedback20210608/',feedback.as_view()), 
		path('onlysum20210608/',onlysum.as_view()),
		path('checkprime20210608/',checkprime.as_view()),
		path('factorial20210608/',factorial.as_view()),
		path('middleno20210608/',middleno.as_view()),
		path('largestno20210608/',largestno.as_view()),
		path('markseetstudent20210608/',markseetstudent.as_view()), 

		path('calcEMIdirect20210608/',views20210608for05.calcEMIdirect,name='calcEMIdirect20210608'),
		path('calcEMI20210608/',views20210608for05.calcEMI,name='calcEMI20210608'),
		path('calcCovid20210608/',views20210608for05.calcCovid,name='calcCovid20210608'),












]