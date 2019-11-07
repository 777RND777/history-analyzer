from browserhistory import get_browserhistory
from history_funcs import get_history_count_info, get_top_history_count_info
from math_funcs import get_maximum_name_size, get_percentages


if __name__ == "__main__":
    limit = 0
    history_info = get_browserhistory()["chrome"]
    history_count_info = get_history_count_info(history_info, limit)
    history_count_info = get_top_history_count_info(history_count_info, 10)

    max_size = get_maximum_name_size(history_count_info)
    for info in history_count_info:
        percentages = get_percentages(info.amount, len(history_info))
        print((max_size - len(info.name)) * " ", info.name, "|", percentages * "#", info.amount,
              "(" + str(percentages) + "%)")
