# Tennis Computer Vision

Computer vision workspace for tennis-related detection experiments.

The repository currently contains:

- notebook-based YOLO exploration
- a Roboflow dataset download module
- a small dataset filtering helper
- scaffolded package folders for data, features, and models

## Current Status

This project is still in setup/scaffolding mode.

- `notebooks/yolo_exploration.ipynb` is the clearest working artifact in the repo today.
- `tennis_analysis/data/load.py` contains the dataset download logic for a Roboflow project.
- `tennis_analysis/data/filter.py` contains a helper for copying image subsets by filename prefix.
- training, prediction, and feature modules are present but currently empty.
- `requirements.txt` exists but is currently empty and needs to be populated.

## Repository Layout

```text
.
|-- data/
|   |-- raw/
|   `-- processed/
|-- notebooks/
|   |-- yolo_exploration.ipynb
|   |-- yolo26n.pt
|   `-- yolo26s.pt
|-- scripts/
|   |-- make_dataset.py
|   `-- train_model.py
`-- tennis_analysis/
    |-- data/
    |   |-- load.py
    |   |-- filter.py
    |   `-- clean.py
    |-- features/
    |   `-- test.py
    `-- models/
        |-- train.py
        `-- predict.py
```

## Setup

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Note: `requirements.txt` is currently empty. Based on the code and notebook, the project will likely need at least:

- `roboflow`
- `python-dotenv`
- `ultralytics`
- `jupyter`

## Environment Variables

The Roboflow download module expects a local `.env` file with values for:

```env
API_KEY_ROBO_FLOW=...
WORKSPACE_ROBO_FLOW=...
PROJECT_ROBO_FLOW=...
VERSION_ROBO_FLOW=...
```

The repository `.gitignore` already excludes `.env`, `.venv`, `__pycache__`, and `data/`.

## Workflow

At the moment, the most practical workflow is:

1. Set up the environment and install the required packages.
2. Add the Roboflow credentials to `.env`.
3. Download or prepare raw data under `data/raw/`.
4. Explore detection results in `notebooks/yolo_exploration.ipynb`.
5. Expand the empty training and prediction modules into reusable scripts.

## Next Improvements

Useful follow-up work for this repository:

- populate `requirements.txt`
- add CLI entrypoints to `scripts/`
- implement model training and inference modules
- add tests for dataset utilities
- document dataset format and model outputs
