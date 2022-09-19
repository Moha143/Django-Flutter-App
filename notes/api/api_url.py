from django.urls import path
from . import views
urlpatterns = [
    path('', views.getRoutes),
    path('notes/', views.getNotes),
    path('notes/create/', views.CreateNote),
    path('notes/<str:id>', views.getNote),
    path('notes/<str:id>/update/', views.UpdateNote),
    path('notes/<str:id>/delete/', views.DeleteNote),

]
