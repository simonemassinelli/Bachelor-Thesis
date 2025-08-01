# Function to select and merge necessary rows and columns
def merge(read_file, qcoffset):

    df = pd.DataFrame(read_file)  # Transforms the input file in a DataFrame

    # Create a new 'row' column to index the rows of the DataFrame
    df['row'] = df.index + 2  # Adds an offset of +2 to match Excel row numbering

    # Select the first row containing the parameter we want to analyze
    first_row = df[df['row'] == qcoffset]

    # Select the name of the parameter
    id = first_row['id'].values[0]

    # Select all the rows of the DataFrame that we need to analyze the parameter
    filtered_df = df[df['id'] == id].copy()

    # We need to create a column containing all the dates, which were first divided in two different 'date' columns
    # due to a formatting error in the dataframe. We fill the empty rows of the firts columns with the dates contained in the second one
    filtered_df['date_c'] = filtered_df['date'].fillna(filtered_df['date.1'])

    # Select only the relevant columns to be returned
    needed_col = filtered_df[['row', 'deviation', 'uppertol', 'lowertol', 'actual', 'nominal', 'date_c']]

    return needed_col  # Returns the relevant columns for the next analysis