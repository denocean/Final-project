	def test_post_edit_permission(self):
		# Only author can edit
		self.client.login(username='testuser', password='testpass123')
		response = self.client.get(reverse('blog:post_edit', kwargs={'slug': self.post.slug}))
		self.assertEqual(response.status_code, 200)
		# Another user should not be able to edit
		other_user = get_user_model().objects.create_user(username='otheruser', password='otherpass123')
		self.client.login(username='otheruser', password='otherpass123')
		response = self.client.get(reverse('blog:post_edit', kwargs={'slug': self.post.slug}))
		self.assertEqual(response.status_code, 403)

	def test_post_delete_permission(self):
		# Only author can delete
		self.client.login(username='testuser', password='testpass123')
		response = self.client.get(reverse('blog:post_delete', kwargs={'slug': self.post.slug}))
		self.assertEqual(response.status_code, 200)
		# Another user should not be able to delete
		other_user = get_user_model().objects.create_user(username='otheruser2', password='otherpass123')
		self.client.login(username='otheruser2', password='otherpass123')
		response = self.client.get(reverse('blog:post_delete', kwargs={'slug': self.post.slug}))
		self.assertEqual(response.status_code, 403)

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Post

class BlogViewTests(TestCase):
	def setUp(self):
		self.user = get_user_model().objects.create_user(username='testuser', password='testpass123')
		self.post = Post.objects.create(
			title='Test Post',
			slug='test-post',
			author=self.user,
			content='Test content.'
		)
		self.client = Client()

	def test_post_list_view(self):
		response = self.client.get(reverse('blog:post_list'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Test Post')

	def test_post_detail_view(self):
		response = self.client.get(reverse('blog:post_detail', kwargs={'slug': self.post.slug}))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Test content.')

	def test_post_create_view_requires_login(self):
		response = self.client.get(reverse('blog:post_create'))
		self.assertNotEqual(response.status_code, 200)
		self.client.login(username='testuser', password='testpass123')
		response = self.client.get(reverse('blog:post_create'))
		self.assertEqual(response.status_code, 200)

	def test_post_create_form(self):
		self.client.login(username='testuser', password='testpass123')
		response = self.client.post(reverse('blog:post_create'), {
			'title': 'Another Post',
			'slug': 'another-post',
			'content': 'More content.'
		})
		self.assertEqual(Post.objects.count(), 2)
		self.assertRedirects(response, reverse('blog:post_list'))
