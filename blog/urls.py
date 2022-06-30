from django.urls import path
from blog.views import BlogView
from . import views

app_name="blog"

urlpatterns=[
    path('blog/', BlogView.as_view(), name="blog"),
    path('category/<int:category_id>/', views.category,name="category"),

]