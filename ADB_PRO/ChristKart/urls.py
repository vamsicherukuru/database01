from django.urls import path
from ChristKart import views

app_name = 'ChristKart'

urlpatterns=[
path('',views.index.as_view(),name='home'),
path('plates',views.plates.as_view(),name='plates'),
path('straws',views.straws.as_view(),name='straws'),
path('bags',views.bags.as_view(),name='bags'),
path('register',views.registerView,name='register'),
path('user_login',views.user_login,name='user_login'),
path('user_logout',views.user_logout,name='user_logout'),

]
