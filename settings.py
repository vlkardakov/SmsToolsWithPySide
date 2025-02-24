import sys, os, subprocess, shutil
from datetime import datetime
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QTableWidget, QTextBrowser, QTextEdit, QPushButton, QVBoxLayout, QWidget
from Scripts.bottle import delete
from openpyxl import load_workbook, Workbook
from ui_settings import Ui_settingswindow


def read_settings():
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

class Settings(QMainWindow):
    def __init__(self):
        super(Settings, self).__init__()
        self.ui = Ui_settingswindow()
        self.ui.setupUi(self)
        #self.ui.sendButton.clicked.connect(self.get_selected_numbers)
        self.ui.archivateData.clicked.connect(self.archivate_logs)


        # self.ui.saveSettings.clicked.connect(self.saveSettings)
        self.ui.cancelSettings.clicked.connect(self.cancelSettings)

    def keyPressEvent(self, event):
        pass
    def archivate_logs(self):
        log_file = "Files/sms_log.xlsx"
        analysis_file = "Files/Analysis.txt"
        archive_dir = "Files/Archive"
        if not os.path.exists(archive_dir):
            os.makedirs(archive_dir)

        current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        archived_log_file = f"{archive_dir}/sms_log_{current_datetime}.xlsx"
        archived_analysis_file = f"{archive_dir}/Analysis_{current_datetime}.txt"

        try:
            shutil.copy2(log_file, archived_log_file)
            print(f"Лог успешно архивирован в {archived_log_file}")

            wb = load_workbook("Files/sms_log.xlsx", data_only=True)
            ws = wb.active
            # Удаляем все строки, кроме первой
            ws.delete_rows(2, ws.max_row)

            # Устанавливаем высоту первой строки по умолчанию
            ws.row_dimensions[1].height = 13.7

            # Удаляем все настройки высоты строк, чтобы они стали по умолчанию
            for row_dim in ws.row_dimensions:
                if row_dim != 1:
                    ws.row_dimensions[row_dim].height = None

            wb.save(log_file)
            print("Лог успешно очищен, кроме строки заголовков")

            # Архивирование файла analysis.txt
            shutil.copy2(analysis_file, archived_analysis_file)
            print(f"Файл analysis.txt успешно архивирован в {archived_analysis_file}")

            # Очистка файла analysis.txt
            with open(analysis_file, 'w') as f:
                f.write('')

            print("Файл analysis.txt успешно очищен")

        except Exception as e:
            print(f"Ошибка при очистке логов: {e}")

    def cancelSettings(self):
        self.close()
