from django.urls import path, re_path
from accounts import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView

urlpatterns = [
    path('register/', views.register, name='register'),
    path('my_account/', views.my_account, name='my_account'),
    re_path(r'^order_details/(?P<order_id>[-\w]+)/$', views.order_details, name='order_details'),
    path('order_info/', views.order_info,  name='order_info'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password-change/', PasswordChangeView.as_view(), name='password-change'),
]
