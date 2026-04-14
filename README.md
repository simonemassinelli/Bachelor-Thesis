## Bachelor's Thesis 

## About 
Contains all the codes used to develop my bachelor's thesis, which represent an exploratory data-driven approach to control the working quality of an already-standardized working tool.
[cite_start]Analyzing historical data of critical dimensions (QC) collected over a two-year period [cite: 2477, 2487][cite_start], this project aims to continuously monitor the evolution of the Process Capability Index (Cpk)[cite: 1818, 1822]. [cite_start]This proposes a shift from the traditional method of relying solely on initial standardization metrics and fixed machine lifecycles (e.g., 100,000 cycles) [cite: 1793, 1796][cite_start], toward a dynamic monitoring system aimed at optimizing tool replacements, predicting process degradation, and minimizing waste[cite: 1812].

## Data Pipeline
* [cite_start]**Data Extraction & Structuring:** Automated parsing of hundreds of individual `.tsv` measurement files from ZIP archives[cite: 2488, 2534]. [cite_start]The script extracts file creation timestamps to build a coherent time-series DataFrame[cite: 2490, 2491].
* [cite_start]**Data Cleaning & Integration:** Merging scattered measurement data into a centralized format and validating it against nominal values and Upper/Lower Tolerances[cite: 2539, 2619, 2620, 2621].

## Methodology & Analytics
The repository includes Python scripts for various stages of statistical analysis:
* [cite_start]**Machine Change Detection:** Implementing the **Mahalanobis distance** on moving averages and moving variances to mathematically identify unrecorded tool replacements and burn-in phases[cite: 2689, 2691, 2695].
* [cite_start]**Trend & Seasonality Analysis:** * Applying **3rd-degree polynomial regression** to detrend the data[cite: 2766].
  * [cite_start]Utilizing the **Lomb-Scargle periodogram** to search for cyclic patterns and seasonality in unevenly spaced time-series data[cite: 2890, 2891].
* [cite_start]**Normality Verification:** Using Histograms and Kernel Density Estimation (KDE) to verify the normal distribution of the data before and after detrending[cite: 2974, 2978].
* **Dynamic Cpk Modeling:**
  * [cite_start]Implementing a rolling daily Cpk calculation[cite: 3156].
  * [cite_start]Applying an **Exponential Decay Weighting function** ($w(t) = e^{-At}$) to assign greater importance to recent measurements[cite: 3161, 3162, 3163].
  * [cite_start]Utilizing **Bessel's correction** to provide an unbiased estimate of the weighted variance[cite: 3203, 3205].
* [cite_start]**Derivative Analysis:** Calculating the daily rate of change (derivative) of the Cpk index to evaluate how rapidly machine capability is gained or lost[cite: 3336, 3337].

## Key Findings
[cite_start]The analysis demonstrates that tool capability does not necessarily degrade in a smooth, linear fashion; rather, the Cpk often changes in sudden "jumps" due to unrecorded events or maintenance[cite: 3426, 3427, 3428]. [cite_start]Continuous, data-driven monitoring of the Cpk index offers a more responsive and accurate framework for scheduling maintenance and replacing machines compared to fixed-cycle estimates[cite: 3441, 3442].
