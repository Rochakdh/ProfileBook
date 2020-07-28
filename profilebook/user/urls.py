from django.urls import path
from . import views

app_name = 'user'
urlpatterns=[
    path('login/',views.LoginView.as_view(),name='login'),
    path('logout/',views.LogoutView.as_view(), name='logout'),
    path('profile/',views.ProfileView.as_view(),name='profile'),
    path('profile/update/<int:pk>/',views.UpdateProfile.as_view(),name='update')
]