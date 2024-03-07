import csv

policy_list = [{"name": "Scheme 1", "type": "Type 1", "description": {"detail": "Detail 1", "category": "Category 1"}},
               {"name": "Scheme 2", "type": "Type 2", "description": {"detail": "Detail 2", "category": "Category 2"}},
               {"name": "Scheme 3", "type": "Type 3", "description": {"detail": "Detail 3", "category": "Category 3"}}]

# Flatten the nested dictionary into a string
for scheme in policy_list:
    scheme['description'] = ', '.join(f"{key}: {value}" for key, value in scheme['description'].items())

# Get the fieldnames from the keys of the first dictionary in the list
fieldnames = policy_list[0].keys()

with open("government_schemes.csv", "w", newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write the header
    writer.writeheader()

    # Write the data
    for scheme in policy_list:
        writer.writerow(scheme)
