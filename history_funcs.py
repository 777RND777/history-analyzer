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
