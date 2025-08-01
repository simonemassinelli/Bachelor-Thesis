# Since the date_c column is filled with 'object', we convert to datetime values
qc_rows['date_c'] = pd.to_datetime(qc_rows['date_c'])
# Now we can sort our data by date
qc_rows = qc_rows.sort_values(by='date_c')

# Ensuring that there are no duplicates in our dataframe
print(qc_rows.duplicated().sum())

# Check if there are anomalous values
qc_rows_float = qc_rows.select_dtypes(include=['float64'])
min_values = qc_rows_float.min()
max_values = qc_rows_float.max()
summary = pd.DataFrame({
    'Min': min_values,
    'Max': max_values})

# Show the summary
summary