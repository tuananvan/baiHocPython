import numpy as np
import matplotlib.pyplot as plt

languages = ['Python', 'JavaScript', 'TypeSript', 'Java', 'C#']
rankings = [
    [8,6,5,3,2,1], [1,2,2,2,3,2], [10,9,8,5,5,3], 
    [2,3,3,4,4,4], [5,4,4,6,5,6], ]
years = [2018, 2019, 2020, 2021, 2022, 2023]

colors = ["lime", "magenta", "purple", "orange", "gray", ]

plt.figure(figsize=(10, 6))

for i, (language, ranking) in enumerate(zip(languages, rankings)):
    plt.plot(years, ranking, label=language, color=colors[i], linewidth=2)

plt.gca().invert_yaxis()
plt.xticks(years, rotation=10)
plt.yticks(range(1, 11), fontsize=10)
plt.xlabel('Years', fontsize=12)
plt.ylabel('Rankings', fontsize=12)
plt.title('Programming Languages Rankings Over Years', fontsize=14)
plt.legend(bbox_to_anchor =(1.05, 1), loc ='upper left', fontsize = 9)
plt.grid(color ='gray', linestyle = '--', linewidth = 0.5, alpha = 0.7)
plt.tight_layout()
plt.show()

#plot(): Vẽ biểu đồ đường với các điểm dữ liệu từ danh sách.
#pie(): Vẽ biểu đồ tròn với các phần trăm từ danh sách.
#bar(): Vẽ biểu đồ cột với các giá trị từ danh sách.
#scatter(): Vẽ biểu đồ phân tán với các điểm dữ liệu từ danh sách x và y.