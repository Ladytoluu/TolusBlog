# # pages/urls.py
# from django.urls import path
# from .views import HomePageView

# urlpatterns = [
#     path('', HomePageView.as_view(), name='home'),
# ]

# # urlpatterns = [
# #     path('', views.PostList.as_view(), name='home'),
# #     path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
# # ]

from . import views
from django.urls import path
from .views import SignUpView
from django.contrib.auth import views as auth_views
from django.conf.urls import url


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    url('password/', views.change_password, name='change_password'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
     name='password_reset'),
    
     

]