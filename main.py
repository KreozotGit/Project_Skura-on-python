import sys
import whisper
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox # нужно испортировать отдельно, чтобы работали

def select_audio(): # функция для выбора пользователем пути к файлу с обработкой отсутствия выбора     
    while True:
        right_extensions = ("Аудио файлы", "*.mp3 *.wav *.m4a *.ogg")
        file_path = filedialog.askopenfilename(
            title = 'Выберите аудиофайл', 
            filetypes = [right_extensions]
        )
        if file_path:
            return file_path
        else:
            again = messagebox.askretrycancel(
                title = 'Файл не выбран',
                message = 'Желаете снова выбрать файл?'
            )
            if not again:
                messagebox.showinfo(
                    title = 'Окончание работы программы.',
                    message = 'Программа завершит свою работу. До свидания!'
                )
                sys.exit()
            
root = tk.Tk() # создание главного окна приложения
root.withdraw() # прячет главное окно для пользователя

audio = select_audio() # выбор пути к аудио файлу
print(f'Выбран файл: {audio}')
new_file_name = simpledialog.askstring( # открывает окно для выбора названия файла после распознавания  
    'Имя файла', 
    'Введите название для текстового файла: ', 
    initialvalue = 'результат_распознавания'
)

new_file_path = filedialog.asksaveasfilename( # открывает окно для выбора пути сохранения файла после распознавания, если файл с таким именем уже существует, говорит об этом пользователю, это базовая особенность
    title = 'Выберите папку для сохранения результата', 
    initialfile = new_file_name, 
    defaultextension='.txt',
    filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")],
)

model = whisper.load_model('turbo') #  выбор модели распознавания
messagebox.showinfo(
    title = 'Начало процесса',
    message = 'Начинаю процесс распознавания. Для продолжения нажмите ОК или закройте данное сообщение.'
)
result = model.transcribe(audio, language = 'ru', fp16 = False, verbose = True)  # сохраняет в переменную результат транскрибации
with open (new_file_path, 'w', encoding = 'utf-8') as f: # открывает файл, записывает в  поле текст результат и закрывает файл
    f.write(result['text'])
messagebox.showinfo(
    title = 'Окончание процесса',
    message = 'Распознавание завершено.'
)