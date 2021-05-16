from django.contrib import admin
from django.urls import path, include
from FoodIndex import views
from FoodIndex.views import *
from django.conf.urls.static import static
from django.conf import settings
from home_app import views as hviews
from basic_app import views as bviews
app_name='FoodIndex'
urlpatterns = [
    path('upload_csv', views.upload_csv, name='upload_csv'),    
    path('filetodb', views.file_to_db, name='filetodb'),
    path('addfood', views.addfood, name='addfood'),
    path('getdata', views.getdata, name='getdata'),
    path('admin_login', views.login, name='login'),
    path('admin_signup', views.signup, name='signup'),
    path('alreadyuser', views.abc, name='alreadyuser'),
    path('base_table', views.base_table, name='base_table'),
    path('upload_csv_', views.xyz, name='upload_csv_'),
    path('user_signup', views.user_signup, name='user_signup'),
    path('base', views.base_page, name='base'),
    path('home', hviews.home, name='home'),
    path('north', bviews.north, name='north'),
    path('continental', bviews.continental, name='continental'),
    path('south', bviews.south, name='south'),
    path('chinese', bviews.chinese, name='chinese'),
    path('dessert', bviews.dessert, name='dessert'),
    path('table', hviews.table, name='table'),
    path('purchase', hviews.purchase, name='purchase'),
    path('', views.user_login, name='user_login'),
    path('usertodb', views.user_to_database, name="usertodb"),
    path('profile_page',hviews.profile_page,name='profile_page'),
    path('search',bviews.search,name='search'),
    path('delete/<str:food_id>',views.delete_book,name="delete"),
    path('chart',hviews.chart,name='chart'),
	
	path('calchartthree',hviews.calchartthree,name='calchartthree'),
    path('update/<str:food_id>', views.update_food, name='update'),
    path('update_userdata/<str:email>', views.updata_userdata, name='update_userdata'),
    path('delete_table', views.delete_table, name='delete_table')


    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_URL)

