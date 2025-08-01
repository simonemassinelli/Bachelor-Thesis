# Define thresholds for good and warning levels
good = 0
warning = -0.3

# Create the Plotly figure for daily Cpk difference
fig_daily_diff = go.Figure()

# Iterate through the dataset, calculating the daily Cpk change
for idx, df in enumerate(all_data):
    df_valid = df.dropna(subset=['cpk'])
    daily_slope = [0]  # Start with 0 for the first point

    for i in range(1, len(df_valid)):
        cpk_diff = df_valid['cpk'].iloc[i] - df_valid['cpk'].iloc[i-1]
        days_diff = (df_valid['day'].iloc[i] - df_valid['day'].iloc[i-1]).days
        daily_slope.append(cpk_diff / days_diff if days_diff != 0 else 0)

    # Add the trace for daily Cpk change
    fig_daily_diff.add_trace(go.Scatter(
        x=df_valid['day'],
        y=daily_slope,
        mode='lines',
        name=f'Machine {idx+1}'))

# Add threshold lines
fig_daily_diff.add_hline(y=good, line=dict(color='green', dash='dash'))
fig_daily_diff.add_hline(y=warning, line=dict(color='yellow', dash='dash'))

# Add highlighted regions
fig_daily_diff.add_hrect(y0=good, y1=2, fillcolor='rgba(0, 255, 0, 0.2)', line_width=0)
fig_daily_diff.add_hrect(y0=warning, y1=good, fillcolor='rgba(255, 255, 0, 0.2)', line_width=0)
fig_daily_diff.add_hrect(y0=-3.5, y1=warning, fillcolor='rgba(255, 0, 0, 0.2)', line_width=0)

# Update layout
fig_daily_diff.update_layout(
    title='Daily Change in Cpk Index',
    xaxis_title='Date',
    yaxis_title='Daily Cpk Difference')

# Show the figure
fig_daily_diff.show()