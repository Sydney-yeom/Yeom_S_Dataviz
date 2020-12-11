import matplotlib.pyplot as plt
import numpy as np

hfont = {'fontname' : 'Arial'}

# dataset
countries = ['CHN', 'JPN', 'KAZ', 'KOR', 'PRK', 'UZB']
skating = [44, 9, 1, 45, 2, 0]
skiing = [5, 4, 0, 0, 0, 1]
Curling = [5, 0, 0, 0, 0, 0]

barWidth = 0.2
br1 = np.arange(len(countries))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]

# plot
fig, ax = plt.subplots(figsize =(11,6))
fig = ax.get_figure()
# fig.tight_layout()

ax.bar(br1, skating, color ='#AAA5E5', width = barWidth, label ='Skating')
ax.bar(br2, skiing, color ='#7874AF', width = barWidth, edgecolor = 'w', label='Skiing')
ax.bar(br3, Curling, color ='#534E89', width = barWidth, edgecolor = 'w', label = 'Curling')

# Xticks  
plt.xlabel('Asian Countries', fontweight ='regular', fontsize =10, **hfont)
plt.ylabel('The Medal Score', fontweight ='regular', fontsize =10, **hfont) 
plt.xticks(br1, labels=countries, **hfont)
plt.title('The medal score comparison by Sports (1956-2014) - Females', **hfont)

ax.legend()

plt.show()