"""Small algorithm library used to demonstrate CICD repair."""


def binary_search(values: list[int], target: int) -> int:
    """Return the index of target in a sorted list, or -1 when absent."""
    left = 0
    right = len(values) - 1

    while left <= right:
        middle = (left + right) // 2
        if values[middle] == target:
            return middle
        if values[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1


def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    """Merge overlapping inclusive intervals."""
    if not intervals:
        return []

    ordered = sorted(intervals)
    merged = [ordered[0][:]]

    for start, end in ordered[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])

    return merged


def shortest_path(graph: dict[str, list[tuple[str, int]]], start: str, goal: str) -> int | None:
    """Return the minimum weighted path cost using Dijkstra's algorithm."""
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    unvisited = set(graph)

    while unvisited:
        current = min(unvisited, key=lambda node: distances[node])
        if distances[current] == float("inf"):
            break
        unvisited.remove(current)

        if current == goal:
            return int(distances[current])

        for neighbor, weight in graph[current]:
            candidate = distances[current] + weight
            if candidate < distances[neighbor]:
                distances[neighbor] = candidate

    return None


def longest_increasing_subsequence(values: list[int]) -> int:
    """Return the length of a longest strictly increasing subsequence."""
    if not values:
        return 0

    lengths = [1] * len(values)
    for index in range(len(values)):
        for previous in range(index):
            if values[previous] < values[index]:
                lengths[index] = max(lengths[index], lengths[previous] + 1)

    return max(lengths)