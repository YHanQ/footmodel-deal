import numpy as np
import random
import copy
import py_test as t
import matplotlib.pyplot as plt


v = t.get_vertex("Foot_data/fwd_l_0/0_SFusion.obj")
p = t.Plane(0, 0, 1, -10)
v1 = p.get_plane_points(v, rel=0.005)
curve = t.cal_ld_curve(v1)
curve = np.array(curve)
girth, dis_list, center = t.cal_shape_girth(v1)
v1 = [[x[0], x[1]] for x in v1]
v2 = copy.deepcopy(v1)
a = v2.pop(0)
v2.append(a)
v1 = np.array(v1)
v2 = np.array(v2)
fig = plt.figure()
ax = fig.add_subplot(131)
bx = fig.add_subplot(132)
for i in range(len(v1)):
    new = [v1[i], v2[i]]
    new = np.array(new)
    ax.plot(new[:, 0], new[:, 1])
bx.scatter(v1[:, 0], v1[:, 1])
bx.scatter(center[0], center[1])
bx.scatter(-46.306152, 150.071579)
cx = fig.add_subplot(133)
cx.scatter(curve[:, 0], curve[:, 1])
plt.show()


# for i in range(1, 11):
#     p = t.Plane(0, 0, 1, -20-i*0.1)
#     v1 = p.get_plane_points(v, rel=0.005)
#     fig = plt.figure()
#     ax = fig.add_subplot(111)
#     ax.scatter(v1[:, 0], v1[:, 1])
#     plt.show()


