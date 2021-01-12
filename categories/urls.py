from django.urls import path

from categories.views import ProductCategoriesView, EditProductCategoriesView, \
    EditSubProductCategoriesView, ProductSubCategoriesView

urlpatterns = [
    path('', ProductCategoriesView.as_view()),
    path('<int:pk>', EditProductCategoriesView.as_view()),

    path('<int:pk>/sub_categories', ProductSubCategoriesView.as_view()),
    path('sub_categories/<int:pk>', EditSubProductCategoriesView.as_view()),
]
