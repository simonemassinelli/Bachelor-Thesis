# Define Cpk thresholds for warning and critical levels
cpk_threshold_warning = 1.33  # Warning threshold for Cpk
cpk_threshold_critical = 1.00  # Critical threshold for Cpk

# Create a figure to visualize the Cpk values over time
fig = go.Figure()

# Iterate through the datasets for each machine to prepare the data and generate the plot
for idx, df in enumerate(all_data):
    df_valid = df.dropna(subset=['cpk'])  # Remove rows where Cpk is NaN

    # List to store colors for markers based on Cpk values
    colors = []
    for cpk in df_valid['cpk']:
        if cpk < cpk_threshold_critical:
            colors.append('red')  # Cpk below the critical threshold (red)
        elif cpk < cpk_threshold_warning:
            colors.append('orange')  # Cpk between the critical and warning thresholds (orange)
        else:
            colors.append('green')  # Cpk above the warning threshold (green)

    # Add a trace to the figure using the date and Cpk values
    fig.add_trace(go.Scatter(x=df_valid['day'], y=df_valid['cpk'], mode='lines+markers',
                            marker=dict(color=colors, size=6), line=dict(width=2, dash='solid'), name=f'Machine {idx+1}'))

# Add horizontal lines to indicate the critical and warning thresholds
fig.add_hline(y=cpk_threshold_critical, line_dash='dash', line_color='red')
fig.add_hline(y=cpk_threshold_warning, line_dash='dash', line_color='orange')

# Add rectangles to visually highlight the critical, warning, and normal regions
fig.add_hrect(y0=cpk_threshold_critical, y1=cpk_threshold_warning, fillcolor='rgba(255, 165, 0, 0.2)', line_width=0)
fig.add_hrect(y0=0, y1=cpk_threshold_critical, fillcolor='rgba(255, 0, 0, 0.2)', line_width=0)
fig.add_hrect(y0=cpk_threshold_warning, y1=12, fillcolor='rgba(0, 255, 0, 0.2)', line_width=0)

# Update the layout of the figure
fig.update_layout(title='Cpk over Time',
                  xaxis_title='Date',
                  yaxis_title='Cpk',
                  xaxis=dict(showgrid=True),
                  yaxis=dict(showgrid=True, zeroline=True, zerolinecolor='black'))

# Add annotations to explain the threshold lines
fig.add_annotation(
    text='- - - → Cpk = 1.33 → Warning',
    xref='paper', yref='paper',  # Coordinates relative to the plot
    x=0.95, y=0.9,  # Position (top right)
    showarrow=False,
    font=dict(size=14, color='orange'),  # Orange text for warning
    borderwidth=1)

fig.add_annotation(
    text='- - - → Cpk = 1.00 → Critical',
    xref='paper', yref='paper',
    x=0.95, y=0.75,  # Slightly lower position
    showarrow=False,
    font=dict(size=14, color='red'),  # Red text for critical
    borderwidth=1)

# Display the plot
fig.show()