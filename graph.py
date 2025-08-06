#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt

def plot_language_chart(language_data, username):
    languages = list(language_data.keys())
    counts = list(language_data.values())

    plt.figure(figsize=(8, 6))
    plt.bar(languages, counts, color='skyblue')
    plt.xlabel('Languages')
    plt.ylabel('Repositories')
    plt.title(f'Languages Used by {username}')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"{username}_languages.png")
    plt.show()

