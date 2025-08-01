# Path to the ZIP folder containing the compressed data
zip_path = r'C:\Users\casam\Downloads\simone.zip'

# Path to the output folder where the modified files will be saved
output_folder = r'C:\Users\casam\OneDrive\Desktop\Simone\Tesi\MERGE\DATI 3'

# Open the ZIP file in read mode
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    # Retrieve the list of all files contained in the ZIP archive
    file_list = zip_ref.namelist()

    # Filter the files, only returning the ones with the specified name.
    # This needs to be done because we only want to select files which refer to the same component
    chr_files = [f for f in file_list if fnmatch.fnmatch(f, 'chr/N739584*_chr.txt')]

    # Iterate over the filtered list of files
    for file in chr_files:
        # Retrieve file metadata to get the last modified date
        info = zip_ref.getinfo(file)

        # Convert the last modified date from tuple format to a human-readable string
        last_modified_date = datetime(*info.date_time).strftime('%Y-%m-%d %H:%M:%S')

        # Open each compressed file directly from the ZIP folder
        with zip_ref.open(file) as f:
            # Read the content of the file into a pandas DataFrame
            # To read it correcly, pandas needs all the informations
            # such as the fact that are TSV files (sep='\t') and so on
            df = pd.read_csv(f, sep='\t', dtype=str, encoding='latin1')

        # Add a new column 'date' to store the last modified date of the original file
        df['date'] = last_modified_date

        # Construct the new file path with a modified name
        new_file = os.path.join(output_folder, os.path.basename(file).replace('_chr', '_modified.chr'))

        # Save the modified DataFrame as a new TSV file in the output folder
        df.to_csv(new_file, sep='\t', index=False)