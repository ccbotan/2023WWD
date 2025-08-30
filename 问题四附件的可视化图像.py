import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体

df=pd.read_excel("附件python版本.xlsx",sheet_name="Sheet1",header=0,index_col=0)

Z=df.values.astype(float)



EW=df.columns.values.astype(float)
NS=df.index.values.astype(float)

print(NS)


X,Y=np.meshgrid(EW, NS)
fig=plt.figure()
ax=fig.add_subplot(111, projection='3d')

surf=ax.plot_surface(X,Y,Z,cmap='viridis',alpha=0.9,edgecolor='k',linewidth=0.3)

ax.set_xlabel('横向坐标/海里', fontsize=12, labelpad=10)
ax.set_ylabel('纵向坐标/海里', fontsize=12, labelpad=10)
ax.set_zlabel('海水深度/m',fontsize=12,labelpad=10)

ax.set_title('海域内不同位置的海水深度')

cbar = fig.colorbar(surf, ax=ax, shrink=0.5, aspect=20, pad=0.1)
cbar.set_label('海水深度 (m)', fontsize=12)

ax.grid(True, alpha=0.3)

plt.tight_layout()

plt.show()
