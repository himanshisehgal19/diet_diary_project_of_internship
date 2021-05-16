from django.urls import path,include
from home_app import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
app_name='home_app'


urlpatterns=[
	path('home/',views.home,name='home'),
	#path('renderhome/',views.renderhome, name='renderhome'),
	path('details/<str:f_name>/', views.details, name='details'),
    path('add_item1/', views.add_item1, name='add_item1'),
	path('delete/<str:f_name>/', views.delete, name='delete'),
	path('delete_purchase/<str:f_id>/', views.delete_purchase, name='delete_purchase'),
	path('table/', views.table, name='table'),
	path('purchase/', views.purchase, name='purchase'),
	path('confirm_purchase/', views.confirm_purchase, name='confirm_purchase'),
	path('confirm_purchase2/', views.confirm_purchase2, name='confirm_purchase2'),
	path('save_table/', views.save_table, name='save_table'),
	path('save_purchase/', views.save_purchase, name='save_purchase'),
	path('deletetemp/',views.deletetemp, name='deletetemp'),
	path('calories/',views.calories,name='calories'),
	path('chart',views.chart,name='chart'),
	
	path('calchartthree',views.calchartthree,name='calchartthree'),
    path('', views.homex, name='homex'),
	path('profile_page/',views.profile_page,name='profile_page')
   # path('population_chart/', views.population_chart, name='population_chart'),


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)