# Function to perform the Lomb-Scargle periodogram
def lomb_scargle(df, dates, detrended_measurements):
    # Extract time values and convert to numerical format (number of hours since first timestamp)
    time = df[dates].values
    time = (time - time[0]).astype('timedelta64[h]').astype(int)  # Time in hours

    # Compute Lomb-Scargle power spectrum
    # Maximum frequency set to 0.5 cycles per day due to Nyquist limit
    # In some days, only one measurement is available, so we cannot detect cycles shorter than 2 days
    frequency, power = LombScargle(time, detrended_measurements).autopower(maximum_frequency=0.5/24)

    return frequency, power  # Return frequency and power

# Compute Lomb-Scargle for the machine 1 dataset
freq_m1, power_m1 = lomb_scargle(df_machine1, 'date_c', detrended_m1)  # Frequency and power for M1

# Compute Lomb-Scargle for the machine 3 dataset
freq_m3, power_m3 = lomb_scargle(df_machine3, 'date_c', detrended_m3)  # Frequency and power for M3

# Create plot to show the power spectrum in the frequency domain
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=24 * freq_m1,  # Convert frequency to cycles per day
    y=power_m1,
    mode='lines',
    name='Machine 1'))

fig.add_trace(go.Scatter(
    x=24 * freq_m3,
    y=power_m3,
    mode='lines',
    name='Machine 3'))

fig.update_layout(
    title='Lomb-Scargle Periodogram (Frequency)',  # Set plot title
    xaxis_title='Frequency (cycles per day)',  # X-axis label
    yaxis_title='Lomb-Scargle Power')  # Y-axis label

# Display the plot
fig.show()