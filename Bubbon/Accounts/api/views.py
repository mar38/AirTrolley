from rest_framework.generics import ListAPIView, RetrieveAPIView
from Accounts.models import Member
from .serializer import UserLoginSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView


class UserLoginAPIView (APIView):
    queryset = Member.objects.all()
    serializer_class =UserLoginSerializer
    def post (self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer (data=data)
        if serializer.is_valid(raise_exception=True):

            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)