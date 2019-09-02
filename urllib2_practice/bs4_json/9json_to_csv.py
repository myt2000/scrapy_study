import csv
import json

def json_to_csv():
    json_file = open("8tencent.json", "r", encoding="utf-8")

    csv_file = open("9tencent_job.csv", "w", encoding="utf-8")

    csv_writer = csv.writer(csv_file)

    data = json.load(json_file)

    sheet_title = data[0].keys()

    content_list = []
    for job in data:
        content_list.append(job.values())

    content_list = [job.values() for job in data]

    csv_writer.writerow(sheet_title)
    csv_writer.writerows(content_list)

    json_file.close()
    csv_file.close()

if __name__ == "__main__":
    json_to_csv()