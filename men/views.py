from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Men, Category
from .serializers import MenSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action # 9
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated # 10
from men.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.pagination import PageNumberPagination


class MenAPIListPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 3


# 10 #11 #12
class MenAPIList(generics.ListCreateAPIView):
    queryset = Men.objects.all()
    serializer_class = MenSerializer
    permission_classes = (IsAuthenticated, )
    # authentication_classes = (TokenAuthentication, )
    # authentication_classes = (BasicAuthentication, SessionAuthentication, )
    # authentication_classes = (JWTAuthentication, )
    pagination_class = MenAPIListPagination

class MenAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Men.objects.all()
    serializer_class = MenSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class MenAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Men.objects.all()
    serializer_class = MenSerializer
    permission_classes = (IsAdminOrReadOnly, )


# class MenAPIDestroy(generics.RetrieveDestroyAPIView):
#     queryset = Men.objects.all()
#     serializer_class = MenSerializer
#     permission_classes = (IsAdminUser,)


##################################################################

# 9
# class MenViewSet(mixins.CreateModelMixin,
#                    mixins.RetrieveModelMixin,
#                    mixins.UpdateModelMixin,
#                    mixins.DestroyModelMixin,
#                    mixins.ListModelMixin,
#                    GenericViewSet):
    # queryset = Men.objects.all()
    # serializer_class = MenSerializer

    # def get_queryset(self):
    #     pk = self.kwargs.get('pk')

    #     if not pk:
    #         return Men.objects.all()[:3]

    #     return Men.objects.filter(pk =pk)


    # @action(methods=['get'], detail = True)
    # def category(self, request, pk = None):
    #     cats = Category.objects.get(pk=pk)
    #     return Response({'cats': cats.name})
    
    # @action(methods=['get'], detail = True)
    # def category(self, request, pk=None):
    #     try:
    #         pk = Men.objects.get(pk=pk).cat_id
    #         cats = Category.objects.get(pk=pk)
    #         return Response({'cats': cats.name})
    #     except:
    #         return Response({'Post': 'object not followed'})

    # @action(methods=['get'], detail = False)
    # def category(self, request):
    #     cats = Category.objects.all()
    #     return Response({'cats': [c.name for c in cats]})



####################################################################
# 8
# class MenViewSet(viewsets.ModelViewSet):
#     queryset = Men.objects.all()
#     serializer_class = MenSerializer

# class MenViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Men.objects.all()
#     serializer_class = MenSerializer


# class MenViewSet(mixins.CreateModelMixin,
#                    mixins.RetrieveModelMixin,
#                    mixins.UpdateModelMixin,
#                    mixins.DestroyModelMixin,
#                    mixins.ListModelMixin,
#                    GenericViewSet):
#     queryset = Men.objects.all()
#     serializer_class = MenSerializer





#########################################################

# 7
# class MenAPIList(generics.ListCreateAPIView):
#     queryset = Men.objects.all()
#     serializer_class = MenSerializer

# class MenAPIUpdate(generics.UpdateAPIView):
#     queryset = Men.objects.all()
#     serializer_class = MenSerializer


# class MenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Men.objects.all()
#     serializer_class = MenSerializer

############################################################################

# 6
# class MenAPIView(APIView):
#     def get(self, request):
#         w = Men.objects.all()
#         return Response({'posts': MenSerializer(w, many= True).data})
    

#     def post(self, request):
#         serializer = MenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response({'post': serializer.data})
    
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
        
#         try:
#             instance = Men.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exists"})
        
#         serializer = MenSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})
    

#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})
        
#         try:
#             instance = Men.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exists"})
        
#         instance.delete()
       
#         return Response({"post": "delete post" + str(pk)})  




####################################################################################

# 5
# class MenAPIView(APIView):
#     def get(self, request):
#         w = Men.objects.all()
#         return Response({'posts': MenSerializer(w, many= True).data})
    

#     def post(self, request):
#         serializer = MenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response({'post': serializer.data})
    
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
        
#         try:
#             instance = Men.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exists"})
        
#         serializer = MenSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})
    

#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})
        
#         try:
#             instance = Men.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exists"})
        
#         instance.delete()
       
#         return Response({"post": "delete post" + str(pk)})  
        



############################################################################

# 4
# class MenAPIView(APIView):
#     def get(self, request):
#         w = Men.objects.all()
#         return Response({'posts': MenSerializer(w, many= True).data})
    

#     def post(self, request):
#         serializer = MenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         post_new = Men.objects.create(
#         title = request.data['title'],
#         content = request.data['content'],
#         cat_id = request.data['cat_id']
#     )
#         return Response({'post': MenSerializer(post_new).data})



##########################################################################

# 2
# class MenAPIView(APIView):
    # def get(self, request):
    #     lst = Men.objects.all().values()
    #     return Response({'posts': list(lst)})
    

    # def post(self, request):
    #     post_new = Men.objects.create(
    #         title = request.data['title'],
    #         content = request.data['content'],
    #         cat_id = request.data['cat_id']
    #     )

    #     return Response({'post': model_to_dict(post_new)})
        


#######################################################################

# 1
# class MenAPIView(APIView):
    # def get(self, request):
    #     return Response({'title': 'Cristiano Ronaldo'})


    # def post(self,request):
    #     return Response({'title': 'Lionel Messi'})




