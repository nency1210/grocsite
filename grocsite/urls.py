
from django.contrib import admin
from django.urls import include, path
from myapp1 import views
app_name = 'myapp1'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path("typeList/",views.type_list,name='typeList'),
    path('typelistcbv',views.TypeListView.as_view(),name="typelistcbv"),
    path('myapp1/<int:type_no>',views.detail,name='detail'),
    path('myapp1/about/<int:year>/<int:month>/', views.about, name='about'),
    # path('', include('myapp1.urls')),
]
