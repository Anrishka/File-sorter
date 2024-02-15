# Импорт необходимых модулей
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
import os
import datetime
import shutil
import ctypes

# Установка DPI-осведомленности процесса для поддержки масштабирования на экранах с высоким разрешением (для Windows)
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except Exception:
    pass

# Создание основного окна приложения
root = Tk()
root.title('FileSorter')
root.geometry("500x150+1000+300")
root.iconbitmap(r'C:\Users\user\Desktop\курс питон записи\GPT_tasks\file_sorter\icon.ico')

# Создание стиля для кнопок
s = ttk.Style()
s.configure('my.TButton', font=("Helvetica", 15))

# Создание фрейма для размещения элементов интерфейса
frame = Frame(root, bg="#56ADFF", bd=5)
frame.pack(pady=10, padx=10, fill=X)

# Переменная для хранения пути к выбранной папке
folder_path = ''


# Функция для сортировки файлов по дате создания
def sort():
    """
    Сортирует файлы в выбранной папке по дате их создания.
    Создает папки с именем, соответствующим дате создания файла,
    и перемещает файлы в соответствующие папки.
    """
    files_by_date = {}
    files = os.listdir(folder_path)

    # Группируем файлы по дате их создания
    for file in files:
        file_path = os.path.join(folder_path, file)
        file_creation_time = os.path.getmtime(file_path)
        creation_date = datetime.datetime.fromtimestamp(file_creation_time)
        formatted_date = creation_date.strftime('%Y-%m-%d')

        if formatted_date not in files_by_date:
            files_by_date[formatted_date] = []
        files_by_date[formatted_date].append(file_path)

    # Перемещаем файлы в соответствующие папки
    for formatted_date, files_in_date in files_by_date.items():
        destination_folder = os.path.join(folder_path, formatted_date)
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
        for file_path in files_in_date:
            shutil.move(file_path, destination_folder)

    # Вывод информационного окна об успешной сортировке файлов
    messagebox.showinfo('Поздравляем!', 'Файлы успешно отсортированы')


# Функция для запроса папки
def ask_directory():
    """
    Запрашивает у пользователя папку для сортировки файлов.
    """
    global folder_path
    folder_path = filedialog.askdirectory(title="Выберите папку")
    # Очищаем и обновляем поле ввода пути к папке
    e_path.delete(0, END)
    e_path.insert(0, folder_path)


# Создание виджета Entry для ввода пути к папке
e_path = ttk.Entry(frame)
e_path.pack(side=LEFT, ipady=2, expand=True, fill=X)

# Создание кнопки "Выбрать папку" для вызова диалога выбора папки
btn_dialog = ttk.Button(frame, text="Выбрать папку", command=ask_directory)
btn_dialog.pack(side=LEFT, padx=5)

# Создание кнопки "Start" для запуска сортировки файлов
btn_start = ttk.Button(root, text="Start", style="my.TButton", command=sort)
btn_start.pack(fill=X, padx=10)

# Запуск главного цикла приложения
root.mainloop()
