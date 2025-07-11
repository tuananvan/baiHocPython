import matplotlib.pyplot as plt
import numpy as np

# Dữ liệu cho biểu đồ đường
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Dữ liệu cho biểu đồ tròn
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]

# Tạo khung hình với 1 hàng, 2 cột
fig, axs = plt.subplots(1, 2, figsize=(10, 4))

# Vẽ biểu đồ đường ở subplot thứ nhất
axs[0].plot(x, y, color='blue')
axs[0].set_title('Biểu đồ đường')
axs[0].set_xlabel('x')
axs[0].set_ylabel('sin(x)')

# Vẽ biểu đồ tròn ở subplot thứ hai
axs[1].pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
axs[1].set_title('Biểu đồ tròn')
axs[1].axis('equal')  # Đảm bảo hình tròn tròn đều

# Hiển thị
plt.tight_layout()
plt.show()
