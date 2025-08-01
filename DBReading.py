# Get the inputs to call the funcion
read_file = pd.read_pickle('file6.pkl')  # File containing data
qcoffset = 2 # Offset indicating the row of the QC to be analyzed

# Merge the data and get the info to understand the structure
qc_rows = merge(read_file, qcoffset)
qc_rows.info()