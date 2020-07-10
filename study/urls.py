from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('blog_study', views.blog_study, name='blog_study'),
    path('blog_add', views.blog_add, name='blog_add'),
    path('blog_submit', views.blog_submit, name='blog_submit'),
    path('blog_delete/<int:pk>', views.blog_delete, name='blog_delete'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('blog/<int:pk>', views.blog, name='blog'),
    path('blog_edit/<int:pk>', views.blog_edit, name='blog_edit'),
    path('blog_delete/<int:pk>', views.blog_delete, name='blog_delete'),
    path('blog_update/<int:pk>', views.blog_update, name='blog_update'),
]