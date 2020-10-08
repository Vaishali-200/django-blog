from rest_framework import status
from rest_framework.generics import (CreateAPIView,GenericAPIView,ListAPIView)
from  rest_framework.response import Response
from .serializers import (UserSignUpSerializer,
                          UserLoginSerializer)
from .models import User
# Create your views here.
# class HelloWorld(APIView):
#     def get(self,request):
#         return Response("Hello World")

class UserSignUpAPIView(CreateAPIView):
    serializer_class = UserSignUpSerializer

    def post(self, request, *args, **kwargs):
        print("REQUEST DATA",request.data)
        serializer=self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            obj=User.objects.get(email=request.data["email"])

            response_data={
                "id":obj.id,
                "first_name":obj.first_name,
                "last_name":obj.last_name,
                "email":obj.email,
                "username":obj.username
            }
            return Response(response_data,status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

class GetUserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignUpSerializer

    # def get_queryset(self):
        # return User.objects.filter(is_superuser=False)

    def get(self, request, *args, **kwargs):
        serializer=super().list(request,*args,**kwargs)
        print("SERIALIZER",serializer.data)
        return Response(serializer.data)


class UserLoginAPIView(GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        print("REQUEST DATA",request.data)
        serializer=self.get_serializer(data=request.data)

        if serializer.is_valid():
            obj=serializer.user

            response_data={
                "id":obj.id,
                "first_name":obj.first_name,
                "last_name":obj.last_name,
                "email":obj.email,
                "username":obj.username
            }
            return Response(response_data)
        else:
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

