
from django.urls import path

from .views import ListView, DetailView, CategoryView, SubCategoryView

urlpatterns = [
    # path('/list', ListView.as_view()),
    path('/category/<int:category_id>', CategoryView.as_view()),
    path('/sub_category/<int:sub_category_id>', SubCategoryView.as_view()),
    # path('/detail', DetailView.as_view()),
    path('/<int:product_id>', DetailView.as_view())
]
