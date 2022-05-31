from django.urls import path
from regdepartment import views

urlpatterns = [
    path("",views.land,name="land"),
    path("index/",views.index,name="index"),
    # path("showdata/",views.showdata,name="showdata"),
    path("userdel/<int:id>/",views.userdel,name="userdel"),
    path("userupdate/<int:id>/",views.userupdate,name="userupdate"),
]
