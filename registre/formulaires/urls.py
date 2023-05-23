from django.urls import path
from . import views

urlpatterns =[
    path('form1',views.identification, name="form1"),
    path('form2',views.spirituel, name= 'form2'),
    path('form3',views.education, name="form3"),
    path('form4',views.professionel, name="form4"),
    path('error_404',views.error_404, name="error_404"),
    path('success',views.success, name='success')
]