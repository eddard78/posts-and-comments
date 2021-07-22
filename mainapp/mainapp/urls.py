from django.contrib import admin
from rest_auth.views import LoginView
from django.urls import path
from rest_auth.registration.views import RegisterView

from posts.views import PostView, CommentView
from user.views import UserView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signin/', LoginView.as_view(), name='rest_login'),
    path('signup/', RegisterView.as_view(), name='rest_register'),
    path('user/<int:pk>', UserView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('', PostView.as_view({'get': 'list'})),
    path('post/create', PostView.as_view({'post': 'create'})),
    path('post/<int:pk>', PostView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('comment', CommentView.as_view({'post': 'create'})),
    path('comment/<int:pk>', CommentView.as_view({'put': 'update', 'delete': 'destroy'}))
]