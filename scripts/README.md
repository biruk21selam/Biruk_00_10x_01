# scripts/

This directory contains Python scripts for various tasks related to the solar radiation analysis project.

**1. data_preprocessing.py:**

*   Loads the raw solar radiation data from the specified source.
*   Performs data cleaning and preprocessing tasks:
    *   Handles missing values (e.g., imputation, removal).
    *   Identifies and handles outliers.
    *   Converts data types as needed.
    *   Creates new features (e.g., time-based features, derived variables).
*   Saves the preprocessed data to a clean and organized format (e.g., CSV, Parquet).

**2. feature_engineering.py:**

*   Creates new features from the preprocessed data:
    *   Time-based features (e.g., hour, day of week, season).
    *   Weather-related features (e.g., clear sky index, cloud cover).
    *   Rolling averages and other time-windowed statistics.
*   Saves the feature-engineered data for further analysis.

**3. model_training.py:**

*   Trains machine learning models (if applicable):
    *   Predictive models for solar radiation forecasting.
    *   Classification models for identifying optimal installation sites.
*   Evaluates model performance using appropriate metrics.
*   Saves trained models for future use.

**4. visualization.py:**

*   Generates various visualizations:
    *   Time series plots of solar radiation, temperature, and other variables.
    *   Histograms, scatter plots, and other exploratory visualizations.
    *   Wind roses and other visualizations for wind data.
    *   Maps and geospatial visualizations (if applicable).

**5. [Add more scripts as needed]:**

*   e.g., `analysis.py`, `report_generation.py`

**How to use:**

1.  Navigate to the `scripts/` directory in your terminal.
2.  Run the desired script using the `python` command: `python data_preprocessing.py`

**Note:**

*   This is a basic template and may need to be adjusted based on the specific scripts and tasks in your project.
*   Add more detailed descriptions and instructions for each script as needed.
*   Consider using a script runner or task management tool (e.g., Make, Invoke) to simplify script execution.

This README provides a clear and concise overview of the scripts contained within the `scripts/` directory, making it easier for you and others to understand and use them.