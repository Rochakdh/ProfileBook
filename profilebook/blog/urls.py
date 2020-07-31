from django.urls import path
from . import views
app_name = 'blog'

urlpatterns=[
    path('view/',views.BlogView.as_view(),name='blog'),
    # path('update/<int:pk>/',views.BlogUpdateView.as_view(),name='updatedetail'),
    path('create/',views.BlogCreate.as_view(),name='create'),
    path('update/<int:pk>/',views.BlogUpdate.as_view(),name='update'),
    path('delete/<int:pk>/',views.BlogDelete.as_view(),name='delete'),
    path('detail/<int:pk>/',views.AllBlogDetail.as_view(),name='blog-detail')
]