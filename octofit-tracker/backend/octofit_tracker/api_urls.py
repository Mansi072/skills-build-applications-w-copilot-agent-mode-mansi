from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, TeamViewSet, ActivityViewSet, WorkoutViewSet, LeaderboardViewSet

from rest_framework.response import Response
from rest_framework.decorators import api_view
import os

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'workouts', WorkoutViewSet)
router.register(r'leaderboards', LeaderboardViewSet)

@api_view(['GET'])
def api_root(request, format=None):
    codespace_name = os.environ.get('CODESPACE_NAME')
    if codespace_name:
        base_url = f'https://{codespace_name}-8000.app.github.dev/api/'
        return Response({
            'users': base_url + 'users/',
            'teams': base_url + 'teams/',
            'activities': base_url + 'activities/',
            'workouts': base_url + 'workouts/',
            'leaderboards': base_url + 'leaderboards/',
        })
    else:
        return Response({
            'users': request.build_absolute_uri('users/'),
            'teams': request.build_absolute_uri('teams/'),
            'activities': request.build_absolute_uri('activities/'),
            'workouts': request.build_absolute_uri('workouts/'),
            'leaderboards': request.build_absolute_uri('leaderboards/'),
        })

urlpatterns = [
    path('', api_root, name='api-root'),
    path('', include(router.urls)),
]
