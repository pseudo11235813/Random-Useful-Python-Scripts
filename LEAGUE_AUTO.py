import pyautogui as pag
import time
from threading import *
import random

pag.FAILSAFE  = False
def move_kinda():#not really uwu
    while True:
        x = random.randint(100, 1200)
        y = random.randint(150, 682)
        pag.rightClick(x, y)
        time.sleep(30)

def move_nosync():
    x = random.randint(100, 1200)
    y = random.randint(100, 350)
    pag.rightClick(x, y)

def use_summs_randomly():
    while True:
        k = random.choice(['f','d'])
        pag.keyDown(k)
        time.sleep(120)

def purchase_tryout():#might work and might not, probably not XD, I mean like, you should be in base so it works
    while True:
        pag.keyDown("p")
        time.sleep(1)
        pag.rightClick(418, 304)
        time.sleep(2)

def level_up_abilities_azerty():
    while True:
        k = random.choice(['a','z','e','r'])
        pag.hotkey("ctrl",k)
        time.sleep(5)

def level_up_abilities_qwerty():
    while True:
        k = random.choice(['q','w','e','r'])
        pag.hotkey("ctrl",k)
        time.sleep(5)
        
def use_abilities_azerty():
    while True:
        k = random.choice(['a','z','e','r'])
        pag.keyDown(k)
        time.sleep(1)

def use_abilities_qwerty():
    while True:
        k = random.choice(['q','w','e','r'])
        pag.keyDown(k)
        time.sleep(1)

def task(x,y,delay):
    while True:
        pag.click(x,y)
        time.sleep(delay)
def task_ohne_schlafen(x,y):
    pag.click(x,y)

def seek_sympathy():
    passe

def switch():
    pag.hotkey("alt", "tab", interval= 0.1)

def goback():
    pag.click(474, 16)

def somereset():
    pag.click(156, 15)

def run():
    time.sleep(5)
    queue = Thread(target = task, args = (590,733,3)) #queue up for a game
    accept_game = Thread(target = task, args = (686,596,3)) #click accept
    ok = Thread(target = task, args = (687, 721,10)) #click some ok button  
    ok_declined = Thread(target=task, args=(686, 430,10)) #click some other button
    ok_dodge = Thread(target = task, args = (680, 468,10)) #some other dodging ok
    okboss = Thread(target = task , args = (681, 433,2)) #some other fucking ok man
    honor = Thread(target = task, args = (682,692,10)) #honor nobody lmao 
    select = Thread(target = task , args = (681,429,10)) #select a champ when a level-up reward is given 
    champ1 = Thread(target = task, args = (531, 211,10))
    champ2 = Thread(target = task, args = (634, 214,10))
    champ3 = Thread(target = task, args = (736, 209,10))
    champ4 = Thread(target = task, args = (838, 221,10))
    champ5 = Thread(target = task, args = (932, 208,10))
    lock = Thread(target = task, args = (757, 655,5))
    move = Thread(target = move_kinda)
    level_up = Thread(target = level_up_abilities_azerty)
    use = Thread(target= use_abilities_azerty)
    na_flash = Thread(target= use_summs_randomly)
    kauf = Thread(target = purchase_tryout)
    sw = Thread(target=switch)
    gobck = Thread(target = goback)
    reset = Thread(target = somereset)
    queue.start()
    accept_game.start()
    champ1.start()
    champ2.start()
    champ3.start()
    champ4.start()
    champ5.start()
    move.start()
    ok.start()
    ok_declined.start()
    ok_dodge.start()
    okboss.start()
    lock.start()
    sw.start()
    gobck.start()
    
def run1():
    time.sleep(5)
    while True:
        move_nosync()
        move_nosync()
        move_nosync()
        move_nosync()
        move_nosync()
        move_nosync()
        move_nosync()
        task_ohne_schlafen(590,733)
        move_nosync()
        task_ohne_schlafen(686,596)
        move_nosync()
        task_ohne_schlafen(687, 721)
        move_nosync()
        task_ohne_schlafen(686, 430)
        move_nosync()
        task_ohne_schlafen(680, 468)
        move_nosync()
        task_ohne_schlafen(681, 433)
        move_nosync()
        task_ohne_schlafen(682,692)
        move_nosync()
        task_ohne_schlafen(681,429)
        move_nosync()
        task_ohne_schlafen(531, 211)
        move_nosync()
        task_ohne_schlafen(757, 655)
        move_nosync()
        task_ohne_schlafen(634, 214)
        move_nosync()
        task_ohne_schlafen(757, 655)
        move_nosync()
        task_ohne_schlafen(736, 209)
        move_nosync()
        task_ohne_schlafen(757, 655)
        move_nosync()
        task_ohne_schlafen(838, 221)
        move_nosync()
        task_ohne_schlafen(757, 655)
        move_nosync()
        task_ohne_schlafen(932, 208)
        move_nosync()
        task_ohne_schlafen(757, 655)
        move_nosync()
        move_nosync()
        move_nosync()
        move_nosync()
        move_nosync()
        move_nosync()
        move_nosync()
        switch()
        time.sleep(1)
        goback()
        somereset()
        time.sleep(1)


run1()