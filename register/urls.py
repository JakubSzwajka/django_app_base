from django.urls import path, include
from . import views

app_name = 'register'
urlpatterns = [
    path('edit_profile_page/', views.edit_user_page, name='edit_profile_page'),   
    path('view_profile_page/', views.View_User_Page.as_view(), name='view_user_page'),
]



