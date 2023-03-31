from django.shortcuts import render
from rest_framework import generics,viewsets
from .models import Myquize, Category
from .serializers import MyquizeSerializer
from rest_framework.views import APIView
from rest_framework. response import Response
from django. forms import model_to_dict
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly , IsAdminUser
from .permissions import IsAdminOrReadOnly,IsOwnerOrReadOnly
class MyquizeAPIList (generics .ListCreateAPIView):
    queryset = Myquize.objects.all()
    serializer_class = MyquizeSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
class MyquizeAPIUpdate (generics. RetrieveUpdateAPIView):
    queryset = Myquize. objects.all()
    serializer_class = MyquizeSerializer
    permission_classes = (IsOwnerOrReadOnly,)
class MyquizeAPIDestroy (generics .RetrieveDestroyAPIView):
    queryset = Myquize.objects.all()
    serializer_class = MyquizeSerializer
    permission_classes = (IsAdminOrReadOnly,)




# class MyquizeViewSet(viewsets.ModelViewSet):
#     # queryset = Myquize.objects.all()
#     serializer_class = MyquizeSerializer
#     def get_queryset(self):
#         pk=self.kwargs.get('pk')
#         if not pk:
#             return Myquize.objects.all()
#         return Myquize.objects.filter(pk=pk)
#     @action(methods=['get'],detail = True)
#     def category (self,request,pk=None):
#         cats = Category.objects.get(pk=pk)
#         return Response({'cats': cats.name})



# class MyquizeAPIList(generics.ListCreateAPIView):
#     queryset = Myquize.objects.all()
#     serializer_class = MyquizeSerializer
# class MyquizeAPIUpdate(generics.UpdateAPIView):
#     queryset = Myquize.objects.all()
#     serializer_class = MyquizeSerializer
# class MyquizeAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Myquize.objects.all()
#     serializer_class = MyquizeSerializer
# class MyquizeAPIView(APIView):
#     def get(self,request):
#         Myquize_list = Myquize.objects.all()
#         return Response({"posts":MyquizeSerializer(Myquize_list, many=True).data})
#     def post(self,request):
#         serializer = MyquizeSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post":serializer.data})
#     def put(self,request,*args,**kwargs):
#         pk = kwargs.get('pk',None)
#         if not pk:
#             return Response({"error":"Method PUT not allowed"})
#         try:
#             instance = Myquize.objects.get(pk=pk)
#         except:
#             return Response({"error": "Objects does not exists"})
#         serializer = MyquizeSerializer(data=request.data,instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post":serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})
#         try:
#             delete_record = Myquize.objects.get(pk=pk)
#             delete_record.delete()
#         except:
#             return Response({"error": "Object does not exists"})
#
#         return Response({"post": "delete post " + str(pk)})