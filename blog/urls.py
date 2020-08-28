from django.urls import path
from .views import index,create,detail,update,delete


urlpatterns = [
    path('', index, name="index"),
    path('create/', create, name="create"),
    path('detail/<int:add_id>', detail, name="detail"),
    path('update/<int:add_id>', update, name="update"),
    path('delete/<int:add_id>', delete, name="delete"),
]
