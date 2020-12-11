import numpy as np
import matplotlib.pyplot as plt

#font
hfont = { 'fontname': 'Arial'}

# dataset
genders = ['Males', 'Females']
sizes = [63, 80]
colors = ["#7EB8BC", "#8981BD"]

width = 0.3

countries = ['M-CHN', 'M-JPN', 'M-KAZ', 'M-KOR', 'F-CHN', 'F-JPN', 'F-KAZ', 'F-KOR']
sizes_countries = [22, 13, 1, 27, 40, 31, 8, 1]
colors_countries = ["#99C5C6", "#AAD7D8", "#A9C3C4", "#B9E3E6", "#AEADC5", "#A19FBE", "#9D9DCE", "#9493BA"]

#plot
fig, ax = plt.subplots()

texts, autotexts = ax.pie(sizes, colors=colors, startangle=90, frame=True, wedgeprops=dict(width=width, edgecolor='#F4F3FF'))
texts, autotexts = ax.pie(sizes_countries, colors=colors_countries, radius=0.7, startangle=90, wedgeprops=dict(width=width, edgecolor='#F4F3FF'))
        
ax.axis('equal')

#legend
bigger = ax.legend(genders, title="Genders", loc="lower left", bbox_to_anchor =(0.85, 0, 0.4, 0))
# smaller = ax.legend(countries, title="Countries", loc="lower right", bbox_to_anchor =(0.55, 0, 0.2, 0))
# ax.add_artist(bigger)

plt.setp(autotexts, size=4, weight="regular")
ax.set_title("The medal count comparison 'After 2000'", **hfont)

plt.show()