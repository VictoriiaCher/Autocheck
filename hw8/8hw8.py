from collections import Counter


def get_count_visits_from_ip(ips):
    return Counter(ips)


def get_frequent_visit_from_ip(ips):
    result = Counter(ips).most_common(1)
    return result[0]


ips = [
    "85.157.172.253",
    "85.157.172.253",
    "85.157.172.253",
    "85.155.172.253",
    "85.155.172.253",
    "85.157.172.255",
]

print(get_count_visits_from_ip(ips))
print(get_frequent_visit_from_ip(ips))
