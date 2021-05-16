from django.urls import path,include
from basic_app import views 
from django.conf.urls import url

app_name='basic_app'

urlpatterns=[
   path('food/',views.food,name='food'),
   path('north/',views.north,name='north'),
   path('south/',views.south,name='south'),
   path('chinese/',views.chinese,name='chinese'),
   path('dessert/',views.dessert,name='dessert'),
   path('search',views.search,name='search'),
   
]