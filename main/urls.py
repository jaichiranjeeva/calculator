from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('eq',views.eq,name='eq'),
    path('ac',views.ac,name='ac'),
    path('bs',views.bs,name='bs'),
    path('inp',views.input,name='inp'),
    path('evalute',views.equate,name='evalute')
]
