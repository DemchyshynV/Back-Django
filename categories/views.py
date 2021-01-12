from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from categories.models import ProductCategoriesModel, SubProductCategoriesModel
from categories.serializers import ProductCategoriesSerializer, ProductSubCategoriesSerializer


class ProductCategoriesView(APIView):
    serializer_class = ProductCategoriesSerializer

    def get(self, request):
        category = ProductCategoriesModel.objects.all()
        data = ProductCategoriesSerializer(category, many=True).data
        return Response(data, status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductCategoriesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class EditProductCategoriesView(APIView):
    serializer_class = ProductCategoriesSerializer

    def put(self, *args, **kwargs):
        pk = kwargs.get('pk')
        data = self.request.data

        category = get_object_or_404(ProductCategoriesModel, pk=pk)
        serializer = ProductCategoriesSerializer(category, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        get_object_or_404(ProductCategoriesModel, pk=pk).delete()
        return Response({'msg': 'Category deleted'}, status.HTTP_200_OK)


class ProductSubCategoriesView(APIView):
    serializer_class = ProductSubCategoriesSerializer

    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        qs = SubProductCategoriesModel.objects.filter(categories_id=pk)
        sub_categories = ProductSubCategoriesSerializer(qs, many=True).data
        return Response(sub_categories, status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        serializer = ProductSubCategoriesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(categories_id=pk)
        return Response(serializer.data, status.HTTP_201_CREATED)


class EditSubProductCategoriesView(APIView):
    serializer_class = ProductSubCategoriesSerializer

    def put(self, *args, **kwargs):
        pk = kwargs.get('pk')
        data = self.request.data
        sub_category = get_object_or_404(SubProductCategoriesModel, pk=pk)
        serializer = ProductSubCategoriesSerializer(sub_category, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        get_object_or_404(SubProductCategoriesModel, pk=pk).delete()
        return Response({'msg': 'Subcategory deleted'})
