# Set the window size to 10 data points
window_size = 10

# Calculate the moving average and moving variance for the 'deviation' column
qc_rows['moving_avg'] = qc_rows['deviation'].rolling(window=window_size).mean()  # Moving average
qc_rows['moving_var'] = qc_rows['deviation'].rolling(window=window_size).var()    # Moving variance

# Initialize the column for Mahalanobis distance with NaN values
qc_rows['mahalanobis'] = np.nan  # Create an empty column for storing Mahalanobis distances

# Calculate the Mahalanobis distance for each point starting from the 20th index
for i in range((window_size*2)-1, len(qc_rows)):
    # Extract the previous window of 10 mean and variance values
    prev_mean = qc_rows['moving_avg'].iloc[i-window_size:i]  # Last 10 values of moving average
    prev_var = qc_rows['moving_var'].iloc[i-window_size:i]    # Last 10 values of moving variance

    # Compute the average mean and variance of the previous window
    mean_mean = np.mean(prev_mean)  # Mean of previous means
    mean_var = np.mean(prev_var)    # Mean of previous variances

    # Calculate the covariance matrix (2x2 matrix)
    cov_matrix = np.cov(prev_mean, prev_var)

    # Invert the covariance matrix
    inv_cov_matrix = np.linalg.inv(cov_matrix)

    # Compute the Mahalanobis distance between the current mean/variance and the previous window
    mahalanobis_score = mahalanobis([qc_rows['moving_avg'].iloc[i], qc_rows['moving_var'].iloc[i]],
                                    [mean_mean, mean_var], inv_cov_matrix)

    # Assign the calculated Mahalanobis distance to the corresponding row in the DataFrame
    qc_rows.loc[qc_rows.index[i], 'mahalanobis'] = mahalanobis_score

# Create a scatter plot of Mahalanobis distance over time using Plotly
fig = px.scatter(qc_rows, x='date_c', y='mahalanobis',
                 labels={'date_c': 'Date', 'mahalanobis': 'Mahalanobis Distance'},
                 title='Mahalanobis Distance Over Time')

# Display the plot
fig.show()