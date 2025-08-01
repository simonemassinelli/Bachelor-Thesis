# Function to assign weights
def weight(time_distance, A):
    # Calculate the weight using an exponential decay function
    # A represents the decay rate
    time_distance = np.array(time_distance)  # Convert input to NumPy array
    return np.exp(-A * time_distance)  # Exponential decay weighting

# Create a list representing time distances from 0 to 15
dists = [i for i in range(11)]  # Time distances from 0 to 10 days

# Apply the weight function to generate z-values for the 3D surface plot
weights = weight(dists, 0.1)  # Compute weights with decay rate A

# Create a 3D surface plot using Plotly
fig = go.Figure(data=go.Scatter(x=dists, y=weights))  # Plot weights vs time distance

# Customize the layout with titles for the axes and the plot
fig.update_layout(title='Weight based on time distance',  # Plot title
        xaxis_title='Days',  # X-axis label
        yaxis_title='Weight')  # Y-axis label

# Display the plot
fig.show()