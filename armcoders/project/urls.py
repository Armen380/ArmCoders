from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",Home,name="home"),
    path("categories/<int:categoryId>/",PostList, name="categories"),
    path("post/<int:postId>/", PostDetail, name="post"),
    path("NewPosts",NewPosts,name="newsPost"),
    path("TopPosts",TopPosts,name="topPost")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)