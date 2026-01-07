from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team', description='A test team')
        self.user = User.objects.create(email='test@example.com', name='Test User', team=self.team)
        self.workout = Workout.objects.create(name='Test Workout', description='A test workout')
        self.activity = Activity.objects.create(user=self.user, activity_type='Test Activity', duration_minutes=30, date='2026-01-01')
        self.leaderboard = Leaderboard.objects.create(team=self.team, total_points=100, week='2026-01-01')

    def test_user_creation(self):
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertEqual(self.user.team, self.team)

    def test_team_creation(self):
        self.assertEqual(self.team.name, 'Test Team')

    def test_workout_creation(self):
        self.assertEqual(self.workout.name, 'Test Workout')

    def test_activity_creation(self):
        self.assertEqual(self.activity.activity_type, 'Test Activity')

    def test_leaderboard_creation(self):
        self.assertEqual(self.leaderboard.total_points, 100)
