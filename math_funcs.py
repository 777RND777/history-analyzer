def get_minimal_value(history_info, minimal):
    for i in range(len(history_info)):
        if minimal > history_info[i].amount:
            minimal = history_info[i].amount

    return minimal


def get_maximum_amount(history_info):
    maximum = 0
    for i in range(len(history_info)):
        if maximum < history_info[i].amount:
            maximum = history_info[i].amount

    return maximum
