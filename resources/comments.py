from flask import jsonify

from classes.comment import Comment
from configs.routes import comments_route
from handlers.comment_handler import CommentHandler
from helpers.get import get_int, get_str
from resources.abstract import ResourceAbstract


class Comments(ResourceAbstract):
    route: str = comments_route

    # filter the comments based on all the available fields
    def get(self):
        post_id_get_field_int: int | None = get_int(Comment.post_id_field_str)
        comment_id_get_field_int: int | None = get_int(Comment.comment_id_field_str)
        name_get_field_str: str | None = get_str(Comment.name_field_str)
        email_get_field_str: str | None = get_str(Comment.email_field_str)
        body_get_field_str: str | None = get_str(Comment.body_field_str)

        query_name_field_str: str | None = get_str(f"query_{Comment.name_field_str}")
        query_body_field_str: str | None = get_str(f"query_{Comment.body_field_str}")

        comment_handler = CommentHandler()

        comments = comment_handler.comments(
            post_id=post_id_get_field_int,
            comment_id=comment_id_get_field_int,
            name=name_get_field_str,
            email=email_get_field_str,
            body=body_get_field_str,
            query_name=query_name_field_str,
            query_body=query_body_field_str,
        )

        response_data_list: list[dict[str, str | int]] = [comment.response_data() for comment in comments]
        return jsonify(response_data_list)
