import csv

rows = []

with open('filtered_data.csv', 'r') as f:
    csvreader = csv.reader(f)
    for i in csvreader:
        rows.append(i)

headers = rows[0]
star_data_rows = rows[1:]

final_dict = []

final_star_list = []
for star_data in star_data_rows:
  temp_dict = {
      "name":star_data[2],
      "distance":star_data[3],
      "mass":star_data[4],
      "radius":star_data[5],
      "gravity":star_data[6],
  }
  final_dict.append(temp_dict)

print(list(final_dict))