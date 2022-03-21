import re

import jieba
import matplotlib.pyplot as plt
import wordcloud

PATH_IN = input('输入聊天记录文件位置：')
PATH_FONT = input('输入字体文件位置（ttf格式）：') or None

with open(PATH_IN, 'r') as io:
    text = io.read()

msgs = re.findall(r'\d+-\d+-\d+ \d+:\d+:\d+ .+\n(.+)', text)
for i, msg in enumerate(msgs):
    msg: str
    msg = re.sub(r'@\S+', '', msg)
    msg = re.sub(r'\[\S+]', '', msg)
    msg = msg.strip()
    msgs[i] = msg

msgs = [msg for msg in msgs if msg]

words_count = {}
for msg in msgs:
    words = list(jieba.cut(msg))
    for word in words:
        c = words_count.get(word, 0)
        words_count[word] = c + 1

wc_items = [(k, v) for k, v in words_count.items() if len(k) > 1]
wc_items = sorted(wc_items, key=lambda x: x[1] + len(x[0].encode()) / 3, reverse=True)

draw_words = [i[0] for i in wc_items[:100]]
wc = wordcloud.WordCloud(PATH_FONT)
wc.generate(' '.join(draw_words))

plt.imshow(wc.to_image())
plt.axis('off')
plt.show()
