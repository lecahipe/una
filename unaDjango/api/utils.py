import csv, json

from django.http import FileResponse

class ExportClass:
    '''
        Export data in either CSV or JSON format
    '''
    def export_csv(self, data):
        with open('export.csv', 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())
            writer.writeheader()
            for row in data:
                writer.writerow(row)
        return FileResponse(open('export.csv', 'rb'), as_attachment=True, filename='export.csv')

    def export_json(self, data):
        with open('export.json', 'w') as json_file:
            json.dump(data, json_file)
        return FileResponse(open('export.json', 'rb'), as_attachment=True, filename='export.json')