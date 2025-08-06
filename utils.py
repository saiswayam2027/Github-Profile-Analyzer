#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from collections import Counter

def get_user_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def analyze_languages(repos):
    language_counter = Counter()
    for repo in repos:
        lang = repo.get('language')
        if lang:
            language_counter[lang] += 1
    return language_counter


# In[ ]:




