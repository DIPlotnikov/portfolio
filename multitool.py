#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Простая программа для рабочего стола, решающая повседневные задачки офисного планктона.

# D.Plotnikov 2021

from tkinter import *
from tkinter import ttk
import datetime
import time
import requests
import calendar
import pyperclip


def dollar_rate():
    allinfo = requests.get("https://www.cbr-xml-daily.ru/daily_json.js").json()
    return round(allinfo["Valute"]["USD"]["Value"], 1)


def time_now():
    nowtime = datetime.datetime.now()
    return nowtime.strftime("%d-%m-%Y %H:%M")


def update_info():
    dollar = dollar_rate()
    res = F""" 1000 usd = {dollar * 1000} руб.
30   usd = {dollar * 30} руб.\n \nВремя обновления: {time_now()}"""
    lbl1.configure(text=res)


def calculate_doll(rub):
    if rub == "":
        lbl2_2.configure(text=F"На нет и суда нет (и туда нет).", font=["Arial Bold", 10])
        return
    if rub.isdigit() is False:
        lbl2_2.configure(text=F"Проверьте правильность ввода", font=["Arial Bold", 10])
        return
    result_dollar = round(float(rub) / dollar_rate(), 2)
    lbl2_2.configure(text=F"\n{rub} руб. это {result_dollar} долл.", font=["Arial Bold", 15])


def calculate_rub(doll):
    if doll == "":
        lbl2_2.configure(text=F"На нет и суда нет (и туда нет).", font=["Arial Bold", 10])
        return
    if doll.isdigit() is False:
        lbl2_2.configure(text=F"Проверьте правильность ввода", font=["Arial Bold", 10])
        return
    result_rub = round(float(doll) * dollar_rate(), 2)
    lbl2_2.configure(text=F"\n{doll} долл. это {result_rub} руб.", font=["Arial Bold", 15])


def transformate_sec(sec):
    if sec == "":
        lbl3_2.configure(text=F"На нет и суда нет (и туда нет).", font=["Arial Bold", 10])
        return
    if len(sec.split()) > 1 or sec.isdigit() is False:
        lbl3_2.configure(text=F"Проверьте правильность ввода", font=["Arial Bold", 10])
        return
    date = time.ctime(int((float(sec))))
    lbl3_2.configure(text=F"{date} (уже скопировано в буфер обмена)", font=["Arial Bold", 10])
    pyperclip.copy(date)


def transformate_date(date):
    if date == "":
        lbl3_2.configure(text=F"На нет и суда нет (и туда нет).",
                         font=["Arial Bold", 10])
        return
    date = date.replace(",", " ")
    date = date.replace("-", " ")
    date = date.replace(":", " ")
    date = date.replace(".", " ")
    date = date.replace("/", " ")
    date = date.replace("\\", " ")
    date = date.split()
    if len(date) < 6 or date.isdigit() is False:
        lbl3_2.configure(text=F"Проверьте правильность ввода", font=["Arial Bold", 10])
        return
    sec = calendar.timegm(tuple(map(int, date)))
    lbl3_2.configure(text=F"{sec} (уже скопировано в буфер обмена)", font=["Arial Bold", 10])
    pyperclip.copy(sec)


# Параметры окна
window = Tk()
window.geometry('430x180')
window.title("Мультитул 3.0")
window.wm_attributes('-alpha', 0.7)

# Параметры вкладок
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Курс')
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text='Калькулятор')
tab3 = ttk.Frame(tab_control)
tab_control.add(tab3, text='Время')
tab_control.pack(expand=1, fill='both')

# Первая вкладка
button1 = Button(tab1, text="Обновить", command=lambda: update_info())
lbl1 = Label(tab1, text=F""" Нажмите "Обновить", \nчтобы полуить свежую информацию.""",
             font=["Arial Bold", 15])
lbl1.pack(side="top")
button1.pack(fill='both', side="bottom")

# Вторая вкладка
top_frame = Frame(tab2)
bottom_frame = Frame(tab2)
lbl2 = Label(top_frame, text=F"Какую сумму переведем?", font=["Arial Bold", 15])
lbl2_2 = Label(tab2)
rub_enter = Entry(bottom_frame, width=30, font=["Arial Bold", 15])
button2 = Button(bottom_frame, text="В доллары", command=lambda: calculate_doll(rub_enter.get()),
                 font=["Arial Bold", 10])
button3 = Button(bottom_frame, text="В рубли", command=lambda: calculate_rub(rub_enter.get()),
                 font=["Arial Bold", 10])
top_frame.pack()
bottom_frame.pack(fill='both')
lbl2.pack(side="top")
rub_enter.pack(fill='both')
button2.pack(fill='both')
button3.pack(fill='both')
lbl2_2.pack()

# Третья вкладка
lbl3_1 = Label(tab3, text="Ввести секунды или дату \nв формате 'ГГГГ ММ ДД ЧЧ ММ СС' (знаки любые)",
               font=["Arial Bold", 10])
enter_num = Entry(tab3, width=50, font=["Arial Bold", 10])
button4 = Button(tab3, text="Секунды переводим в дату", command=lambda: transformate_sec(enter_num.get()))
button5 = Button(tab3, text="Дату в секунды", command=lambda: transformate_date(enter_num.get()))
lbl3_2 = Label(tab3)
lbl3_1.pack()
enter_num.pack(fill='both')
button4.pack(fill='both')
button5.pack(fill='both')
lbl3_2.pack()

window.mainloop()
