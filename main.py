from browserhistory import get_browserhistory
from history_funcs import get_history_count_info, get_top_history_count_info
from math_funcs import get_maximum_name_size, get_percentages


if __name__ == "__main__":
    limit = 0
    history_info = get_browserhistory()["chrome"]
    history_count_info = get_history_count_info(history_info, limit)
