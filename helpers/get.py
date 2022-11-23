from flask import request


def get_str(field: str) -> str | None:
    return request.args.get(field)


def get_int(field: str) -> int | None:
    get_field_str: str | None = get_str(field)
    if get_field_str is not None and get_field_str.isdigit():
        return int(get_field_str)
    else:
        return None
