def solve(st):
    first_seen = {}
    distance = {}

    for index, char in enumerate(st):
        if char not in first_seen:
            first_seen[char] = index

        distance[char] = index - first_seen[char]

    max = distance[st[0]]

    max_char = st[0]
