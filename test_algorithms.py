from algorithms import (
    binary_search,
    longest_increasing_subsequence,
    merge_intervals,
    shortest_path,
)


def test_binary_search_returns_minus_one_when_missing():
    assert binary_search([2, 4, 6, 8, 10], 7) == -1


def test_binary_search_finds_existing_value():
    assert binary_search([2, 4, 6, 8, 10], 8) == 3


def test_merge_intervals_merges_touching_ranges():
    assert merge_intervals([[1, 3], [3, 5], [8, 10]]) == [[1, 5], [8, 10]]


def test_merge_intervals_handles_nested_ranges():
    assert merge_intervals([[1, 10], [2, 4], [12, 14]]) == [[1, 10], [12, 14]]


def test_shortest_path_finds_cheapest_route():
    graph = {
        "A": [("B", 4), ("C", 1)],
        "B": [("D", 1)],
        "C": [("B", 2), ("D", 7)],
        "D": [],
    }
    assert shortest_path(graph, "A", "D") == 4


def test_shortest_path_returns_none_when_unreachable():
    graph = {"A": [("B", 1)], "B": [], "C": []}
    assert shortest_path(graph, "A", "C") is None


def test_lis_is_strictly_increasing():
    assert longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]) == 4


def test_lis_handles_duplicates():
    assert longest_increasing_subsequence([2, 2, 2, 3]) == 2