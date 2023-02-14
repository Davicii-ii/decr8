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

def on_press(event):
    if event.button == 1:
        # ax.clear()
        # Create the table
        table = ax.table(cellText=table_data)

        # Adjust the table appearance
        table.auto_set_font_size(False)
        table.set_fontsize(7)
        table.scale(1, 2)

        # table(cellText=table)
        fig.canvas.draw()

def on_click(event):
    # fig.clear()
    # if event.dblclick:
    ax.pie(np.random.rand(5), labels=['A', 'B', 'C', 'D', 'E'], autopct='%1.1f%%')
    plt.legend()
    plt.show()

data = process_data('C:\\Users\\avici\\decr8\\res\\decr8_data.json')

keys_list = [key for key in data]

title_list = [data[key]["title"] for key in data]

performer_list = [data[key]["performer"] for key in data]

performer_count = {}
for _, d in data.items():
    performer = d["performer"]
    if performer is None:
        continue
    if performer in performer_count:
        performer_count[performer] += 1
    else:
        performer_count[performer] = 1

# Sort performers by number of songs
sorted_performers = sorted(performer_count.items(), key=lambda x: x[1], reverse=True)

# Extract top 10 performers
top_5_performers = [performer[0] for performer in sorted_performers[:5]]

# Extract fractions of songs for top 10 performers
top_5_fracs = [performer_count[performer] for performer in top_5_performers]
top_5_fracs = [frac/sum(top_5_fracs) for frac in top_5_fracs]

top_5_performer_counts = [(performer, performer_count[performer]) for performer in top_5_performers]
top_5_fracs_counts = [(frac, count) for frac, count in zip(top_5_fracs, top_5_performer_counts)]

# Extract the duration values from the result variable and store them in a list
duration_minutes = [
    audio_data[
        'duration'
        ] for audio_data in data.values() if audio_data[
            "duration"
            ]
    ]
# Extract the date values from the result variable and store them in a list
dates = [
    datetime.strptime(
        audio_data['date'],
        '%Y-%m-%d %H:%M:%S'
        )
    for audio_data in data.values() if 'date' in audio_data
    ]
