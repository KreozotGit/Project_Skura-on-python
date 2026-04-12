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
         
        if file_path == '':
            if messagebox.askyesno(
                title = 'Файл не выбран',
                message = 'Желаете выбрать файл?'
            ):
                continue
            else:
                messagebox.showinfo(
                    title = 'Окончание работы программы.',
                    message = 'Программа завершит свою работу. До свидания!'
                )
                sys.exit()
    
def select_file_name():
    while True:
        new_file_name = simpledialog.askstring( # открывает окно для выбора названия файла после распознавания  
        'Имя файла', 
        'Введите название для текстового файла: ', 
        initialvalue = 'результат_распознавания'
        )
        
        if new_file_name is None:
            if messagebox.askyesno(
                title = 'Выход из программы',
                message = 'Вы хотите выйти из программы?'
            ):
                messagebox.showinfo(
                    title = 'Окончание работы программы.',
                    message = 'Программа завершит свою работу. До свидания!'
                )
                sys.exit()
            else:
                 continue
             
        elif new_file_name.strip() == '':
            messagebox.showwarning(
                title = 'Ошибка',
                message = 'Имя файла не может быть пустым. Укажите имя файла.'
            )
            continue
        
        return new_file_name
    
root = tk.Tk() # создание главного окна приложения
root.withdraw() # прячет главное окно для пользователя

audio = select_audio() # выбор пути к аудио файлу
print(f'Выбран файл: {audio}')

file_name = select_file_name()

new_file_path = filedialog.asksaveasfilename( # открывает окно для выбора пути сохранения файла после распознавания, если файл с таким именем уже существует, говорит об этом пользователю, это базовая особенность
    title = 'Выберите папку для сохранения результата', 
    initialfile = file_name, 
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