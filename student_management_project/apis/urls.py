from django.urls import path
from .import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('students/', views.students_list),
    path('student/<int:pk>/', views.student_management),
    path('addtask/', views.add_task),
    path('viewtasks/', views.task_list),
    path('taskmanage/<int:pk>/', views.task_management),
    path('student_tasks/', views.student),
    path('update_task/<int:pk>/', views.update_task)
]
