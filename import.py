import random
import datetime
import time
import easygui



def idiom_exists(x):
    with open('idiom.txt','r',) as f:
        for i in set(f.readlines()):
            if x == i.strip():
                return True
        return False
def idiom_test(idiom1, idiom2):
    try:
        if idiom2[0] != idiom1[-1] or len(idiom2) != 4:
            return False
        else:
            return True
    except:
        return False
    


def idiom_select(x):
    if x == None:
        with open('idiom.txt','r') as f:
            return random.choice(f.readlines())[:-1]
    else:
        with open('idiom.txt','r') as f:
            base = f.readlines()
            random.shuffle(base)
            for i in base:
                if i[:-1] == x or len(i) != 5:
                    continue
                if i[0] == x[-1]:
                    return i[:-1]
        return None

def idiom_start(start = 0):
    global hhs
    hhs = 0
    memory = set()
    if start == 0:
        while True:
            t = idiom_select(None)
            if idiom_select(t) != None and len(t) == 4:
                break
        print(t+'                                                                   |')
    else:
        p = input("请输入成语:                                                                 |")
        for e in range(1,3):
            if idiom_exists(p) == False:
                print("该成语不存在,还有"+str(3 - e)+"次机会                                                   |")
        if idiom_exists(p) == False:
            print("游戏结束！该成语不存在")
            return 0
        memory.add(p)
        cycle_flag = 0  #控制while True循环次数
        while True:
            t = idiom_select(p)
            cycle_flag += 1
            if t not in memory:
                break
            if cycle_flag == 10:
                t = None
                break
        if t == None:
            print()
            return 1
        else:
            print(t)
            memory.add(t)        
    while True:
        for d in range(1,4):
            p = input("请输入成语:                                                                |")
            if idiom_exists(p) == False:
                print("该成语不存在,还有"+str(3 - d)+"次机会                                                   |")
            if p in memory:
                print("该成语已被使用过,还有"+str(3 - d)+"次机会                                               |")
            if idiom_test(t, p) == False:
                print("你未遵守游戏规则,还有"+str(3 - d)+"次机会                                               |")
        if idiom_exists(p) == False:
            print("该成语不存在,你失败了                                                      |")
            return 0
        if p in memory:
            print("该成语已被使用过,你失败了                                                  |")
            return 0
        if p != '':
            if idiom_test(t, p) == False:
                print("你未遵守游戏规则,你失败了                                                               |")
                return 0


        
        memory.add(p)
        cycle_flag = 0
        while True:
            t = idiom_select(p)
            cycle_flag += 1
            if t not in memory:
                break
            if cycle_flag == 10:
                t = None
                break
        if t == None:
            return 1
        else:
            print(t+'                                                                   |')
            memory.add(t)
        hhs = hhs + 1
    
