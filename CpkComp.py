# Define parameters for rolling window, minimum data points, and exponential decay
window_size = 30  # Rolling time window size (in days)
min_measurements = 20  # Minimum number of measurements required to calculate Cpk
expected_value = qc_rows['nominal'].iloc[0]  # Extract the expected nominal value
max_value = expected_value + UT  # Compute the upper tolerance limit
min_value = expected_value + LT  # Compute the lower tolerance limit
A = 0.1  # Decay factor used in the weighting function

# Combine all machine datasets for processing
all_data = [df_machine1, df_machine2, df_machine3]
for df in all_data:
    # Add a column with only the date (no time) from datetime
    df['day'] = df['date_c'].dt.date  # Extract date component
    # Flag the last measurement of each production day
    df['last_measurement'] = df['day'] != df['day'].shift(-1)
    # Initialize the Cpk column with NaN values
    df['cpk'] = np.nan  # Prepare column for Cpk results

    # Count how many production days are present in the dataset
    production_days = df['last_measurement'].sum()
    # Filter only the last measurement entries for each day
    last_measurements = df.loc[df['last_measurement'] == True]  # Daily endpoints

    # Loop through each production day to compute Cpk
    for i in range(production_days):
        # Select the current day's last measurement
        production_day = last_measurements.iloc[i]
        date = production_day['day']  # Extract the date

        # Define the time window start (rolling back in time)
        window_start = date - pd.Timedelta(days=window_size - 1)
        # Filter the dataset to include only data within the rolling window
        window = df[(df['day'] >= window_start) & (df['day'] <= date)]
        total_measurements = len(window)  # Number of measurements in the window

        # Check if the window contains enough data to calculate Cpk
        if total_measurements < min_measurements:
            df.loc[last_measurements.index[i], 'cpk'] = np.nan  # Not enough data
        else:
            # Initialize the list of weights
            alfa = []
            for j in range(len(window)):
                td = (date - window['day'].iloc[j]).days
                alfa.append(weight(td, A))

            # Normalize weights
            norm_factor = sum(alfa)
            normalized_alfa = [a / norm_factor for a in alfa]

            # Weighted mean
            mean = sum(window['actual'].iloc[k] * normalized_alfa[k] for k in range(len(window)))

            # Weighted variance with Bessel correction
            squared_diffs = [(window['actual'].iloc[k] - mean) ** 2 for k in range(len(window))]
            num = sum(normalized_alfa[k] * squared_diffs[k] for k in range(len(window)))
            den = 1 - sum(w ** 2 for w in normalized_alfa)
            var = num / den if den > 0 else 0  # Avoid division by 0
            sigma = np.sqrt(var)


            # Calculate Cpk for both upper and lower limits
            cpk_upper = (max_value - mean) / (3 * sigma)  # Upper process capability
            cpk_lower = (mean - min_value) / (3 * sigma)  # Lower process capability
            cpk = min(cpk_upper, cpk_lower)  # Take the worst-case (minimum) value

            # Assign the Cpk value to the corresponding row in the DataFrame
            df.loc[last_measurements.index[i], 'cpk'] = cpk  # Save the result