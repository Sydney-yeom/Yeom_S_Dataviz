import numpy as np
import matplotlib.pyplot as plt

#font
hfont = { 'fontname': 'Arial'}

# dataset
sports = ['Skating', 'Skiing', 'Curling']
data = [87, 38, 0]

# explode dataset
explode = [0, 0, 0]

#color
colors = ["#837FBF", "#5D5A84", "#3F3D59"]

# plot
fig, ax = plt.subplots()
texts, autotexts = ax.pie(data, explode=explode, colors=colors, startangle=15)

#legend
ax.legend(sports, title="Sports", loc="lower right", bbox_to_anchor =(0.75, 0.09, 0.5, 0))

plt.setp(autotexts, size=4, weight="regular")
ax.set_title("The medal count comparison-Male", **hfont)

plt.show()