while True:
    answe = easygui.buttonbox('''                              ==============================================
                              |成 语 大 赛                                 |
                              |                                            |
                              |                                    作者:WYH|
                              |                                 made by:WYH|
                              |按ENTER键以开始                             |
                              ==============================================''',choices = ['开始','源代码','规则','退出'])
    answe = easygui.buttonbox('''                              ==============================================
                              |成 语 大 赛                                 |
                              |                                            |
                              |                                    作者:WYH|
                              |                                 made by:WYH|
                              |按ENTER键以开始                             |
                              ==============================================''',choices = ['开始','源代码','规则','退出'])
    if answe == '退出':
        break
    if answe == '源代码':
        print('源代码展示：                                                                    |')        
        print('''import random

def idiom_exists(x):
    with open('idiom.txt','r') as f:
        for i in set(f.readlines()):
            if x == i.strip():
                return True
        return False

def idiom_test(idiom1, idiom2):
    if idiom2[0] != idiom1[-1] or len(idiom2) != 4:
        return False
    return True

def idiom_select(x):
    if x == None:
        with open('idiom.txt','r') as f:
            return random.choice(f.readlines())[:-1]
    else:
        with open('idiom.txt','r') as f:
            base = f.readlines()
            random.shuffle(base)
            for i in base:
                if i[:-1] == x or len(i) != 5:
                    continue
                if i[0] == x[-1]:
                    return i[:-1]
        return None

def idiom_start(start = 0):
    """start参数表示先后手，0表示电脑先手，1表示玩家先手；返回值代表游戏结果，为0表示玩家失败，为1代表玩家胜利"""
    memory = set()
    if start == 0:
        while True:
            t = idiom_select(None)
            if idiom_select(t) != None and len(t) == 4:
                break
        print(t)
    else:
        p = input("请输入成语:")
        if p.strip() == '':
            print("游戏结束！你输了")
            return 0
        if idiom_exists(p) == False:
            print("游戏结束！该成语不存在")
            return 0
        memory.add(p)
        cycle_flag = 0  #控制while True循环次数
        while True:
            t = idiom_select(p)
            cycle_flag += 1
            if t not in memory:
                break
            if cycle_flag == 10:
                t = None
                break
        if t == None:
            print("恭喜你，你赢了！")
            return 1
        else:
            print(t)
            memory.add(t)        
    while True:
        p = input("请输入成语:")
        if p.strip() == '':
            print("游戏结束！你输了")
        if idiom_exists(p) == False:
            print("游戏结束！该成语不存在")
            return 0
        if p in memory:
            print("游戏结束！该成语已被使用过")
            return 0
        if idiom_test(t, p) == False:
            print("游戏结束！你未遵守游戏规则")
            return 0
        memory.add(p)
        cycle_flag = 0
        while True:
            t = idiom_select(p)
            cycle_flag += 1
            if t not in memory:
                break
            if cycle_flag == 10:
                t = None
                break
        if t == None:
            print("恭喜你，你赢了！")
            return 1
        else:
            print(t)
            memory.add(t)''')
        print('|按ENTER返回                                                                    |')
        input('|                                                                               |')
    elif answe == '规则':
        print('|规则：                                                                         |')
        print('|1.不得作弊                                                                     |')
        print('|2.不得用相同的成语                                                             |')
        print('|按ENTER返回                                                                    |')
        input('|                                                                               |')
    else:
        for i in range(1,101):
            if i < 10:
                print('loading'+'█'*int(i*0.75)+str(i)+'%')
            elif i <100:
                print('loading'+'█'*int(i*0.75)+str(i)+'%')
            else:
                print('loading'+'█'*int(i*0.75)+str(i)+'%')
            
        start = datetime.datetime.now()
        print('================================================================================')
        zg = idiom_start()
        end = datetime.datetime.now()
        time_ = end - start
        time = time_.seconds + time_.microseconds / 1000000
        if zg == 0:
            print('================================================================================')
            print('|失败了，再接再厉                                                               |')
            fen = (-1 * time / ((hhs+1)*10))
            print('|经过了'+str(hhs)+'回合'+',一共用了'+str(time)+'秒，得分'+str(fen)+'                        |')
            print('|按ENTER重新开始                                                                |')
            cd = input()
            if cd == 'cd':
                print('你以发现彩蛋，按100次ENTER即可解锁')
                for c in range(1,100):
                    input('|                                                                              |')
                cd1 = input('|                                                                              |')
                if cd1 == 'cd':
                    print('恭喜你，发现真正的彩蛋！！！')
                else:
                    print('什么也没有23333')
                    input()
        if zg == 1:
            print('================================================================================')
            print('|胜利啦！                                                                       |')
            fen = (1 / time * ((hhs+1)*10))
            print('|经过了'+str(hhs+1)+'回合'+',一共用了'+str(time)+'秒，得分'+str(fen)+'                        |')
            print('|按ENTER重新开始                                                                |')
            cd_ = input()
            if cd_ == 'cd':
                print('你以发现彩蛋，按100次ENTER即可解锁')
                for c in range(1,100):
                    input('|                                                                              |')
                cd1_ = input('|                                                                              |')
                if cd1_ == 'cd':
                    print('恭喜你，发现真正的彩蛋！！！')
                else:
                    print('什么也没有23333')
                    input()
