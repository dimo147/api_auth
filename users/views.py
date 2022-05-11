from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer
from rest_framework import permissions, generics
from .serializers import UserSerializer, RegisterSerializer
from django.contrib.auth.models import User

# Create your views here.

from .serializers import UserSerializer, GroupSerializer
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from .serializers import MyTokenObtainPairSerializer
from .serializers import RegisterSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

# def follow(id, user_id):
#     try:
#         PROFILES.update_one(
#             {'id' : id},
#         {
#             '$push': {
#                 'follower' : {'user_id' : user_id}
#             }
#         },
#         )
#         PROFILES.update_one(
#             {'id' : user_id},
#         {
#             '$push': {
#                 'following' : {'user_id' : id}
#             }
#         },
#         )
#     except Exception as e:
#         print('page unavailable')

# def unfollow(id, user_id):
#     try:
#         PROFILES.update_one(
#             {'id' : id},
#         {
#             '$pull': {
#                 'follower' : {'user_id' : user_id}
#             }
#         },
#         )
#         PROFILES.update_one(
#             {'id' : user_id},
#         {
#             '$pull': {
#                 'following' : {'user_id' : id}
#             }
#         },
#         )
#     except Exception as e:
#         print('page unavailable')

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

# class FollowView(APIView):
#     permission_classes = [IsAuthenticated]
   
#     def post(self, request):
#         try:
#             id = request.query_params.get('id')
#             follow(int(id), request.user.id)
#             return Response({"state" : "done"})
#         except Exception as e:
#             return Response({"state" : "post unavailable"})

# class UnfollowView(APIView):
#     permission_classes = [IsAuthenticated]
   
#     def post(self, request):
#         try:
#             id = request.query_params.get('id')
#             unfollow(int(id), request.user.id)
#             return Response({"state" : "done"})
#         except Exception as e:
#             return Response({"state" : "post unavailable"})
