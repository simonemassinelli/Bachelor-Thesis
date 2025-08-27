from scipy.stats import gaussian_kde
from plotly.subplots import make_subplots

# Function to calculate KDE (Kernel Density Estimation)
def get_kde(x_vals, data):
    kde = gaussian_kde(data)  # Fit a kernel density estimator to the data
    return kde(x_vals)  # Evaluate KDE at the points x_vals

# Concatenate the data for all machines (before detrending)
all_original = qc_rows['deviation']
# Concatenate the data after detrending
all_detrended = pd.concat([detrended_m1, detrended_m2, detrended_m3], ignore_index=True)

# List of datasets with names and colors for each plot
datasets = [(all_original, "All Data - Original", 'royalblue'),
    (all_detrended, "All Data - Detrended", 'firebrick'),
    (df_machine1['deviation'], "Machine 1 - Original", 'gray'),
    (detrended_m1, "Machine 1 - Detrended", 'darkgray'),
    (df_machine2['deviation'], "Machine 2 - Original", 'orange'),
    (detrended_m2, "Machine 2 - Detrended", 'darkorange'),
    (df_machine3['deviation'], "Machine 3 - Original", 'lightgreen'),
    (detrended_m3, "Machine 3 - Detrended", 'green')]

# Create subplots layout with 8 rows and 1 column
fig = make_subplots(rows=8, cols=1,
    subplot_titles=[name for _, name, _ in datasets])  # Set titles for each subplot

# Add histogram and KDE for each dataset
for i, (data, title, color) in enumerate(datasets):
    row = i + 1  # Determine which row to plot the data on
    # Calculate KDE
    x_vals = np.linspace(data.min(), data.max(), 500)  # Create a range of x values for the KDE
    kde_vals = get_kde(x_vals, data)  # Get the KDE values for the given data

    # Add histogram to the plot
    fig.add_trace(go.Histogram(x=data,
        histnorm='probability density',  # Normalize histogram to represent probability density
        name='Histogram',
        marker_color=color,
        opacity=0.6,
        xbins=dict(size=0.001),  # Bin size
        showlegend=False),  # Don't show legend for the histogram
        row=row, col=1)

    # Add KDE curve to the plot
    fig.add_trace(go.Scatter(
        x=x_vals,
        y=kde_vals,
        mode='lines',  # Line plot for KDE
        line=dict(color='white', width=2),
        name='KDE',
        showlegend=False),  # Don't show legend for the KDE curve
        row=row, col=1)

# Global layout settings
fig.update_layout(height=2600,  # Increase the height of the figure for better visibility
    title="Distributions with Histogram and KDE Curve",  # Title of the plot
    bargap=0.1)  # Gap between bars in the histogram


# Set axis labels for each subplot
for r in range(1, 9):
    fig.update_yaxes(title_text="Density", row=r, col=1)  # Y-axis label for density
    fig.update_xaxes(title_text="Deviation", row=r, col=1)  # X-axis label for deviation

# Display the plot
fig.show()