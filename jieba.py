#!/usr/bin/env python
# coding: utf-8

# In[2]:


import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re
from PIL import Image
import numpy as np


# In[3]:


text = open("D:\cy\comment.txt",encoding='utf8').read()
text = text.replace('\n',"").replace("\u3000","")


# In[4]:


# 分词，返回结果为词的列表
text_cut = jieba.lcut(text)
# 将分好的词用某个符号分割开连成字符串
text_cut = ' '.join(text_cut)


# In[5]:


text_cut


# In[6]:


# 导入停词库
stop_words = open("D:\cy\stopwords.txt",encoding="utf8").read().split("\n")
# 导入图片
background = Image.open("D:\cy\mask.jpg")
graph = np.array(background)


# In[9]:


# 使用WordCloud生成词云
word_cloud = WordCloud(font_path="simsun.ttc",  # 设置词云字体
                       height= 700, # 画布高度
                       width=1000, # 画布宽度
                       max_words=180, # 最大显示词数
                       max_font_size=65, #显示的最大的字体大小
                       mask=graph,
                       mode='RGBA', # 生成透明背景
                       background_color="white", # 词云图的背景颜色
                       stopwords=stop_words) # 被淘汰不用于显示的词语，去掉的停词
word_cloud.generate(text_cut) # 根据文本生成词云图

# 运用matplotlib展现结果
plt.subplots(figsize=(12,8))
plt.imshow(word_cloud)
plt.axis("off")


# In[10]:


word_cloud.to_file("wc.png")


# In[ ]:




