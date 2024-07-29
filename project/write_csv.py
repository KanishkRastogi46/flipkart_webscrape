import csv


def write_to_csv(path, content):
    with open(path, 'w', encoding="utf-8", newline="") as fp:
        data_fields = ["Phone Name", "Phone Current Price"]
        writer = csv.DictWriter(fp, fieldnames=data_fields)
        writer.writeheader()
        for item in content:
            writer.writerow({"Phone Name":item[0], "Phone Current Price": item[1]})


if __name__=="__main__":
    print(__name__)