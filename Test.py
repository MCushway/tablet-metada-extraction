import os
import csv
import xml.etree.ElementTree as ET
from tkinter import Tk, filedialog

os.chdir(os.path.expanduser("~"))

root = Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title="Choose your Tableau workbook"
)

root.destroy()

print("Workbook selected:")
print(file_path)

tree = ET.parse(file_path)
workbook = tree.getroot()

print("\nWorksheets found:")

for worksheet in workbook.findall(".//worksheets/worksheet"):
    print("-", worksheet.get("name"))
    
print("\nDashboards found:")

for dashboard in workbook.findall(".//dashboards/dashboard"):
    print("-", dashboard.get("name"))

print("\nData sources found:")

data_sources = set()

for datasource in workbook.findall(".//datasources/datasource"):
    name = datasource.get("caption") or datasource.get("name")

    if name and name != "Parameters":
        data_sources.add(name)

for name in sorted(data_sources):
    print("-", name)

print("\nFields found:")

fields = set()

for datasource in workbook.findall(".//datasources/datasource"):
    datasource_name = datasource.get("caption") or datasource.get("name")

    if not datasource_name or datasource_name == "Parameters":
        continue

    for column in datasource.findall("./column"):
        field_name = column.get("caption") or column.get("name")
        data_type = column.get("datatype")
        role = column.get("role")

        if field_name:
            fields.add((field_name, data_type, role))

for field_name, data_type, role in sorted(fields):
    print("-", field_name, "|", data_type, "|", role)

print("\nCalculated fields found:")

calculated_fields = set()

for datasource in workbook.findall(".//datasources/datasource"):

    for column in datasource.findall("./column"):

        calculation = column.find("calculation")

        if calculation is not None:

            field_name = column.get("caption") or column.get("name")
            formula = calculation.get("formula")

            if field_name and formula:
                calculated_fields.add((field_name, formula))

for field_name, formula in sorted(calculated_fields):
    print("-", field_name)
    print("  Formula:", formula)

output_path = os.path.join(
    os.path.dirname(file_path),
    "tableau_metadata_report.csv"
)

with open(output_path, "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    writer.writerow([
        "Metadata Type",
        "Name",
        "Data Type",
        "Role",
        "Formula"
    ])

    for worksheet in workbook.findall(".//worksheets/worksheet"):
        writer.writerow([
            "Worksheet",
            worksheet.get("name"),
            "",
            "",
            ""
        ])

    for dashboard in workbook.findall(".//dashboards/dashboard"):
        writer.writerow([
            "Dashboard",
            dashboard.get("name"),
            "",
            "",
            ""
        ])

    for name in sorted(data_sources):
        writer.writerow([
            "Data Source",
            name,
            "",
            "",
            ""
        ])

    for field_name, data_type, role in sorted(fields):
        writer.writerow([
            "Field",
            field_name,
            data_type,
            role,
            ""
        ])

    for field_name, formula in sorted(calculated_fields):
        writer.writerow([
            "Calculated Field",
            field_name,
            "",
            "",
            formula
        ])

print("\nCSV report created successfully!")
print(output_path)


