from django.contrib import admin
from django.urls import path , include
from basic_app import views


app_name  = 'basic_app'


urlpatterns = [

    path('',views.SchoolListView.as_view(),name='list'),
    path('<int:pk>/',views.SchoolDetailView.as_view(),name='details'),
    path('create/',views.SchoolCreateView.as_view(),name='create'),
    path('update/<int:pk>',views.SchoolUpdateView.as_view(),name='update'),
    path('delete/<int:pk>',views.SchoolDeleteView.as_view(),name='delete'),
    path('createstudent/',views.StudentCreateView.as_view(),name='createstudent'),
    path('updatestudent/<int:pk>/',views.StudentUpdateView.as_view(),name='update_student'),
    path('studentlist',views.StudentListView.as_view(),name='studentlist'),
    path('student/<int:pk>/',views.StudentDetailView.as_view(),name='student_details'),
]
