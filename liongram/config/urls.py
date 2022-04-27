
from django.contrib import admin
from django.urls import path

from posts.views import url_view, url_parameter_view, function_view, class_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('url/', url_view),
    path('url/<str:username>/', url_parameter_view),
    path('fbv/', function_view),
    path('cbv/', class_view.as_view()),
]
