from django.urls import path
from . import views
app_name = 'blog'

urlpatterns=[
    path('view/',views.BlogView.as_view(),name='blog'),
    path('update/<int:pk>/',views.BlogUpdate.as_view(),name='update'),
    path('delete/<int:pk>/',views.BlogDelete.as_view(),name='delete')
]