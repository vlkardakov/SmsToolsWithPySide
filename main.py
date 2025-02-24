import os
import subprocess
import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QTableWidget
from openpyxl import load_workbook, Workbook

import settings
from ui_main import Ui_MainWindow


class SmsTools(QMainWindow):
    def __init__(self):
        super(SmsTools, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.sendButton.clicked.connect(self.get_selected_numbers)
        self.ui.add_contact.clicked.connect(self.add_contacts)

        #self.ui.message.keyPressEvent = self.keyPressEvent
        #self.ui.arguments.keyPressEvent = self.keyPressEvent

        self.ui.search.clicked.connect(self.load_contacts)
        self.ui.settings.clicked.connect(self.openSettings)
    def add_contacts(self):
        print("Начинаю добавление...")
        file_path = "Files/contacts.xlsx"
        number = self.ui.number.toPlainText()
        name = self.ui.name.toPlainText()

        contact = [name, number]

        # создаем каталог, если он не существует
        directory = os.path.dirname(file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        if os.path.exists(file_path):
            # загружаем существующий файл
            wb = load_workbook(file_path)
            ws = wb.active
        else:
            # создаем новый файл и заполняем заголовки
            wb = Workbook()
            ws = wb.active
            ws.title = "Contacts"
            ws.append(["Phone Number", "Contact Name"])


        ws.append(contact)

        wb.save(file_path)

        self.load_contacts()
        print(f"Контакты успешно добавлены в {file_path}")
        return None
    def openSettings(self):
        #app = #QApplication(sys.argv)
        self.settingsWindow = settings.Settings()
        self.settingsWindow.show()


    def delete_contact(self, nums):
        ii = 0
        try:
            # Загружаем файл
            wb = load_workbook("Files/contacts.xlsx")
            ws = wb.active
            # находим все для удаления в обратном порядке
            rows_to_delete = []
            for row in range(ws.max_row, 1, -1):  # начинаем с конца, пропускаем заголовок
                if f"+7{ws.cell(row=row, column=1).value}" in nums:
                    ii += 1
                    rows_to_delete.append(row)

            #удаляем
            for row_idx in rows_to_delete:
                ws.delete_rows(row_idx, 1)

            #Сохраняем
            wb.save("Files/contacts.xlsx")
            return True, f"{ii} Контактов успешно удалено"

        except Exception as e:
            return False, f"Ошибка при удалении контакта: {str(e)}"
    def read_settings(self):
        settings_file = "Files/settings.txt"
        if not os.path.exists(settings_file):
            print(f"Файл {settings_file} не существует.")
            exit()
        settings = {}
        with open(settings_file, 'r') as file:
            for line_num, line in enumerate(file, start=1):
                line = line.strip()
                if not line or '=' not in line:
                    continue
                try:
                    name, value = line.split('=', 1)
                    settings[name.strip()] = value.strip()
                except ValueError as e:
                    print(f"Ошибка в строке {line_num}: '{line}', ошибка: {e}")
                    continue
        return settings
    def get_selected_numbers(self):
        selected_rows = set()
        for index in self.ui.contacts.selectedIndexes():
            selected_rows.add(index.row())

        first_column_data = []
        for row in selected_rows:
            item = self.ui.contacts.item(row, 0)
            if item is not None:
                first_column_data.append(item.text())

        #self.conprint(f"Выделено {(first_column_data)}")  # Выводим в консоль (можно использовать иначе)
        return first_column_data

    def open_files_folder(self):
        # Открывает папку 'Files' в текущем каталоге в проводнике.

        try:
            # Определяем путь к папке 'Files'
            current_directory = os.getcwd()
            folder_path = os.path.join(current_directory, 'Files')

            # Проверяем, существует ли папка
            if not os.path.isdir(folder_path):
                print(f"Папка не существует: {folder_path}")
                return

            # Открываем папку в проводнике
            if os.name == 'nt':  # Windows
                subprocess.run(['explorer', folder_path], check=True)
            elif os.name == 'posix':  # macOS or Linux
                if sys.platform == 'darwin':  # macOS
                    subprocess.run(['open', folder_path], check=True)
                else:  # Linux
                    subprocess.run(['xdg-open', folder_path], check=True)
            else:
                print(f"Операционная система не поддерживается: {os.name}")

        except subprocess.CalledProcessError as e:
            print('', end='')
        except Exception as e:
            print('', end='')

    def keyPressEvent(self, event):
        """Обрабатывает нажатие клавиши"""
        if self.ui.contacts.hasFocus():
            if event.key() == Qt.Key_Escape:
                print("Очистка.")
                self.ui.contacts.clearSelection()
            elif event.key() == Qt.Key_Backspace:
                numbers = self.get_selected_numbers()
                print(f"Удаление {len(numbers)} контактов..")
                self.delete_contact(numbers)
                self.ui.contacts.clearSelection()
                self.load_contacts()
            else:
                print(event)



    def search_contacts(self, file_path, search_terms):
        wb = load_workbook(file_path)
        ws = wb.active

        if search_terms == "":
            search_terms = ["9", "8", "7", "6", "5", "4", "3", "2", "1", "0"]
        else:
            search_terms = search_terms.split()

        final_strings = []

        for search_term in search_terms:
            if not search_term.startswith("-"):
                for row in ws.iter_rows(min_row=2, values_only=True):
                    phone_number, contact_name = row
                    if phone_number:
                        string = f"{phone_number}::{contact_name}".replace(" ", "")
                        if search_term in string and string not in final_strings:
                            final_strings.append(string)
            else:
                argument = search_term.replace("-", "")
                for final_string in final_strings[:]:  # Используем копию списка
                    if argument in final_string:
                        final_strings.remove(final_string)

        contacts_found = [{"num": f"+7{num}", "name": name} for num, name in
                          (s.split("::") for s in final_strings)]

        if not contacts_found:
            return []

        return contacts_found
    def load_contacts(self, search_terms = None):
        file_path = "Files/contacts.xlsx"  # Укажите путь к файлу
          # Получаем текст из `TextEdit`
        if not search_terms:
            search_terms = self.ui.arguments.text()
        contacts = self.search_contacts(file_path, search_terms)  # Получаем список контактов

        self.populate_table(contacts)  # Заполняем таблицу

    def populate_table(self, contacts):
        self.ui.contacts.setRowCount(len(contacts))
        self.ui.contacts.setColumnCount(2)
        self.ui.contacts.setHorizontalHeaderLabels(["Номер", "Имя"])

        self.ui.contacts.setColumnWidth(0, 90)  # Номер телефона
        self.ui.contacts.setColumnWidth(1, 81)  # Имя
        self.ui.contacts.verticalHeader().setDefaultSectionSize(30)  # Высота строк

        self.ui.contacts.setSelectionBehavior(QTableWidget.SelectRows)

        self.ui.contacts.horizontalHeader().hide()
        self.ui.contacts.verticalHeader().hide()

        for row, contact in enumerate(contacts):
            self.ui.contacts.setItem(row, 0, QTableWidgetItem(contact["num"]))
            self.ui.contacts.setItem(row, 1, QTableWidgetItem(contact["name"]))

    def conprint(self, text):
        self.ui.console.setText(f"{self.ui.console.toPlainText()}\n{text}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SmsTools()
    window.show()
    window.load_contacts(search_terms="1")

    sys.exit(app.exec())
