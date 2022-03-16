from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from user.models import User
from .serializers import UserSerializer


class UserListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        Login for returning user
        """
        users = User.objects.filter(user=request.user.id)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        Create new user - Signup
        """
        data = {
            "user": request.data.get("user"),
            "jhed_id": request.data.get("jhed_id"),
            "jhed_email": request.data.get("jhed_email"),
            "class_year": request.data.get("class_year"),
            "preferred_name": request.data.get("preferred_name"),
            "is_admin": request.data.get("is_admin"),
        }

        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
