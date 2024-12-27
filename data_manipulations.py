import os
import pandas as pd

def convert_and_process_files(csv_file, json_file, xml_file):
    try:
        # Check if input CSV file exists
        if not os.path.exists(csv_file):
            print(f"CSV file not found: {csv_file}")
            return

        # Read CSV file
        df = pd.read_csv(csv_file)
        print("Data from CSV:")
        print(df)

        # Write to JSON
        try:
            df.to_json(json_file, orient="records", lines=True)
            print(f"Data written to JSON: {json_file}")
        except Exception as e:
            print(f"Failed to write to JSON: {e}")

        # Write to XML
        try:
            df.to_xml(xml_file, index=False)
            print(f"Data written to XML: {xml_file}")
        except Exception as e:
            print(f"Failed to write to XML: {e}")

        # Read JSON file
        try:
            df_from_json = pd.read_json(json_file, orient="records", lines=True)
            print("Data from JSON:")
            print(df_from_json)
        except Exception as e:
            print(f"Failed to read JSON: {e}")

        # Read XML file
        try:
            df_from_xml = pd.read_xml(xml_file)
            print("Data from XML:")
            print(df_from_xml)
        except Exception as e:
            print(f"Failed to read XML: {e}")

        # Write back to CSV
        try:
            json_csv_file = "data_from_json.csv"
            xml_csv_file = "data_from_xml.csv"
            df_from_json.to_csv(json_csv_file, index=False)
            df_from_xml.to_csv(xml_csv_file, index=False)
            print(f"Data written back to CSV from JSON: {json_csv_file}")
            print(f"Data written back to CSV from XML: {xml_csv_file}")
        except Exception as e:
            print(f"Failed to write back to CSV: {e}")

    except Exception as e:
        print(f"Error processing files: {e}")

# Example usage
#convert_and_process_files("data/data.csv", "data/data.json", "data/data.xml")
