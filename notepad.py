from datetime import datetime

from Notes import Notes

notes = Notes()

PBVERSION = '1.0'


def get_notes():
    data_dict = notes.get_all()
    print("Ключ", "Тема", "Содержание", "Дата", sep="\t")
    for key, value in data_dict.items():
        print(key, value['subject'], value['contents'], value['date'], sep="\t")


def add_record():
    data_list = []
    data_list.append(input('Введите тему: '))
    data_list.append(input('Введите содержание: '))
    data_list.append(str(datetime.now().date()))
    notes.add_note(data_list)
    notes.end()


def update_record():
    data_list = []
    ID = input("Введите ID: ")
    data = notes.search_by_ID(int(ID))
    if not data:
        print('Запись не найдена')
    else:
        data_list.append(input('Введите тему: '))
        data_list.append(input('Введите содержание: '))
        data_list.append(str(datetime.now().date()))
        notes.change_by_id(int(ID), data_list)
    notes.end()


def export():
    while True:
        file_name = input('Введите имя файла (без расширения): ')
        file_type = input('Введите расширение (json / csv, json - по умолчанию): ')
        temp = notes.export_notes(file_name, file_type)
        if temp is not False:
            break


def import_data():
    while True:
        file_name = input('Введите имя файла (с расширением): ')
        file_type = input('Введите расширение (json / csv / sql, json - по умолчанию): ')
        temp = notes.import_notes(file_name, file_type)
        if temp is not False:
            notes.end()
            break


def search():
    ln = input('Введите дату ("год-месяц-день"): ')
    data = notes.search_by_date(ln)
    if data == []:
        print('Запись не найдена')
    else:
        print("Ключ", "Тема", "Содержание", "Дата", sep="\t")
        for key, value in data.items():
            print(key, value['subject'], value['contents'], value['date'], sep="\t")


def delete_record():
    while True:
        id_ = input('Введите ID: ')
        if id_.isdigit():
            notes.delete_by_id(id_)
            notes.end()
            break


def purge_database():
    notes.clear_all()
    notes.end()


def exit_notebook():
    notes.end()
    exit()


def check_menu():
    print('Работает функция')


def check_numeric(message, min_, max_):
    out = -100
    check = False
    while not check or out > max_ or out < min_:
        str_out = input(message)
        if not str_out.isdigit():
            check = False
        else:
            out = int(str_out)
            check = True
    return out


def main_menu():
    print(f"Телефонный справочник: {PBVERSION}")
    options = {1: "Добавление записей",
               2: "Изменение записи",
               3: "Вывод всех записей",
               4: "Импорт",
               5: "Экспорт",
               6: "Удаление записей",
               7: "Поиск по дате",
               8: "Завершить работу",
               9: "Очистка базы"
               }
    functions = {1: add_record,
                 2: update_record,
                 3: get_notes,
                 4: import_data,
                 5: export,
                 6: delete_record,
                 7: search,
                 8: exit_notebook,
                 9: purge_database}
    for iter in options.keys():
        print(iter, options[iter])
    option = check_numeric("Выберите действие: ", 1, 10)
    print("Выбрано: ", options[option])
    functions[option]()  # можно передавать без аргумента "()"

    user_dec = input('Продолжить - Enter, выйти - exit: ')
    if user_dec == 'exit':
        exit_notebook()
    else:
        main_menu()
    return option


main_menu()
