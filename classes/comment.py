class Comment:
    post_id_external_str: str = "postId"
    comment_id_external_str: str = "id"
    name_external_str: str = "name"
    email_external_str: str = "email"
    body_external_str: str = "body"

    post_id_field_str: str = "post_id"
    comment_id_field_str: str = "comment_id"
    name_field_str: str = "name"
    email_field_str: str = "email"
    body_field_str: str = "body"

    def __init__(self, post_id: int, comment_id: int, name: str, email: str, body: str):
        self._post_id = post_id
        self._comment_id = comment_id
        self._name = name
        self._email = email
        self._body = body

    def post_id(self) -> int:
        return self._post_id

    def comment_id(self) -> int:
        return self._comment_id

    def name(self) -> str:
        return self._name

    def email(self) -> str:
        return self._email

    def body(self) -> str:
        return self._body

    def response_data(self) -> dict[str, int | str]:
        data = {
            self.post_id_field_str: self._post_id,
            self.comment_id_field_str: self._comment_id,
            self.name_field_str: self._name,
            self.email_field_str: self._email,
            self.body_field_str: self._body,
        }
        return data
