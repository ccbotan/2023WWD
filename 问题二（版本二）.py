import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体

df=pd.read_excel("问题二导入python版本.xlsx",sheet_name="Sheet1",header=1,index_col=0)


Z=df.values.astype(float)

distances=df.columns.values.astype(float)
angles=df.index.values.astype(float)

X,Y=np.meshgrid(distances, angles)
fig=plt.figure()
ax=fig.add_subplot(111, projection='3d')

surf=ax.plot_surface(X,Y,Z,cmap='viridis',alpha=0.9,edgecolor='k',linewidth=0.3)

ax.set_xlabel('测量船距海域中心点处的距离/海里', fontsize=12, labelpad=10)
ax.set_ylabel('测线方向夹角/°', fontsize=12, labelpad=10)
ax.set_zlabel('覆盖宽度/m',fontsize=12,labelpad=10)

ax.set_title('覆盖宽度随距离和角度的变化关系')

cbar = fig.colorbar(surf, ax=ax, shrink=0.5, aspect=20, pad=0.1)
cbar.set_label('覆盖宽度 (m)', fontsize=12)

ax.grid(True, alpha=0.3)

plt.tight_layout()

plt.show()