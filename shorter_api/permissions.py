from rest_framework import permissions
import logging
logger = logging.getLogger(__name__)


class ReadOwnShorter(permissions.BasePermission):
    """"Permission to read all data"""

    def has_object_permission(self, request, view, obj):
        logger.warning(f'usr {request.user.id} obj {obj.user_profile.id}')
        return obj.user_profile.id == request.user.id


class ReadPublicShorter(permissions.BasePermission):
    """"Permission to read all data"""

    def has_object_permission(self, request, view, obj):
        return request.method in permissions.SAFE_METHODS


