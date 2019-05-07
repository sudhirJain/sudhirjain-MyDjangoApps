
from django.conf.urls import url 
from django.urls import path 
from .views import ( 
    PostListView, 
    PostDetailView, 
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views

urlpatterns = [
    # url(r'^$',views.home, name='blog-home'),
    url(r'^$',PostListView.as_view(), name='blog-home'),
    path('user/<str:username>',UserPostListView.as_view(), name='user-posts'),
    # url(r'^post/<int:pk>/',PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/',PostDetailView.as_view(), name='post-detail'),
    path('post/new/',PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(), name='post-update'),
    # url(r'^about/',views.about, name='blog-about'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(), name='post-delete'),
    path('about/',views.about, name='blog-about'),
];
