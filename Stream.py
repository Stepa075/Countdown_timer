from threading import Thread
from time import sleep
from tkinter.filedialog import askopenfilename
import os
import Variables
import sys

default_seconds = 120  # изначальное положение(120 мин 00 сек)
timer_seconds = 0
timer_running = True


def open_file():
    Variables.filename = askopenfilename()


# def timer_start_pause():
#         global timer_running
#         timer_running = True  # работа или пауза
#         if timer_running:  # работа
#             timer_tick()

# def timer_reset():
#         global timer_running, timer_seconds
#         timer_running = False  # стоп
#         timer_seconds = default_seconds  # изначальное положение
#         show_timer()

def timer_tick():
    global timer_running, timer_seconds
    while timer_seconds > 0:
        if Variables.stop_timer:
            break

        timer_seconds -= 1               # уменьшить таймер
        # print(str(timer_seconds))
        show_timer()
        sleep(1.0)
                                         # тут еще разобраться нужно в настройке этой функции
    if Variables.stop_timer:
        pass
    else:
        print('Finish Timer!')
        do_it_by_end_timer()

def show_timer():
    '''отобразить таймер'''
    Variables.set_h = timer_seconds // 3600
    Variables.set_m = timer_seconds // 60 - Variables.set_h * 60
    # print(str(Variables.set_m))
    Variables.set_s = timer_seconds - Variables.set_m * 60 - Variables.set_h * 3600
    # print(str(Variables.set_m) + str(Variables.set_s))
    Variables.set_timer_time = str(('%02d:%02d:%02d' % (Variables.set_h, Variables.set_m, Variables.set_s)))
    print('%02d:%02d:%02d' % (Variables.set_h, Variables.set_m, Variables.set_s))


def do_it_by_end_timer():
    if Variables.input_combo_box == 0:
        print('Выключить ПК')
        os.system('shutdown -s')
        os.execl(sys.executable, sys.executable, *sys.argv)

    if Variables.input_combo_box == 1:
        print('Перезагрузить ПК')
        os.system('shutdown -r')
        os.execl(sys.executable, sys.executable, *sys.argv)
    if Variables.input_combo_box == 2:
        print('Гибернация')
        os.system('shutdown -h')
        os.execl(sys.executable, sys.executable, *sys.argv)
    if Variables.input_combo_box == 3:
        print('Выполнить файл')
    if Variables.input_combo_box == 4:
        print('Завершить файл')
    if Variables.input_combo_box == 5:
        print('Выдать напоминание')
        Variables.message()


def start_timer():
    try:
        global timer_seconds
        print('Start timer!')
        Variables.stop_timer = False
        timer_seconds = (int(Variables.h) * 3600) + (int(Variables.m) * 60) + int(Variables.s)
        # timer_start_pause()
        # timer_tick()
        th = Thread(target=timer_tick, daemon=True)
        th.start()

        # show_timer()
    except ValueError:
        Variables.warning_messege()
        pass


def stop_timer():
    Variables.stop_timer = True
