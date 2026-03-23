# Numerical Methods - 5th Semester

Professional workspace for University Lab assignments and Lecture scripts.

## 🚀 Setup
This project uses **Poetry** for dependency management.
1. Install dependencies: `poetry install`
2. Activate environment: `poetry shell`

## 📁 Structure
- `src/`: Core mathematical algorithms (Bisection, Newton-Raphson, etc.)
- `notebooks/`: Visual analysis and Calculus exploration.
- `data/`: Datasets for curve fitting and interpolation.
- `docs/`: Lab manuals and lecture notes.
```
Numerical-Method/
├── .venv/               # Isolated environment (never touch files here)
├── .vscode/             # Editor-specific settings (linter, interpreter)
├── data/                # Raw and processed datasets (CSV, JSON)
├── docs/                # Project documentation, Lab manuals, or PDFs
├── notebooks/           # Jupyter Notebooks for exploration and plotting
├── tests/               # Unit tests to ensure your math logic is correct
├── src/                 # THE ACTUAL SOURCE CODE
│   └── numerical_methods/
│       ├── __init__.py  # Makes the folder a package
│       ├── solvers/     # Reusable math algorithms
│       └── utils/       # Helper functions (plotting, logging)
├── .gitignore           # Tells Git to ignore .venv and temp files
├── poetry.lock          # Frozen library versions
├── pyproject.toml       # Project metadata and dependencies
└── README.md            # The "Face" of the project (instructions)
```

## 🛠 Tech Stack
- **Python 3.14**
- **NumPy** (Linear Algebra)
- **SciPy** (Optimization/Integration)
- **Matplotlib** (Visualization)
