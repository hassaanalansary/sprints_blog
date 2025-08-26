from django.test import TestCase

class TestBlogViews(TestCase):
    def test_blog_season_success(self):
        # Arrange

        # Act
        response = self.client.get("/blog/winter/")

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "❄️ Winter")
        self.assertContains(response, "A hush falls over the world")
        self.assertTemplateUsed(response, "blog/season.html")

    def test_blog_season_when_season_does_not_exist_should_return_404(self):
        # Arrange

        # Act
        response = self.client.get("/blog/march/")
        
        # Assert
        self.assertEqual(response.status_code, 404)
    def test_blog_season_by_number_success(self):
        # Arrange

        # Act
        response = self.client.get("/blog/1/")

        # Assert
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.headers['Location'], '/blog/winter/')

    def test_blog_season_by_number_when_season_does_not_exist_should_return_404(self):
        # Arrange

        # Act
        response = self.client.get("/blog/4/")
        
        # Assert
        self.assertEqual(response.status_code, 404)
        
    
    def test_blog_home_returns_seasons_list(self):
        # Arrange

        # Act
        response = self.client.get("/blog/")

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<a href="/blog/winter/"')
        self.assertContains(response, '<a href="/blog/fall/"')
        self.assertContains(response, '<a href="/blog/spring/"')
        self.assertContains(response, '<a href="/blog/summer/"')
        self.assertTemplateUsed(response, "blog/home.html")