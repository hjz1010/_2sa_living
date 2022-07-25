
from django.urls import path

from .views import *

urlpatterns = [
    # # path('/list', ListView.as_view()),
    # path('/category/<int:category_id>', CategoryView.as_view()),
    # path('/sub_category/<int:sub_category_id>', SubCategoryView.as_view()),

    path('', ListView.as_view()),
    # 127.0.0.1:8000/products?category_id=2&page=2
    # 127.0.0.1:8000/products?sub_category_id=7&page=1
    # 127.0.0.1:8000/products?category_id=2&sub_category_id=7&page=1   ## 데이터 가공 시 sub_category_id만 필터링 함

    # path('/detail', DetailView.as_view()),
    path('/<int:product_id>', DetailView.as_view())
    # 127.0.0.1:8000/products/7    
    # 127.0.0.1:8000/products?product_id=7   

    
]
