# -*- coding: utf-8 -*-
#!/usr/bin/python3
import codecs
import re

decode_list = ["utf-8", 'gb18030', 'ISO-8859-2', 'gb2312', "gbk", "Error"]


class Count():
    emptyLines = 0
    codeLines = 0
    commentLines = 0
    lineCount = 0
    charCount = 0
    wordCount = 0
    lineList = []

    def __init__(self, path):
        # if path in (".c"):
        for k in decode_list:
            # 编码集循环
            try:
                file = open(path, "r", encoding=k)
                # 打开路径中的文本
                lineList = file.readlines()
                # 这步如果解码失败就会引起错误,跳到except。
                print("open file with encoding %s" % (k))
                break
                # 打开路径成功跳出编码匹配
            except:
                if k == "Error":  # 如果碰到这个程序终止运行
                    raise Exception("%s had no way to decode" % path)
                continue
        #file = open(path, 'r', encoding="ansi")
        #lineList = file.readlines()
        self.calcLines(lineList)
        file.close()

    def calcLines(self, lineList):
        lineNo, self.lineCount, flag = 0, len(
            lineList), 0  # 上个字符是否是空格(1表示是  0表示不是)
        while lineNo < len(lineList):
            temp = 0
            for c in lineList[lineNo]:
                if (c != '\n') & (c != '\r') & (c != ' ') & (c != '\t'):
                    self.charCount += 1
                    if not((c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z')):
                        temp += 1
                if (c == ' ') | (c == '\t'):
                    if flag == 0:
                        self.wordCount += 1
                    flag = 1
                elif (c != '\n') & (c != '\r'):
                    flag = 0
            if flag == 0:
                self.wordCount += 1
            flag = 1
            if (lineList[lineNo].isspace()) or (temp == 1):  # 空行
                self.emptyLines += 1
                lineNo += 1
                continue
            regMatch = re.match('^([^/]*)/(/|\*)+(.*)$',
                                lineList[lineNo].strip())
            if regMatch != None:  # 注释行

                # 代码&注释混合行
                if regMatch.group(1) != '':
                    self.codeLines += 1
                    lineNo += 1
                    continue
                elif regMatch.group(2) == '*' \
                        and re.match('^.*\*/.+$', regMatch.group(3)) != None:
                    self.codeLines += 1
                    lineNo += 1
                    continue

                self.commentLines += 1
                # 行注释或单行块注释
                if '/*' not in lineList[lineNo] or '*/' in lineList[lineNo]:
                    lineNo += 1
                    continue

                # 跨行块注释
                lineNo += 1
                while '*/' not in lineList[lineNo]:
                    if lineList[lineNo].isspace():
                        self.emptyLines += 1
                    else:
                        self.commentLines += 1
                    lineNo = lineNo + 1
                    continue
                self.commentLines += 1  # '*/'所在行
            else:  # 代码行
                self.codeLines += 1
            lineNo += 1
