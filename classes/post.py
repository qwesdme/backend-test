class Post:
    user_id_external_str: str = "userId"
    id_external_str: str = "id"
    title_external_str: str = "title"
    body_external_str: str = "body"

    user_id_field_str: str = "post_id"
    id_field_str: str = "post_title"
    title_field_str: str = "post_body"
    body_field_str: str = "total_number_of_comments"

    def __init__(self, user_id: int, post_id: int, title: str, body: str, comment_count: int):
        self._user_id = user_id
        self._post_id = post_id
        self._title = title
        self._body = body
        self._comment_count = comment_count

    def user_id(self) -> int:
        return self._user_id

    def post_id(self) -> int:
        return self._post_id

    def title(self) -> str:
        return self._title

    def body(self) -> str:
        return self._body

    def comment_count(self) -> int:
        return self._comment_count

    def response_data(self) -> dict[str, int | str]:
        data = {
            self.user_id_field_str: self._post_id,
            self.id_field_str: self._title,
            self.title_field_str: self._body,
            self.body_field_str: self._comment_count,
        }
        return data

    # allow sorting
    def __lt__(self, other):
        # noinspection PyStatementEffect,PyProtectedMember
        self._comment_count < other._comment_count
