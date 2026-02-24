from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Task


class TaskAPITestCase(TestCase):

    def setUp(self):
        """Set up test data before each test."""
        self.client = APIClient()

        # Create two test users
        self.user1 = User.objects.create_user(
            username='testuser1',
            password='testpass123'
        )
        self.user2 = User.objects.create_user(
            username='testuser2',
            password='testpass123'
        )

        # Create a task for user1
        self.task = Task.objects.create(
            title='Test Task',
            description='Test Description',
            user=self.user1
        )

    def get_token(self, username, password):
        """Helper to get JWT token."""
        response = self.client.post('/api/auth/login/', {
            'username': username,
            'password': password
        })
        return response.data['tokens']['access']

    # ===== REGISTRATION TESTS =====
    def test_register_user(self):
        """Test that a new user can register."""
        response = self.client.post('/api/auth/register/', {
            'username': 'newuser',
            'email': 'new@test.com',
            'password': 'newpass123'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], 'User registered successfully!')

    def test_register_duplicate_username(self):
        """Test that duplicate username fails."""
        response = self.client.post('/api/auth/register/', {
            'username': 'testuser1',
            'password': 'testpass123'
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # ===== LOGIN TESTS =====
    def test_login_success(self):
        """Test that a user can login."""
        response = self.client.post('/api/auth/login/', {
            'username': 'testuser1',
            'password': 'testpass123'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('tokens', response.data)

    def test_login_wrong_password(self):
        """Test that wrong password fails."""
        response = self.client.post('/api/auth/login/', {
            'username': 'testuser1',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # ===== TASK TESTS =====
    def test_create_task(self):
        """Test that a logged in user can create a task."""
        token = self.get_token('testuser1', 'testpass123')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        response = self.client.post('/api/tasks/', {
            'title': 'New Task',
            'description': 'New Description'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'New Task')

    def test_get_all_tasks(self):
        """Test that a user can get all their tasks."""
        token = self.get_token('testuser1', 'testpass123')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_task(self):
        """Test that a user can get a single task."""
        token = self.get_token('testuser1', 'testpass123')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        response = self.client.get(f'/api/tasks/{self.task.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Task')

    def test_update_task(self):
        """Test that a user can update their task."""
        token = self.get_token('testuser1', 'testpass123')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        response = self.client.put(f'/api/tasks/{self.task.id}/', {
            'title': 'Updated Task'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Task')

    def test_delete_task(self):
        """Test that a user can delete their task."""
        token = self.get_token('testuser1', 'testpass123')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        response = self.client.delete(f'/api/tasks/{self.task.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_mark_task_complete(self):
        """Test that a user can mark a task as complete."""
        token = self.get_token('testuser1', 'testpass123')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        response = self.client.post(f'/api/tasks/{self.task.id}/complete/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['task']['status'], 'complete')

    def test_mark_task_incomplete(self):
        """Test that a user can mark a task as incomplete."""
        token = self.get_token('testuser1', 'testpass123')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        response = self.client.post(f'/api/tasks/{self.task.id}/incomplete/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['task']['status'], 'pending')

    def test_user_cannot_see_other_users_tasks(self):
        """Test that a user cannot see another user's tasks."""
        token = self.get_token('testuser2', 'testpass123')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        response = self.client.get(f'/api/tasks/{self.task.id}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_filter_tasks_by_status(self):
        """Test that a user can filter tasks by status."""
        token = self.get_token('testuser1', 'testpass123')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        response = self.client.get('/api/tasks/?status=pending')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_task_without_login(self):
        """Test that a user cannot create a task without logging in."""
        response = self.client.post('/api/tasks/', {
            'title': 'New Task'
        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)