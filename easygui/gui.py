# _*_ coding:utf-8 _*_

import easygui
import sys

while 1:
    easygui.msgbox('hi，欢迎进入第一个界面小游戏^_^')

    msg = '请问你能在这学到什么知识呢？'
    title = '小游戏互动'
    choices = ['谈恋爱', '编程', '琴棋书画']

    choice = easygui.choicebox(msg, title, choices)

    easygui.msgbox('你的选择是：' + str(choice), '结果')

    msg = '你希望重新开始小游戏吗？'
    title = '提示'

    if easygui.ccbox(msg, title):
        pass
    else:
        sys.exit(0)
