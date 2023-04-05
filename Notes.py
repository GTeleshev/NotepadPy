import csv
import json

from ConnectDb import ConnectDb


class Notes:
    def __init__(self):
        self.connect = ConnectDb()
        self.all_notes = self.connect.all_data_dict

    def add_note(self, data):
        self.all_notes[max([int(item) for item in self.all_notes.keys()]) + 1 if self.all_notes != {} else 0] = {
            'subject': data[0],
            'contents': data[1],
            'date': data[2]
        }

    def import_notes(self, name_file, type='json'):
        if type not in ["csv", "json"]:
            return False
        if type == "json":
            with open(name_file, "r", encoding="utf-8") as f:
                for key, value in json.load(f).items():
                    self.all_notes[
                        max([int(item) for item in self.all_notes.keys()]) + 1 if self.all_notes != {} else 0] = {
                        'subject': value["subject"],
                        'contents': value["contents"],
                        'date': value["date"]
                    }
        if type == "csv":
            with open(name_file, newline="") as f:
                reader = csv.reader(f)
                for row in reader:
                    self.all_notes[
                        max([int(item) for item in self.all_notes.keys()]) + 1 if self.all_notes != {} else 0] = {
                        'subject': row[0],
                        'contents': row[1],
                        'date': row[2]
                    }

    def export_json(self, file, type='json'):
        with open(f"{file}.json", "w", encoding="utf-8") as f:
            json.dump(self.all_notes, f, indent=4, ensure_ascii=False)

    def get_all(self):
        return self.all_notes

    def delete_by_id(self, id):
        del self.all_notes[int(id)]

    def change_by_id(self, id, data):
        if id in self.all_notes.keys():
            self.all_notes[id] = {
                'subject': data[0],
                'contents': data[1],
                'date': data[2]
            }
            return True
        else:
            return False

    def clear_all(self):
        self.all_notes = {}
        self.connect.clear_db()

    def end(self):
        self.connect.finish(self.all_notes)

    def search_by_ID(self, ID):
        res = []
        for key, value in self.all_notes.items():
            if key == ID:
                temp = {}
                temp[key] = value
                res.append(temp)
        return res

    def search_by_date(self, date):
        res = {}
        for key, value in self.all_notes.items():
            if value['date'].lower() == date.lower():
                temp = {key: value}
                res.update(temp)
        return res

    def export_notes(self, name_file, type="json"):
        if type not in ["csv", "json"]:
            return False
        if type == "json":
            with open(f"{name_file}.json", "w", encoding="utf-8") as f:
                json.dump(self.all_notes, f, indent=4, ensure_ascii=False)
        if type == "csv":
            with open(f"{name_file}.csv", "w") as f:
                writer = csv.writer(f, delimiter=";")
                for key, value in self.all_notes.items():
                    writer.writerow([value["subject"], value["contents"], value["date"]])