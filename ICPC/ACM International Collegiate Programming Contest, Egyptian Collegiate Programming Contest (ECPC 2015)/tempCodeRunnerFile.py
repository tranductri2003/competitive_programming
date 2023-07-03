import numpy as np
import matplotlib.pyplot as plt
from skimage import measure

# Đọc hình ảnh vào Python
image = plt.imread('"C:\Users\ADMIN\Downloads\class-diagram.png"')

# Áp dụng phép xoay hình ảnh
image = np.rot90(image)

# Sử dụng phương pháp marching cubes để tạo vật thể 3D
vertices, faces, _, _ = measure.marching_cubes(image)

# Hiển thị vật thể 3D bằng matplotlib
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

# Vẽ vật thể 3D
ax.plot_trisurf(vertices[:, 0], vertices[:, 1], faces,
                vertices[:, 2], shade=True, color='purple')

# Đặt tên cho trục
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Hiển thị vật thể 3D
plt.show()
