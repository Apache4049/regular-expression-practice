#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
def text_match(text):
        patterns = 'ab{3}?'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("abbb"))
print(text_match("aabbbbbc"))


# In[ ]:




