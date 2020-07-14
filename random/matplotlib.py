import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d 

fig = plt.figure()
ax = Axes3D(fig)

ax.set_xlabel("X" , fontsize=20)
ax.set_ylabel("Y", fontsize=20)
ax.set_zlabel("Z" , fontsize=20)

ax.view_init(azim=-20)

ax.tick_params(axis='x', which='major', pad=0)

x = np.arange(0,10,0.01)
y = np.ones(len(x))
z = np.sin(x)
plt.plot(x,y,z)