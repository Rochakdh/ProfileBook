from django.urls import path
from . import views
app_name = 'user'
urlpatterns=[
    path('view',views.BlogView.as_view(),name='blog' )

]