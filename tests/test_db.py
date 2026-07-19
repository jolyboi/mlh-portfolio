import os
import unittest

from peewee import SqliteDatabase

os.environ["TESTING"] = "true"

from app import TimelinePost


MODELS = [TimelinePost]

# Use an in-memory SQLite database for tests.
test_db = SqliteDatabase(":memory:")


class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        # Bind model classes to the test db. Since we have a complete list of
        # all models, we do not need to recursively bind dependencies.
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)
        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        test_db.drop_tables(MODELS)
        test_db.close()

    def test_timeline_post(self):
        first_post = TimelinePost.create(
            name="John Doe",
            email="john@example.com",
            content="Hello world, I'm John!",
        )
        self.assertEqual(first_post.id, 1)

        second_post = TimelinePost.create(
            name="Jane Doe",
            email="jane@example.com",
            content="Hello world, I'm Jane!",
        )
        self.assertEqual(second_post.id, 2)

        timeline_posts = list(TimelinePost.select().order_by(TimelinePost.id))
        self.assertEqual(timeline_posts, [first_post, second_post])
        self.assertEqual(timeline_posts[0].name, "John Doe")
        self.assertEqual(timeline_posts[0].email, "john@example.com")
        self.assertEqual(timeline_posts[0].content, "Hello world, I'm John!")
        self.assertEqual(timeline_posts[1].name, "Jane Doe")
        self.assertEqual(timeline_posts[1].email, "jane@example.com")
        self.assertEqual(timeline_posts[1].content, "Hello world, I'm Jane!")
