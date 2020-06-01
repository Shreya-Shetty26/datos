from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class DataSourceApiView(APIView) :
    def get(self,request):
        return Response(
            data="Get method worked"
        )

    def post(self, request):
        return Response(
            data="Post method worked"
        )
