from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),  # Blog homepage
    path('<int:post_id>/', views.detail, name='detail'),  # Post detail
    path('<int:post_id>/comments/', views.comments, name='comments'),  # Comments for a post
]
