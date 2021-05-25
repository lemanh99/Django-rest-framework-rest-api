from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from profiles_api.models import UserProfile, ProfileFeedItem
from profiles_api.permissions import UpdateOwnProfile
from profiles_api.serializers import UserProfileSerializer, ProfileFeedItemSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = ProfileFeedItemSerializer
    queryset = ProfileFeedItem.objects.all()

    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user)
