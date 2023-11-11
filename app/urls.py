from django.urls import path
from app import views

app_name = 'app'
urlpatterns = [
    path('list/', views.PostListView.as_view(), name='list'),
    path('create/', views.PostCreateView.as_view(), name='create'),
    path('detail/<str:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('update/<str:pk>/', views.PostUpdateView.as_view(), name='update'),
    path('delete/<str:pk>/', views.PostDeleteView.as_view(), name='delete'),
]
