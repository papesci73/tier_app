from django.db.models import F
from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from shorter_api import serializers, models
from rest_framework.permissions import IsAuthenticated
from shorter_api import models
from shorter_api import permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


class UserLoginApiView(ObtainAuthToken):
    """Provide Oauth token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


# Create your views here.
class ShorterApiView(ModelViewSet):
    """ API for the Shorter test"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ShorterUrlSerializer
    queryset = models.ShorterModelItem.objects.all()
    permission_classes = (
        permissions.ReadOwnShorter,
        IsAuthenticated
    )

    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user)

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(user_profile=self.request.user)
        return query_set


class ShorterApiPublicView(ModelViewSet):
    """ API for the Shorter test"""
    serializer_class = serializers.ShorterPublicUrlSerializer
    queryset = models.ShorterModelItem.objects.all()
    http_method_names = ['get']
    permission_classes = (
        permissions.ReadPublicShorter,
    )

    def list(self, request, *args, **kwargs):
        response = {'message': 'List function is not offered in this path.'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        models.ShorterModelItem.objects.filter(pk=instance.id).update(hits=F('hits') + 1)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
