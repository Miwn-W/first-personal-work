#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import re
import time
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
}


# In[2]:


comment = []
comments = []
cursor = '0'
last_id = '1614095972004'
for i in range(0, 1000):
    url = 'https://coral.qq.com/article/5963120294/comment/v2?callback=_article5963120294commentv2&orinum=10&oriorder=o&pageflag=1&cursor=' + cursor + '&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=1&_='+ last_id
    source = requests.get(url, headers=headers).content.decode()
    comment = re.findall('.*?"content":"(.*?)",',source,re.S)
    comments.append(comment)
    cursor = re.findall('.*?"last":"(.*?)"',source,re.S)[0]
    last_id = str(int(last_id) + 1)


# In[3]:


with open('comment.txt','a',encoding='utf-8') as file:
    file.write(str(comments))


# In[ ]:




