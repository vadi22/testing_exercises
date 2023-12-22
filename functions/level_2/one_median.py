

def get_median_value(items: list[int]) -> int | float | None:
    """
    Вычисляет медиану списка целых чисел.

    Подробнее про медиану: https://ru.wikipedia.org/wiki/%D0%9C%D0%B5%D0%B4%D0%B8%D0%B0%D0%BD%D0%B0_(%D1%81%D1%82%D0%B0%D1%82%D0%B8%D1%81%D1%82%D0%B8%D0%BA%D0%B0)
    """
    if not items:
        return None

    sorted_items = sorted(items)
    middle_index = len(sorted_items) // 2
    if len(sorted_items) % 2:
        return (sorted_items[middle_index])
    else:
        return (sorted_items[middle_index] + sorted_items[middle_index - 1])/2
