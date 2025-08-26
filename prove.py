# Define thresholds for good and warning levels
good = 0  # Threshold for good Cpk difference
warning = -0.3  # Threshold for warning Cpk difference

# Create two Plotly Figure objects
fig_diff = go.Figure()
fig_daily_diff = go.Figure()

# Iterate through the dataset, calculating the change in Cpk and the time difference
for idx, df in enumerate(all_data):
    df_valid = df.dropna(subset=['cpk'])
    delta_cpk = []  # List to store the difference in consecutive Cpk values
    delta_cpk.append(0)
    delta_days = []  # List to store the number of days between consecutive data points
    delta_days.append(0)
    daily_slope = []  # List to store the daily change in Cpk (slope)
    daily_slope.append(0)
    for i in range(1, len(df_valid)):
        # Calculate the difference in consecutive Cpk values
        cpk_diff = df_valid['cpk'].iloc[i] - df_valid['cpk'].iloc[i-1]
        delta_cpk.append(cpk_diff)

        # Calculate the number of days between the current and next Cpk
        days_diff = (df_valid['day'].iloc[i] - df_valid['day'].iloc[i-1]).days
        delta_days.append(days_diff)

        # Calculate the daily change in Cpk (slope)
        daily_slope.append(cpk_diff / days_diff if days_diff != 0 else 0)

    # Add traces for Cpk difference and daily Cpk difference
    fig_diff.add_trace(go.Scatter(x=df_valid['day'].iloc[:-1], y=delta_cpk, mode='lines', name=f'Machine {idx+1}'))
    fig_daily_diff.add_trace(go.Scatter(x=df_valid['day'].iloc[:-1], y=daily_slope, mode='lines', name=f'Machine {idx+1}'))

# Add horizontal lines to indicate good and warning thresholds for Cpk difference
fig_diff.add_hline(y=good, line=dict(color='green', dash='dash'))
fig_diff.add_hline(y=warning, line=dict(color='yellow', dash='dash'))

# Add rectangles to visually highlight different regions for Cpk difference
fig_diff.add_hrect(y0=good, y1=4, fillcolor='rgba(0, 255, 0, 0.2)', line_width=0)
fig_diff.add_hrect(y0=warning, y1=good, fillcolor='rgba(255, 255, 0, 0.2)', line_width=0)
fig_diff.add_hrect(y0=-2.5, y1=warning, fillcolor='rgba(255, 0, 0, 0.2)', line_width=0)

# Update the layout of the figure for Cpk difference
fig_diff.update_layout(title='Cpk Difference',
                       xaxis_title='Date',
                       yaxis_title='Value')

# Add horizontal lines to indicate good and warning thresholds for daily Cpk difference
fig_daily_diff.add_hline(y=good, line=dict(color='green', dash='dash'))
fig_daily_diff.add_hline(y=warning, line=dict(color='yellow', dash='dash'))

# Add rectangles to visually highlight different regions for daily Cpk difference
fig_daily_diff.add_hrect(y0=good, y1=2, fillcolor='rgba(0, 255, 0, 0.2)', line_width=0)
fig_daily_diff.add_hrect(y0=warning, y1=good, fillcolor='rgba(255, 255, 0, 0.2)', line_width=0)
fig_daily_diff.add_hrect(y0=-2, y1=warning, fillcolor='rgba(255, 0, 0, 0.2)', line_width=0)

# Update the layout of the figure for daily Cpk difference
fig_daily_diff.update_layout(title='Cpk Daily Difference',
                             xaxis_title='Date',
                             yaxis_title='Value')

# Display the plots
fig_diff.show()
fig_daily_diff.show()
