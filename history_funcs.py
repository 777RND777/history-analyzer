from math_funcs import *


class Amount:
    def __init__(self, name):
        self.name = name
        self.amount = 1


def get_history_count_info(history_info, limit):
    history_count = []
    for i in range(len(history_info)):
        if i > limit != 0:
            break
        link = history_info[i][0]
        if link.startswith("https://"):
            link = link[8:]
            if link.startswith("www."):
                link = link[4:]
            link = link[:link.index("/")]
            for j in range(len(history_count)):
                if history_count[j].name == link:
                    history_count[j].amount += 1
                    break
            else:
                history_count.append(Amount(link))

    return history_count


def get_top_history_count_info(history_count, top):
    top_history_count = []
    limit = get_maximum_amount(history_count)

    for info in history_count:
        if len(top_history_count) == top:
            minimal = get_minimal_value(top_history_count, limit)
            if info.amount > minimal:
                for i in range(len(top_history_count)):
                    if top_history_count[i].amount == minimal:
                        top_history_count[i] = info
                        break
        else:
            top_history_count.append(info)

    return add_minimal_equal(sort_history(top_history_count), history_count)


def sort_history(top_history_count):
    for i in range(len(top_history_count)):
        for j in range(len(top_history_count))[1:]:
            if top_history_count[j - 1].amount < top_history_count[j].amount:
                top_history_count[j - 1], top_history_count[j] = top_history_count[j], top_history_count[j - 1]

    return top_history_count


def add_minimal_equal(top_history_count, history_count):
    minimal = top_history_count[len(top_history_count) - 1].amount
    for info in history_count:
        if info.amount == minimal:
            for sort_name in top_history_count:
                if sort_name.name == info.name:
                    break
            else:
                top_history_count.append(info)

    return top_history_count
