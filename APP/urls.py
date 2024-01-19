from django.urls import path

from APP import views

urlpatterns=[
    path('student_list',views.student_list,name='student_list'),
    path('student_detail/<int:id>/',views.student_detail,name='student_detail'),

]