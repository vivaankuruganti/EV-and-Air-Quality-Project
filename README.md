# Predicting Air Quality (Daily AQI) from Energy, Transportation, and Fuel Indicators

This repository contains a **notebook-first** data science project that combines multi-year air quality data with
energy consumption, vehicle sales (ZEV/LDV), and gas price signals to model **Daily AQI Value**.

The main artifact is the Jupyter notebook:

- `notebooks/air_quality_modeling.ipynb`

## Project goal

Build and evaluate regression models to predict **Daily AQI Value** using features such as:

- Electricity consumption (GWh)
- Natural gas consumption (MMTherms)
- Total energy consumption
- Gas price
- ZEV vs. LDV sales (and ratios)
- County identifier and time features (e.g., year/quarter)

## What’s inside

- Data loading & merging across multiple CSV sources (2008–2024)
- Feature engineering (time + energy/transport aggregates)
- Baselines (linear / regularized regression)
- Nonlinear models (Random Forest, SVR, XGBoost)
- Cross-validation designed to reduce time leakage (e.g., grouping by year)

## How to run

1. **Clone**
   ```bash
   git clone <your-repo-url>
   cd <your-repo-folder>
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   # .venv\Scripts\activate  # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add data**
   Place the required CSV files into `data/` (see `data/README.md`).

5. **Open the notebook**
   ```bash
   jupyter lab
   ```
   Then open: `notebooks/air_quality_modeling.ipynb`

## Notes for applications / reviewers

- The notebook is written to be readable end-to-end (data → models → evaluation).
- If the raw datasets cannot be shared publicly, this repo intentionally keeps data out of version control.
- If you have a slide deck, export it as a PDF and add it to `slides/`.

## Suggested next improvements (optional)

- Move repeated preprocessing steps into `src/` functions
- Add a small sample dataset (if allowed) for easy reproduction
- Add a short one-page writeup with key findings + one figure
