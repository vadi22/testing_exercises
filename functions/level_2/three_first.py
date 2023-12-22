NOT_SET = "NOT_SET"


def first(items: list[int], default: int | None | str = NOT_SET) -> int | None:
    if items == []:
        return None
    if default == NOT_SET:
        raise AttributeError from None
    return items[0]
