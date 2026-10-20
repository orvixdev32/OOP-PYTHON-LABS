# list_utils.py

def sort_list(lst):
    """Повертає відсортований список"""
    return sorted(lst)

def remove_duplicates(lst):
    """Видаляє дублікати зі списку, зберігаючи порядок елементів (за бажанням), або просто через set"""
    return list(set(lst))

def find_max_min(lst):
    """Повертає максимальний та мінімальний елементи списку"""
    if not lst:
        return None, None
    return max(lst), min(lst)