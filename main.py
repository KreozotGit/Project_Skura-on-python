import whisper
import tkinter as tk
from tkinter import filedialog, simpledialog


root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title = 'Выберите аудиофайл',
    filetypes = [(("Аудио файлы", "*.mp3 *.wav *.m4a *.ogg"))]
)

if file_path:
    print(f'Выбран файл: {file_path }')
    new_file_name = simpledialog.askstring(
        'Имя файла', 
        'Введите название для текстового файла: ', 
        initialvalue = 'результат_распознавания'
        )
    new_file_path = filedialog.asksaveasfilename(
        title = 'Выберите папку для сохранения результата', 
        initialfile = new_file_name, 
        defaultextension='.txt',
        filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")],
        )
    model = whisper.load_model('small')
    result = model.transcribe(file_path, language = 'ru', fp16 = False, verbose = True)
    with open (new_file_path, 'w', encoding = 'utf-8') as f:
        f.write(result['text'])
    print('Распознавание завершено.')
else:
    print('Файл не выбран')