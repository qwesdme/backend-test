from classes.comment import Comment
from configs.endpoints import comments_url
from helpers.request import data_dict


class CommentHandler:
    def __init__(self):
        self._comments: list[Comment] = []
        self._load()

    def _load(self):
        for item_data in data_dict(comments_url):
            post_id: int = item_data[Comment.post_id_external_str]
            comment_id: int = item_data[Comment.comment_id_external_str]
            name: str = item_data[Comment.name_external_str]
            email: str = item_data[Comment.email_external_str]
            body: str = item_data[Comment.body_external_str]

            comment = Comment(post_id=post_id, comment_id=comment_id, name=name, email=email, body=body)
            self._comments.append(comment)

    def count_comment(self, post_id) -> int:
        count = 0

        for comment in self._comments:
            if comment.post_id() == post_id:
                count += 1

        return count

    def comments(self, post_id: int | None, comment_id: int | None, name: str | None, email: str | None,
                 body: str | None, query_name: str | None, query_body: str | None) -> list[Comment]:
        comments: list[Comment] = self._comments

        if post_id is not None:
            comments = [comment for comment in comments if comment.post_id() == post_id]
        if comment_id is not None:
            comments = [comment for comment in comments if comment.comment_id() == comment_id]
        if name is not None:
            comments = [comment for comment in comments if comment.name() == name]
        if email is not None:
            comments = [comment for comment in comments if comment.email() == email]
        if body is not None:
            comments = [comment for comment in comments if comment.body() == body]
        if query_name is not None:
            comments = [comment for comment in comments if query_name in comment.name()]
        if query_body is not None:
            comments = [comment for comment in comments if query_body in comment.body()]

        return comments
