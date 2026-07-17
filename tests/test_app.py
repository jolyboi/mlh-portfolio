import os
import unittest

os.environ["TESTING"] = "true"

from app import TimelinePost, app


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        TimelinePost.delete().execute()

    def test_home(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

        html = response.get_data(as_text=True)
        self.assertIn("<title>MLH Fellows</title>", html)
        self.assertIn("<h1>MLH Fellows</h1>", html)
        self.assertIn("<h2>About Me</h2>", html)
        self.assertIn("<h2>Work Experience</h2>", html)
        self.assertIn("<h2>Education</h2>", html)
        self.assertIn("Ghadi", html)
        self.assertIn("Andrei", html)

    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.is_json)
        self.assertEqual(response.get_json(), {"timeline_posts": []})

        response = self.client.post(
            "/api/timeline_post",
            data={
                "name": "John Doe",
                "email": "john@example.com",
                "content": "Hello world, I'm John!",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.is_json)
        created_post = response.get_json()
        self.assertEqual(created_post["id"], 1)
        self.assertEqual(created_post["name"], "John Doe")
        self.assertEqual(created_post["email"], "john@example.com")
        self.assertEqual(created_post["content"], "Hello world, I'm John!")
        self.assertIn("created_at", created_post)

        response = self.client.get("/api/timeline_post")
        self.assertEqual(response.status_code, 200)
        timeline_posts = response.get_json()["timeline_posts"]
        self.assertEqual(len(timeline_posts), 1)
        self.assertEqual(timeline_posts[0], created_post)

        response = self.client.get("/timeline")
        self.assertEqual(response.status_code, 200)
        html = response.get_data(as_text=True)
        self.assertIn("<title>Timeline</title>", html)
        self.assertIn("<h2>Add a Post</h2>", html)
        self.assertIn('id="timeline-form"', html)
        self.assertIn('id="timeline-posts"', html)
        self.assertIn("fetch('/api/timeline_post')", html)

    def test_malformed_timeline_post(self):
        response = self.client.post(
            "/api/timeline_post",
            data={
                "email": "john@example.com",
                "content": "Hello world, I'm John!",
            },
        )
        self.assertEqual(response.status_code, 400)
        html = response.get_data(as_text=True)
        self.assertIn("Invalid name", html)

        response = self.client.post(
            "/api/timeline_post",
            data={
                "name": "John Doe",
                "email": "john@example.com",
                "content": "",
            },
        )
        self.assertEqual(response.status_code, 400)
        html = response.get_data(as_text=True)
        self.assertIn("Invalid content", html)

        response = self.client.post(
            "/api/timeline_post",
            data={
                "name": "John Doe",
                "email": "not-an-email",
                "content": "Hello world, I'm John!",
            },
        )
        self.assertEqual(response.status_code, 400)
        html = response.get_data(as_text=True)
        self.assertIn("Invalid email", html)
