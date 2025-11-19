from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_view,name='student_view'),
    path('<int:pk>/', views.student_detail, name='student_detail'),
    # Add your API endpoints here
    # Example: path('items/', views.item_list, name='item_list'),
]
