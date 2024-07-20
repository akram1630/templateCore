
from django.contrib import admin
from django.urls import path, include
from django.http.response import HttpResponse


#only me
def homeFunc(request):
  return HttpResponse('<h6>HOME</h6>')


urlpatterns = [
    path('', homeFunc),
    path('admin/', admin.site.urls),
    # we declare only student/...edit...add.....
    path('student/', include('student.urls')),
]
