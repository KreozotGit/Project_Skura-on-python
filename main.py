import whisper
from tkinter import filedialog
import tkinter as tk

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title = 'Выберите аудиофайл',
    filetypes = [(("Аудио файлы", "*.mp3 *.wav *.m4a *.ogg"))]
)

if file_path:
    print(f'Выбран файл: {file_path }')
    model = whisper.load_model('small')
    result = model.transcribe(file_path, language = 'ru', fp16 = False, verbose = True)
    with open ('вторая_глава.txt', 'w', encoding = 'utf-8') as f:
        f.write(result['text'])
    print('Распознавание завершено.')
else:
    print('Файл не выбран')