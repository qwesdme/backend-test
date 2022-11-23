from flask import jsonify

from classes.post import Post
from configs.routes import posts_route
from handlers.post_handler import PostHandler
from resources.abstract import ResourceAbstract


class Posts(ResourceAbstract):
    route: str = posts_route

    # return a list of top posts ordered by their number of Comments
    def get(self):
        post_handler = PostHandler()

        posts: list[Post] = post_handler.posts(return_type="list")
        sorted_posts = sorted(posts, reverse=True)  # most number of comments first

        response_data_list: list[dict] = [post.response_data() for post in sorted_posts]

        return jsonify(response_data_list)
