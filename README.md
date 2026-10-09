# Tableau Metadata Extraction

I created this project to practice using Python with Tableau and to learn how workbook metadata can be extracted automatically.

For the test, I used Tableau's Sample Superstore workbook.

The Python script reads the Tableau `.twb` file and pulls information such as:

- Worksheets
- Dashboards
- Data sources
- Fields
- Data types
- Dimensions and measures
- Calculated fields
- Formulas

The program then exports the results into a CSV file called:

`tableau_metadata_report.csv`

The CSV includes:

- Metadata Type
- Name
- Data Type
- Role
- Formula

## How it works

1. Select a Tableau workbook.
2. Python reads the workbook XML.
3. The script extracts the metadata.
4. Duplicate values are cleaned.
5. The results are exported to CSV.

## Tools used

- Python
- Tableau Desktop
- XML
- CSV
- GitHub

This project helped me understand how Python can be used to automate Tableau workbook analysis and metadata extraction.# tablet-metada-extraction
python to extract metadata from tables file
