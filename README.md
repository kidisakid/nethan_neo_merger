# Nethan Neo Merger (Module)

`nethan_neo_merger` is a small, reusable Python module intended to be integrated into a larger application that manipulates dataset files. It exposes utilities to read, normalize, and merge CSV and XLSX files; a lightweight Streamlit demo app is included for manual testing and quick previews, but the package is designed primarily for programmatic use.

## Purpose

- Provide reliable utilities to combine tabular datasets (CSV / XLSX) used by a host application.
- Keep merging and file-handling logic separate from UI so other services (CLI, API, ETL pipelines) can reuse it.

## Key Features

- Read CSV and Excel (`.xlsx`) files and normalize headers.
- Append/concatenate multiple datasets while preserving column names.
- Small Streamlit demo for interactive testing (optional).

## Requirements

- Python 3.8+
- See `merge/requirements.txt` for exact dependency pins (notably `pandas` and `openpyxl`).

## Installation (for host projects)

Install dependencies into your host project's environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r merge/requirements.txt
```

## Project Layout, (to be adjusted and documented)

- `src/merge_csv.py` — Core merge and file-handling utilities (primary integration point).
- `src/main.py` — Streamlit demo entrypoint (optional for manual testing).
- `src/ui/merge_page.py` — Demo UI components used by the Streamlit app.
- `merge/requirements.txt` — Dependency pins used by the demo and module.

## Integration Tips

- Import only the utility functions from `src/merge_csv.py` into your host application to avoid pulling Streamlit/UI dependencies into production code.
- Validate column compatibility before merging if your workflow requires strict schemas.
- Add wrapper functions in your project to map host-specific file storage (S3, database blobs) into the file-like objects accepted by this module.

## Contributing

- Improvements and fixes welcome. Open an issue or submit a PR against the `main` branch.

## License

No license is specified. Add a license if you intend to publish or share this module publicly.

