import sqlite3

connname = 'notepad.db'


class ConnectDb:
    def __init__(self, name_file='notepad.db'):
        self.connstring = f'{name_file}'
        self.all_data = self.select_all_db()
        self.all_data_dict = self.from_sql_to_dict()

    def select_all_db(self):
        conn = sqlite3.connect(self.connstring)
        cursor = conn.cursor()
        data = cursor.execute('''SELECT * FROM notepad''')
        cursor.close()
        conn.close()
        return data

    def clear_db(self):
        conn = sqlite3.connect(self.connstring)
        cursor = conn.cursor()
        cursor.execute('''DELETE FROM notepad;''')
        conn.commit()
        conn.close()

    def update_record(self, id, subject, contents, date):
        conn = sqlite3.connect(self.connstring)
        cursor = conn.cursor()
        cursor.execute(
            f''''UPDATE notepad SET subject = '{subject}', contents = '{contents}', date = '{date}' WHERE id = {id}''')

    def insert_in_db(self, id, subject, contents, date):
        conn = sqlite3.connect(self.connstring)
        cursor = conn.cursor()
        dbstring = f'''INSERT INTO notepad (ID, subject, contents, date) VALUES 
                ({id}, '{subject}', '{contents}', '{date}')'''
        cursor.execute(dbstring)
        conn.commit()
        conn.close()

    def from_sql_to_dict(self):
        conn = sqlite3.connect(self.connstring)
        cursor = conn.cursor()
        data = cursor.execute('''SELECT * FROM notepad''')
        res = {}
        for id, row in enumerate(data):
            res[id] = {
                'subject': row[1],
                'contents': row[2],
                'date': row[3]
            }
        conn.close()
        return res

    def finish(self, data_dict):
        self.clear_db()
        for key, value in data_dict.items():
            self.insert_in_db(key, value["subject"], value["contents"], value["date"])
