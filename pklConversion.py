def conversion(file_path, output_file):
    df = pd.read_excel(file_path, engine='odf')  # Reads the ODS file and converts it into a DataFrame
    df.to_pickle(output_file)  # Saves the DataFrame in pickle format

# Giving inputs to the function
conversion(r'C:\Users\casam\OneDrive\Desktop\Simone\Tesi\MERGE\data.3.ods', 'file6.pkl')