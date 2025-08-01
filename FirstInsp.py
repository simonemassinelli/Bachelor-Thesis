# Create a line plot with the date on the x-axis and the deviation on the y-axis
fig = px.line(qc_rows, x='date_c', y='deviation', markers=True, title='Deviation of Components in Time')
fig.update_traces(line=dict(color='gray'))

UT = qc_rows['uppertol'].iloc[0]
LT = qc_rows['lowertol'].iloc[0]

# Add the upper tolerance line (constant value) to the chart
fig.add_trace(go.Scatter(
    x=[qc_rows['date_c'].min(), qc_rows['date_c'].max()],
    y=[UT, UT],
    mode='lines',
    line=dict(color='red', dash='dash'),
    name='Upper Tolerance'))

# Add the lower tolerance line (constant value) to the chart
fig.add_trace(go.Scatter(
    x=[qc_rows['date_c'].min(), qc_rows['date_c'].max()],
    y=[LT, LT],
    mode='lines',
    line=dict(color='red', dash='dash'),
    name='Lower Tolerance'))

# Add names to the axis of the graph
fig.update_layout(xaxis_title='Date', yaxis_title='Deviation from Nominal Value')

# Display the chart
fig.show()