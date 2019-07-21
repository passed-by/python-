import pygame,os

def welcome():
    print('''
    *************************
    * 欢迎来到酷我音乐播放器 *
    *************************
    ''')

def select():
    print('''
    ***************************
    * 1.开始播放   2.暂停/播放 *
    * 3.下一曲     4.上一曲    *
    * 5.增大音量   6.减少音量  *
    * 7.显示歌单   0.退出      *
    ***************************
    ''')
    return input("请选择您要操作的选项：")

def action(allmusic_name):
    '''用于播放音乐
    :param allmusic_name: 播放歌曲的歌名
    :return: 返回True表示正在播放歌曲
    '''
    pygame.mixer.init()
    pygame.mixer.music.load(allmusic_name)
    pygame.mixer.music.play()
    pygame.mixer.music.queue(allmusic[2])
    return True

def findmusic():
    '''
    查找当前目录的所有音乐
    :return: 以列表方式返回当前目录的音乐
    '''
    dirspath = os.getcwd()
    mslist = os.listdir(dirspath)
    return [ms for ms in mslist if ms.endswith('.mp3')]


if __name__ == '__main__':
    welcome()

    # allmusic = ['王菲-传奇.mp3','周杰伦-稻香.mp3','周传雄 - 寂寞沙洲冷.mp3','周传雄-黄昏.mp3']
    allmusic = findmusic()

    action_num = 0     ##默认播放第一首歌曲
    action_vo = 0.6   ##默认播放声音大小

    while 1:
        num = select()
        # print(pygame.mixer.music.get_endevent())
        # pygame.mixer.music.set_endevent(pygame.USEREVENT + 1)
        if num == "1":
           checkm = action(allmusic[action_num])
           print("当前播放歌曲:%s" % allmusic[action_num])
           # print(pygame.USEREVENT)
           # print(pygame.mixer.music.get_endevent())
           # print(allmusic[allmusic.index(allmusic[action_num])+1])
        elif num == "2":
            if checkm:
                pygame.mixer.music.pause()     #暂停播放
                checkm = False
                print("已暂停~~~~")
            else:
                pygame.mixer.music.unpause()    #取消暂停播放
                checkm = True
        elif num == "3":
            action_num += 1
            if action_num == len(allmusic):
                action_num = 0
            action(allmusic[action_num])
            print("当前播放歌曲:%s" % allmusic[action_num])
            pass
        elif num == "4":
            action_num -= 1
            if action_num > len(allmusic):
                action_num = 0
            action(allmusic[action_num])
            print("当前播放歌曲:%s"%allmusic[action_num])
        elif num == "5":
            if action_vo + 0.2 < 1:
                action_vo += 0.2
            else:
                action_vo = 1
                print("声音已经最大~~~~")
            pygame.mixer.music.set_volume(action_vo)
        elif num == "6":
            if action_vo - 0.2 > 0:
                action_vo -= 0.2
            else:
                action_vo = 0
                print("声音已经最小~~~")
            pygame.mixer.music.set_volume(action_vo)
        elif num == "0":
            pygame.mixer.music.stop()         #停止播放歌曲
            print("退出酷我音乐播放器")
            break
        elif num =="7":
            for n,gq in enumerate(allmusic):
                print("%d. %s"%(n+1,gq))
            gq_num = int(input("\n选择歌曲编号:"))
            action(allmusic[gq_num - 1])
            print("当前播放歌曲:%s" % allmusic[gq_num - 1])
 
