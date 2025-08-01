# Function to find best trend
def estimate_trend(x, y, max_degree):
    x_numeric = (x - x.iloc[0]).dt.total_seconds() / (60 * 60 * 24)  # Convert datetime to numeric (in days)
    best_rmse = float('inf')  # Initialize best RMSE with infinity
    best_trend = None  # Initialize best trend as None

    for deg in range(1, max_degree + 1):
        coeffs = np.polyfit(x_numeric, y, deg=deg)  # Fit polynomial of given degree
        trend = np.polyval(coeffs, x_numeric)  # Evaluate polynomial
        rmse = np.sqrt(mean_squared_error(y, trend))  # Calculate RMSE
        if rmse < best_rmse:
            best_rmse = rmse  # Update best RMSE
            best_trend = trend  # Update best trend

    return best_trend  # Return best trend line

# Define date boundaries
change1 = pd.to_datetime('2023-09-25')  # First change date
year_24 = pd.to_datetime('2024-01-01')  # Start of year 2024
change2 = pd.to_datetime('2024-06-11')  # Second change date
assessed_change2 = pd.to_datetime('2024-06-18')  # Assessed change date

# Split dataset into three parts based on date ranges
df_machine1 = qc_rows[qc_rows['date_c'] < change1].copy()  # Data before change1
df_machine2 = qc_rows[(qc_rows['date_c'] > year_24) & (qc_rows['date_c'] < change2)].copy()  # Data between year_24 and change2
df_machine3 = qc_rows[qc_rows['date_c'] > assessed_change2].copy()  # Data after assessed_change2

# Ensure date column is in datetime format
for df in [df_machine1, df_machine2, df_machine3]:
    df['date_c'] = pd.to_datetime(df['date_c'])  # Convert to datetime

# Estimate polynomial trends for each machine dataset
max_degree = 3  # Maximum polynomial degree
trend_m1 = estimate_trend(df_machine1['date_c'], df_machine1['deviation'], max_degree)  # Trend for machine 1
trend_m2 = estimate_trend(df_machine2['date_c'], df_machine2['deviation'], max_degree)  # Trend for machine 2
trend_m3 = estimate_trend(df_machine3['date_c'], df_machine3['deviation'], max_degree)  # Trend for machine 3

# Remove trend from the data to get detrended values
detrended_m1 = df_machine1['deviation'] - trend_m1  # Detrended machine 1 data
detrended_m2 = df_machine2['deviation'] - trend_m2  # Detrended machine 2 data
detrended_m3 = df_machine3['deviation'] - trend_m3  # Detrended machine 3 data

# Create plot for original data with trends
fig_trends = go.Figure()

fig_trends.add_trace(go.Scatter(x=df_machine1['date_c'], y=df_machine1['deviation'],
                                mode='lines', name='Data Machine 1', line=dict(color='gray')))  # Original data M1
fig_trends.add_trace(go.Scatter(x=df_machine1['date_c'], y=trend_m1,
                                mode='lines', name='Trend Machine 1', line=dict(color='blue')))  # Trend M1

fig_trends.add_trace(go.Scatter(x=df_machine2['date_c'], y=df_machine2['deviation'],
                                mode='lines', name='Data Machine 2', line=dict(color='white')))  # Original data M2
fig_trends.add_trace(go.Scatter(x=df_machine2['date_c'], y=trend_m2,
                                mode='lines', name='Trend Machine 2', line=dict(color='orange')))  # Trend M2

fig_trends.add_trace(go.Scatter(x=df_machine3['date_c'], y=df_machine3['deviation'],
                                mode='lines', name='Data Machine 3', line=dict(color='lightgreen')))  # Original data M3
fig_trends.add_trace(go.Scatter(x=df_machine3['date_c'], y=trend_m3,
                                mode='lines', name='Trend Machine 3', line=dict(color='red')))  # Trend M3

fig_trends.update_layout(
    title='Original Data and Estimated Trends',  # Set plot title
    xaxis_title='Date',  # X-axis label
    yaxis_title='Value')  # Y-axis label

fig_trends.show()  # Display the trend plot

# Create plot for detrended data
fig_detrended = go.Figure()

fig_detrended.add_trace(go.Scatter(x=df_machine1['date_c'], y=detrended_m1,
                                   mode='lines', name='Detrended Machine 1', line=dict(color='gray')))  # Detrended M1
fig_detrended.add_trace(go.Scatter(x=df_machine2['date_c'], y=detrended_m2,
                                   mode='lines', name='Detrended Machine 2', line=dict(color='white')))  # Detrended M2
fig_detrended.add_trace(go.Scatter(x=df_machine3['date_c'], y=detrended_m3,
                                   mode='lines', name='Detrended Machine 3', line=dict(color='lightgreen')))  # Detrended M3

fig_detrended.update_layout(
    title='Detrended Data',  # Set plot title
    xaxis_title='Date',  # X-axis label
    yaxis_title='Detrended Value')  # Y-axis label

# Display the detrended plot
fig_detrended.show()