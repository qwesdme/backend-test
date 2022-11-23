from classes.post import Post
from configs.endpoints import posts_url
from handlers.comment_handler import CommentHandler
from helpers.request import data_dict


class PostHandler:
    def __init__(self):
        self._posts: dict[int, Post] = {}
        self._comment_handler = CommentHandler()
        self._load()

    def _load(self):
        for post_data in data_dict(posts_url):
            user_id: int = post_data[Post.user_id_external_str]
            post_id: int = post_data[Post.id_external_str]
            title: str = post_data[Post.title_external_str]
            body: str = post_data[Post.body_external_str]
            comment_count: int = self._comment_handler.count_comment(post_id)

            post: Post = Post(user_id=user_id, post_id=post_id, title=title, body=body, comment_count=comment_count)
            self._posts[post_id] = post

    def posts(self, return_type: str = "dict") -> dict[int, Post] | list[Post]:
        if return_type == "dict":
            return self._posts
        elif return_type == "list":
            list_post: list[Post] = list(self._posts.values())
            return list_post

    def response_data(self, post_id) -> dict[str, int | str] | None:
        post = self._posts[post_id]
        if post:
            return post.response_data()
        else:
            return None
