from django.contrib import admin

# Register your models here.
from profiles_api.models import UserProfile, ProfileFeedItem

admin.site.register(UserProfile)
admin.site.register(ProfileFeedItem)