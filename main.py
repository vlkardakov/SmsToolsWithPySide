import os, psutil, sys, subprocess, serial, time
import pandas as pd
from Continue import Continue
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QTableWidget
from openpyxl import load_workbook, Workbook

from openpyxl.styles import Alignment, PatternFill
from datetime import datetime, timedelta
import settings
from ui_main import Ui_MainWindow
from Notification import Notification


class SmsTools(QMainWindow):
    def __init__(self):
        super(SmsTools, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)



        # Чтение настроек
        self.settings = self.read_settings()
        self.settings.port = None # Настроить


        # Инициализация модема
        self.kill_connect_manager() # Отключение коннект-менеджера
        with serial.Serial(self.settings['port'], self.settings['speed'], timeout=1) as ser: # Подключение к модему
            self.send_at_command(ser, 'AT+CMGF=1') # Задание текстового формата
            self.send_at_command(ser, 'AT+CPMS="ME","ME","ME"') # переключение на внутреннюю память


        #

        # Привязка кнопок
        self.ui.sendButton.clicked.connect(self.get_selected_numbers)
        self.ui.add_contact.clicked.connect(self.add_contacts)
        self.ui.analyze.clicked.connect(self.menu_analysis)
        self.ui.open_folder.clicked.connect(self.open_files_folder)
        self.ui.save.clicked.connect(self.edit_contacts)
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

    def restart_modem(self):
        with serial.Serial(modem_port, self.settings['speed'], timeout=1) as ser:
            res = self.send_at_command(ser, 'AT+CFUN=1,1')
            return True if "OK" in res else False

    def kill_connect_manager(self):
        try:
            # Ищем процесс Connect Manager
            for proc in psutil.process_iter(['name']):
                if proc.info['name'] and 'Connect Manager.exe' in proc.info['name']:
                    # print(f"Найден процесс Connect Manager (PID: {proc.pid})")
                    # Принудительно завершаем процесс
                    proc.kill()
                    # print("Процесс успешно завершен")
                    return True

            # print("Процесс Connect Manager.exe не найден")
            return False

        except Exception as e:
            print(f"Произошла ошибка: {e}")
            return False
    def menu_analysis(self):
        if Continue("Анализировать данные?", "Нет", "Да").get_choice():
            self.analysis()
            Notification("Анализ завершён.")
    def openSettings(self): # Открывает настройки
        self.settingsWindow = settings.Settings()
        self.settingsWindow.show()
    def send_at_command(self, ser, command, response_timeout=1): # Отправляет команду на порт через уже активное подключение
        ser.write((command + '\r\n').encode())
        time.sleep(response_timeout)
        response = ser.read_all().decode()
        return response



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

    def load_sms_log(self, filename):
        try:
            df = pd.read_excel(filename)
            df = df.drop_duplicates()
            df['Сообщение'] = df['Сообщение'].astype(str)
            #print("Загруженные столбцы:", df.columns)
        except Exception as e:
            print(f"Ошибка при чтении файла SMS логов: {e}")
            return pd.DataFrame()
        return df

    def analyze_sms_log(self, contacts_file, sms_log_file, analysis_file):
        contacts = self.search_contacts(contacts_file, "0 1 2 3 4 5 6 7 8 9")
        sms_log = self.load_sms_log(sms_log_file)

        if sms_log.empty:
            print(f"Список сообщений пуст.")
            return
        if not contacts:
            print(f"Не удалось загрузить контакты.")
            return
        #Получение даты и времени
        today_date, current_time = self.get_current_datetime()
        yesterday_date = (datetime.now() - timedelta(days=1)).strftime('%d/%m/%Y')

        #Используем индексаци
        phone_column_index = 0  # Индекс столбца с номерами телефонов
        date_column_index = 3  # Индекс столбца с датой получения SMS

        #Проверка типов
        sms_log.iloc[:, phone_column_index] = sms_log.iloc[:, phone_column_index].astype(str)
        sms_log.iloc[:, date_column_index] = pd.to_datetime(sms_log.iloc[:, date_column_index], format='%d/%m/%Y',
                                                            errors='coerce').dt.strftime('%d/%m/%Y')

        #получаем номера телефонов, которые отправляли SMS за последние сутки
        recent_sms = sms_log[sms_log.iloc[:, date_column_index].isin([today_date, yesterday_date])]
        recent_sms_numbers = recent_sms.iloc[:, phone_column_index].str.replace(' ', '').str.replace('-', '').replace(
            "+7", "").unique()

        #определяем контакты, которые не прислали SMS за последние сутки
        missing_contacts = {number: name for number, name in contacts.items() if number not in recent_sms_numbers}

        #определяем номер анализа
        try:
            with open(analysis_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                last_analysis_number = None
                for line in reversed(lines):
                    if line.startswith('Анализ номер '):
                        last_analysis_number = int(line.strip().split('Анализ номер ')[-1].split()[0])
                        break
                if last_analysis_number is None:
                    new_analysis_number = 1
                else:
                    new_analysis_number = last_analysis_number + 1
        except FileNotFoundError:
            new_analysis_number = 1

        # Запись результатов в файл
        analysis_content = f"Анализ номер {new_analysis_number}\n"
        analysis_content += f"Дата: {today_date}, время: {current_time}.\n"
        analysis_content += "Контакты, не приславшие сообщение за последние сутки:\n\n"
        for number, name in missing_contacts.items():
            if len(number) == 11 and not number.startswith('8'):
                analysis_content += f"+{number} -- {name}\n"
            else:
                analysis_content += f"{number} -- {name}\n"

        # Анализ сообщений
        settings = self.read_settings()
        charge_warning = int(settings.get('charge_warning', 0))
        wb = load_workbook("Files/sms_log.xlsx", data_only=True)
        ws = wb.active

        # Очистка 7-го столбца
        for row in ws.iter_rows(min_row=2, values_only=False):
            row[5].value = ""

        # Добавляем столбец "Отклонения", если его нет
        if ws.max_column < 6:
            ws['G1'] = 'Отклонения'

        for row in ws.iter_rows(min_row=2, values_only=False):
            message = row[2].value
            if isinstance(message, str):  # Проверяем, является ли сообщение строкой
                deviations = row[5].value if row[5].value else ""
                battery_warning = False
                gps_warning = False
                for line in message.splitlines():
                    if "Спутн: 0" in line:
                        gps_warning = True
                    if "Бат:" in line:
                        battery_level = int(line.split("(")[1].split("%")[0])
                        if battery_level < charge_warning:
                            battery_warning = True
                if battery_warning:
                    deviations += "Бат! "
                if gps_warning:
                    deviations += "GPS! "
                row[5].value = deviations

                # Устанавливаем цвет фона для 7-го столбца
                if "Бат! GPS! " in deviations:
                    row[5].fill = PatternFill(start_color='FFFF950E', end_color='FFFF950E', fill_type='solid')
                elif "GPS! " in deviations:
                    row[5].fill = PatternFill(start_color='FFF0F076', end_color='FFF0F076', fill_type='solid')
                elif "Бат! " in deviations:
                    row[5].fill = PatternFill(start_color='FFAFEEEE', end_color='FFAFEEEE', fill_type='solid')

        # Установка белой заливки для пустых ячеек в 7-м столбце
        for row in ws.iter_rows(min_row=2, values_only=False):
            if row[5].value is None or row[5].value == "":
                row[5].fill = PatternFill(start_color='FFFFFF', end_color='FFFFFF', fill_type='solid')

        wb.save(sms_log_file)

        with open(analysis_file, 'a', encoding='utf-8') as f:
            f.write("\n\n")
            f.write(analysis_content)

        print(f"Анализ номер {new_analysis_number} успешно добавлен в файл {analysis_file}.")

    def analysis(self):
        # анализирует
        contacts_file = "Files/contacts.xlsx"
        sms_log_file = "Files/sms_log.xlsx"
        analysis_file = "Files/Analysis.txt"
        self.analyze_sms_log(contacts_file, sms_log_file, analysis_file)


    def keyPressEvent(self, event):
        """Обрабатывает нажатие клавиши"""
        if self.ui.contacts.hasFocus():
            if event.key() == Qt.Key_Escape:
                print("Очистка.")
                self.ui.contacts.clearSelection()
            elif event.key() == Qt.Key_Backspace:
                numbers = self.get_selected_numbers()
                if Continue(f"Удалить выделенные контакты ({len(numbers)})?", "Нет", "Да").get_choice():
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
        file_path = "Files/contacts.xlsx"
        if not search_terms:
            search_terms = self.ui.arguments.text()
        contacts = self.search_contacts(file_path, search_terms)  # Получаем список контактов

        self.populate_table(contacts)
        return contacts

    def edit_contacts(self):
        if Continue(f"Сохранить контакты?", "Нет", "Да").get_choice():
            edited_contacts = self.get_displayed_contacts()
            file_path = "Files/contacts.xlsx"
            all_contacts = self.search_contacts(file_path, "0 1 2 3 4 5 6 7 8 9")  # Получаем список контактов

            # Создаем словарь, где ключ — это номер телефона, а значение — новое имя
            edited_dict = {contact['num']: contact['name'] for contact in edited_contacts}

            # Обновляем all_contacts, если номер найден в edited_dict
            for contact in all_contacts:
                if contact['num'] in edited_dict:
                    contact['name'] = edited_dict[contact['num']]
            #print(edited_contacts)

            self.rewrite_contacts(all_contacts)
            # self.load_contacts()

    def rewrite_contacts(self, contacts):
        file_path = "Files/contacts.xlsx"
        wb = Workbook()
        ws = wb.active
        ws.title = "Контакты"
        ws.append(["Номер телефона", "Имя маячка"])  # Заголовки

        for contact in contacts:
            ws.append([contact["num"].replace("+7", ""), contact["name"]])

        wb.save(file_path)

    def get_displayed_contacts(self):
        contacts = []
        for row in range(self.ui.contacts.rowCount()):
            num_item = self.ui.contacts.item(row, 0)  # Получаем номер
            name_item = self.ui.contacts.item(row, 1)  # Получаем имя

            if num_item and name_item:  # Проверяем, что ячейки не пустые
                contacts.append({"num": num_item.text(), "name": name_item.text()})

        return contacts

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
            # Устанавливаем номер телефона (запрещаем редактирование)
            phone_item = QTableWidgetItem(contact["num"])
            phone_item.setFlags(phone_item.flags() & ~Qt.ItemIsEditable)  # Убираем флаг редактирования
            self.ui.contacts.setItem(row, 0, phone_item)

            # Устанавливаем имя (разрешаем редактирование)
            name_item = QTableWidgetItem(contact["name"])
            self.ui.contacts.setItem(row, 1, name_item)

    def conprint(self, text):
        self.ui.console.setText(f"{self.ui.console.toPlainText()}\n{text}")


if __name__ == "__main__":
    # print(edit_contacts())
    app = QApplication(sys.argv)

    window = SmsTools()
    window.show()
    window.load_contacts(search_terms="1")

    sys.exit(app.exec())
