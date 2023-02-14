import matplotlib.pyplot as plt
import numpy as np
import json, random
from datetime import datetime
import matplotlib.widgets as widgets

def process_data(file_path):
    with open(file_path, "r+", encoding="utf-8") as f:
        d = json.load(f)
        sorted(d)
    return d

data = process_data('C:\\Users\\avici\\decr8\\res\\decr8_data.json')
keys_list = [key for key in data if data['title'] is None]

# create a histogram
plt.hist(keys_list, bins=20, color='blue', edgecolor='black')
plt.show()
