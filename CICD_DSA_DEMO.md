# CICD DSA Repair Demo

This is an intentionally broken Python repository for demonstrating the CICD self-healing pipeline.

## Run locally

```powershell
python -m pytest -q
```

The tests should fail before repair. The defects are in `algorithms.py`:

- `binary_search` returns `0` instead of `-1` when a value is absent.
- `merge_intervals` does not merge touching intervals.
- `longest_increasing_subsequence` treats equal values as increasing.

The Dijkstra implementation is included as a larger context example and is tested for reachable and unreachable nodes.

## Use with CICD

Push this folder to a GitHub repository, then enter:

- Repository: the public GitHub URL
- Source branch: `main`
- Target file: `algorithms.py`

CICD clones the GitHub repository into a temporary workspace, runs these tests in Docker, sends the failure context to OpenRouter on a memory miss, applies the returned repair, and runs the tests again.