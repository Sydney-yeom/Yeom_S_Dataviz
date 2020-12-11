import numpy as np
import matplotlib.pyplot as plt

#font
hfont = { 'fontname': 'Arial'}

# dataset
genders = ['Males', 'Females']
data = [125, 117]

# explode dataset
explode = [0, 0]

#color
colors = ["#7EB8BC", "#8981BD"]

# plot
fig, ax = plt.subplots()
texts, autotexts = ax.pie(data, explode=explode, colors=colors, startangle=15)

#legend
ax.legend(genders, title="Genders", loc="lower right", bbox_to_anchor =(0.75, 0.09, 0.5, 0))

plt.setp(autotexts, size=4, weight="regular")
ax.set_title("The medal count comparison", **hfont)

plt.show()