from django.contrib import admin
from django.urls import path
from . import views
app_name='blog'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index',views.index,name='index'),
    path('article/<int:pk>/',views.article_page,name='article_page'),
    path('archives/<int:year>/<int:month>/',views.archives,name='archives'),
    path('categories/<int:pk>/',views.categories,name='categories')
]