import copy
import json
import math
import os
import tkinter as tk
from abc import ABC, abstractmethod
from random import randrange as rnd, choice
from tkinter import filedialog

import hit_check


# Time step for delayed jobs
DT = 30
VICTORY_MSG_TIME = 3000
WINDOW_SHAPE = (800, 600)


def pass_event(event):
    pass

class BattleField(tk.Canvas):
    def __init__(self, master):
        super().__init__(master, background='white')

        self.num_targets = 2

#        self.gun = Gun(self)
        self.targets = {}
        self.bullets = {}

        # Переменная для присвоения номеров выпущенным пулям.
        # Номера используются для определения, каким по счету выстрелом была
        # уничтожена цель. Отсчет начинается с единицы.
        self.bullet_counter = 0
        self.last_hit_bullet_number = None
        self.victory_text_id = self.create_text(
            WINDOW_SHAPE[0] // 2, WINDOW_SHAPE[1] // 2, text='', font='28')

        self.catch_victory_job = None
        self.canvas_restart_job = None

class MainFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.score = 0
        self.score_tmpl = 'Score: {}'
        self.score_label = tk.Label(
            self,
            text=self.score_tmpl.format(self.score),
            font=("Times New Roman", 36)
        )
        self.score_label.pack()

        self.battlefield = BattleField(self)
        self.battlefield.pack(fill=tk.BOTH, expand=1)

class Menu(tk.Menu):
    def __init__(self, master, game):
        super().__init__(master)

        self.game = game

        self.file_menu = tk.Menu(self)
        self.file_menu.add_command(label="save", command=self.master.save)
        self.file_menu.add_command(label="load", command=self.master.load)
        self.add_cascade(label="file", menu=self.file_menu)

        self.game_menu = tk.Menu(self)
        self.game_menu.add_command(label="new", command=self.master.new_game)
        self.add_cascade(label="game", menu=self.game_menu)

class GunGameApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('{}x{}'.format(*WINDOW_SHAPE))

        # Переменная `__file__` содержит путь к файлу, в котором используется.
        #
        # Функция `os.path.split()` разделяет путь к файлу на имя директории
        # и имя файла.
        #
        # Функция `os.path.join()` объединяет несколько путей в один. Она
        # самостоятельно подбирает разделитель в соответствии с операционной
        # системой: '/' для UNIX и '\' для Windows.
        self.save_dir = os.path.join(os.path.split(__file__)[0], 'save')

        self.main_frame = MainFrame(self.master)
        self.main_frame.pack(fill=tk.BOTH, expand=1)

        self.menu = Menu(self.master, self)
        self.config(menu=self.menu)

        self.bind("<Control-s>", self.save)

    def get_state(self):
        """Собирает все меняющиеся признаки виджетов и подвижных элементов
        из `canvas`.
        """
        return {'main_frame': self.main_frame.get_state()}

    def set_state(self, state, job_init='pause'):
        """Создает игру соответствующую состоянию `state`.
        Применяется к состояниям приложения полученным с помощью метода
        `GunGameApp.set_state()`.
        `state` содержит значения всех изменяющиеся в процессе игры
        признаков. Эти значения присваются признакам `MainFrame`,
        `BattleField` и `Gun`. Мишени и пули создаются заново.
        Отложенным событиям, которым соответствует `True` в `state`,
        присваивается значение `job_init`, Если `job_init == 'pause'`,
        то игра после выполнения `GunGameApp.set_state()`, игра может
        быть запущена методом `GunGameApp.play()`.
        Args:
            state (словарь, содержащий другие словари и списки): Структура
                словаря `state` должна повторять структуру виджетов
                приложения. В словаре `state` есть ключ `'main_frame'`,
                в словаре `state['main_frame']` -- элемент `'battlefield'`
                и т.д..
            job_init (`str` или `None`): Этим значением инициализируется
                активные на момент получения состояния игры `state` отложенные
                задачи.
        Returns:
            None
        """
        self.main_frame.set_state(state['main_frame'], job_init)

    def get_save_file_name(self):
        os.makedirs(self.save_dir, exist_ok=True)
        file_name = filedialog.asksaveasfilename(
            initialdir=self.save_dir,
            title='Save game',
            filetypes=(("json files", "*.json"), ("all files", "*.*"))
        )
        if file_name in [(), '']:
            return None
        return file_name

    def get_load_file_name(self):
        file_name = filedialog.askopenfilename(
            initialdir=self.save_dir,
            title='Load game',
            filetypes=(("json files", "*.json"), ("all files", "*.*"))
        )
        if file_name in [(), '']:
            return None
        return file_name

    def save(self, event=None):
        self.pause()
        game_state = self.get_state()
        file_name = self.get_save_file_name()
        if file_name is not None:
            with open(file_name, 'w') as f:
                # Аргумент `indent` обеспечивает за красивое
                # оформление JSON файла.
                json.dump(game_state, f, indent=2)
        self.play()

    def load(self):
        # Приложение ставится на паузу, а не останавливается, чтобы при сборе
        # состояния игры было видно, какие отложенные задачи активны.
        self.pause()
        file_name = self.get_load_file_name()
        if file_name is not None:
            with open(file_name) as f:
                state = json.load(f)
            self.set_state(state)
        self.play()

    def new_game(self):
        self.main_frame.new_game()

    def pause(self):
        """Приостанавливает игру. Отложенным задачам присвваивается значение
        `'pause'`. Игру можно возобновить с помощью метода
        `GunGameApp.play()`.
        """
        self.main_frame.pause()

    def play(self):
        self.main_frame.play()

    def stop(self):
        """Снимает все отложеннве задачи. Отложенным задачам причваиватеся
        `None`.
        """
        self.main_frame.stop()


app = GunGameApp()
#app.new_game()
app.mainloop()