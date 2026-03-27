# Sample Project: CFD Utilities

A small Python module with utility functions for CFD pre/post-processing.
Use this project to practise the Git workflows from the lecture.

## Suggested exercises

1. **Branch and add a function:** Create a `feature/reynolds` branch, add a Reynolds number calculator to `src/utils.py`, commit, push, and open a PR.
2. **Fix a bug:** There's a deliberate bug in `src/mesh.py` — find it, fix it on a `fix/mesh-bug` branch, and submit a PR.
3. **Add tests:** Write pytest tests in `tests/` for the existing functions.
4. **Resolve a conflict:** Have two branches modify the same function, then merge both into main.
5. **Tag a release:** After merging, tag the result as `v0.1.0` and create a GitHub release with `gh`.

## Running

```bash
python3 -m src.utils
python3 -m pytest tests/ -v   # after writing tests
```
