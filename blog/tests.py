from django.test import TestCase
from blog.models import Post
from users.models import User


class TestBlogViews(TestCase):
    def test_blog_post_success(self):
        # Arrange
        user = User.objects.create(name="test", email="test@test.com", username="test")
        Post.objects.create(
            title="Winter", body="❄️ Winter \n A hush falls over the world ", author=user
        )

        # Act
        response = self.client.get("/blog/winter/")

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "❄️ Winter")
        self.assertContains(response, "A hush falls over the world")
        self.assertTemplateUsed(response, "blog/post.html")

    def test_blog_post_when_post_does_not_exist_should_return_404(self):
        # Arrange

        # Act
        response = self.client.get("/blog/march/")

        # Assert
        self.assertEqual(response.status_code, 404)

    def test_blog_post_by_number_success(self):
        # Arrange
        user = User.objects.create(name="test", email="test@test.com", username="test")
        post = Post.objects.create(
            title="Winter", body="❄️ Winter \n A hush falls over the world ", author=user
        )

        # Act
        response = self.client.get(f"/blog/{post.id}/")

        # Assert
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.headers["Location"], "/blog/winter/")

    def test_blog_post_by_number_when_post_does_not_exist_should_return_404(self):
        # Arrange

        # Act
        response = self.client.get("/blog/4/")

        # Assert
        self.assertEqual(response.status_code, 404)

    def test_blog_home_returns_posts_list(self):
        # Arrange
        user = User.objects.create(name="test", email="test@test.com", username="test")
        Post.objects.create(title="Winter", author=user)
        Post.objects.create(title="fall", author=user)
        Post.objects.create(title="spring", author=user)
        Post.objects.create(title="summer", author=user)

        # Act
        response = self.client.get("/blog/")

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<a href="/blog/winter/"')
        self.assertContains(response, '<a href="/blog/fall/"')
        self.assertContains(response, '<a href="/blog/spring/"')
        self.assertContains(response, '<a href="/blog/summer/"')
        self.assertTemplateUsed(response, "blog/home.html")
