import jieba

## # 读取书本文件，使用jieba分词
def countWords(excludes, merges):
    txt = open('西游记 .txt', 'r', encoding = 'utf-8').read()
    words = jieba.lcut(txt)
    counts = {}#转化为字典


 # 取出⻓度为⼀的词和符号以及excludes中的词
    for word in words:
        if len(word) == 1 or word in excludes:
            continue
        else:
           counts[word] = counts.get(word, 0) + 1

 # 合并名称相同的⼈名
    for merge in merges:
        for name in merge[1]:
            counts[merge[0]] += counts.get(name, 0)
            if name in counts:
                del counts[name]
    word_list = list(counts.items())
    word_list.sort(key = lambda x : x[1], reverse = True)
    return word_list

#排除词语
excludes = {'一个','那里','怎么','我们','不知','两个','什么',
            '不是','甚么',
            '原来','不敢','不曾',
            '这个','如何','正是'
            '知道','那里','不知','两个','这么','那么',
            '怎么','如果',
            '是','的','这个','一个','这种','时候','什么',
            '这里','一部','这部','没有',
             '还有','因为','只见','甚么','原来',
             '不敢','如何','不曾'
             ,'闻言','那怪','一声',
             '真个','不得','只是','片子','可以'
             ,'其实','无法','这样'
             ,'可能','最后','我们','东西',
             '现在','正是','所以','一直','也许'
             ,'出来','不能'}

# 人名合并
merges = [('孙悟空',('美猴王','老孙','齐天大圣','行者道','悟空','大圣','行者')),
          ('唐僧',('三藏','唐长老','唐僧道','师父')),
          ('猪八戒',('猪刚鬣','夯货','八戒','八戒道')),('沙僧',('沙和尚','悟净'))]
word_list = countWords(excludes, merges)

# 显示前10个词语和出现次数
for i in range(10):
    word, count = word_list[i]
    print(i+1, word, count) # chr(12288)为中⽂空格
