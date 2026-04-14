## Bachelor's Thesis 

## About 
Contains all the codes used to develop my bachelor's thesis, which represent an exploratory data-driven approach to control the working quality of an already-standardized working tool.
Analyzing historical data of critical dimensions (QC) collected over a two-year period, this project aims to continuously monitor the evolution of the Process Capability Index (Cpk). This proposes a shift from the traditional method of relying solely on initial standardization metrics and fixed machine lifecycles (e.g., 100,000 cycles), toward a dynamic monitoring system aimed at optimizing tool replacements, predicting process degradation, and minimizing waste.

## Data Pipeline
**Data Extraction & Structuring:** Automated parsing of hundreds of individual `.tsv` measurement files from ZIP archives.The script extracts file creation timestamps to build a coherent time-series DataFrame.
**Data Cleaning & Integration:** Merging scattered measurement data into a centralized format and validating it against nominal values and Upper/Lower Tolerances.

## Methodology & Analytics
The repository includes Python scripts for various stages of statistical analysis:
**Machine Change Detection:** Implementing the **Mahalanobis distance** on moving averages and moving variances to mathematically identify unrecorded tool replacements and burn-in phases.
**Trend & Seasonality Analysis:** * Applying **3rd-degree polynomial regression** to detrend the data.
Utilizing the **Lomb-Scargle periodogram** to search for cyclic patterns and seasonality in unevenly spaced time-series data.
**Normality Verification:** Using Histograms and Kernel Density Estimation (KDE) to verify the normal distribution of the data before and after detrending.
**Dynamic Cpk Modeling:**
  Implementing a rolling daily Cpk calculation.
  Applying an **Exponential Decay Weighting function** ($w(t) = e^{-At}$) to assign greater importance to recent measurements.
  Utilizing **Bessel's correction** to provide an unbiased estimate of the weighted variance.
**Derivative Analysis:** Calculating the daily rate of change (derivative) of the Cpk index to evaluate how rapidly machine capability is gained or lost.

## Key Findings
The analysis demonstrates that tool capability does not necessarily degrade in a smooth, linear fashion; rather, the Cpk often changes in sudden "jumps" due to unrecorded events or maintenance. Continuous, data-driven monitoring of the Cpk index offers a more responsive and accurate framework for scheduling maintenance and replacing machines compared to fixed-cycle estimates.
