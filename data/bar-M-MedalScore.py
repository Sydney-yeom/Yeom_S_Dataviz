import matplotlib.pyplot as plt
import numpy as np

hfont = {'fontname' : 'Arial'}

# dataset
countries = ['CHN', 'JPN', 'KAZ', 'KOR', 'PRK', 'UZB']
skating = [25, 19, 1, 42, 0, 0]
skiing = [3, 31, 4, 0, 0, 0]
Curling = [0, 0, 0, 0, 0, 0]

barWidth = 0.20
br1 = np.arange(len(countries))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]

# plot
fig, ax = plt.subplots(figsize =(10,6))
fig = ax.get_figure()
# fig.tight_layout()

ax.bar(br1, skating, color ='#188955', width = barWidth, label ='Skating')
ax.bar(br2, skiing, color ='#5DC697', width = barWidth, edgecolor = 'w', label='Skiing')
ax.bar(br3, Curling, color = '#7E9E8F', width = barWidth, edgecolor = 'w', label = 'Curling')

# Xticks  
plt.xlabel('Asian Countries', fontweight ='regular', fontsize =10, **hfont)
plt.ylabel('The Medal Score', fontweight ='regular', fontsize =10, **hfont) 
plt.xticks(br1, labels=countries, **hfont)
plt.title('The medal score comparison by Sports (1956-2014) - Males', **hfont)

ax.legend()

plt.show()