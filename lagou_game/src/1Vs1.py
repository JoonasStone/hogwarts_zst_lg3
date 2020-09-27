#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
题目：
一个多回合制游戏，每个角色都有hp 和power，
hp代表血量，power代表攻击力，hp的初始值为1000，
power的初始值为200。打斗多个回合
定义一个fight方法：
my_hp = hp - enemy_power
enemy_final_hp = enemy_hp - my_power
谁的hp先为0，那么谁就输了
'''
import random
import time

print(" ******游戏开始****** ")
time.sleep(1.5)
print("******玩家信息*****")
print("Play A HP = 1000")
print("Enemy B HP = 1050")
def game():                     #定义游戏玩家基础属性
    My_HP = 1000                #玩家A血量
    My_power= random.randint(70,100)      #玩家A随机攻击力
    Your_Hp = 1050              #对手血量
    Your_power = random.randint(40,80)    #对手攻击力

    while True:
        print("*******************")
        print("敌方先发起攻击")
        My_HP = My_HP - Your_power                #玩家A的血量没轮减少
        print("玩家A剩余血量My_HP",My_HP)
        time.sleep(1)
        print("轮到玩家A发起攻击")
        Your_Hp = Your_Hp - My_power              #敌人的血量每轮减少
        print("敌人剩余血量为",Your_Hp)
        time.sleep(1)
        if My_HP <= 0 and My_HP < Your_Hp :       #玩家血量小于等于0 并且比敌人血少，则玩家败北
            print("敌人获胜")
            break
        elif Your_Hp <= 0 and My_HP > Your_Hp:    #敌人血量小于等于0 并且比玩家血少，则敌人败北
            print("玩家A获得胜利")
            break
        elif My_HP == Your_Hp:                    #若血量相同则平局
            print("平局，稍后进入下一个回合")
            break

game()