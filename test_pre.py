import numpy as np
import random
import py_test as t
import matplotlib.pyplot as plt

# pointlist = []
# for i in range(0,50):
#     x = random.randrange(0, 50)
#     y = random.randrange(0, 50)
#     point = [x,y]
#     pointlist.append(point)
#
# pointlist = np.array(pointlist)
# res = t.convexhull(pointlist)
# res = np.array(res)
# print(t.cal_dis(res))
# print(t.cal_centroid(res))
# fig = plt.figure()
# ax = fig.add_subplot(121)
# bx = fig.add_subplot(122)
# ax.scatter(pointlist[:,0],pointlist[:,1])
# bx.scatter(res[:,0],res[:,1])
# plt.show()


v = t.get_vertex("Foot_data/fwd_l_0/0_SFusion.obj")
p = t.Plane(0, 0, 1, -19.9)
v1 = p.get_plane_points(v, rel=0.005)
girth, dis_list, center = t.cal_shape_girth(v1)
print(girth)
print(v1)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(v1[:,0], v1[:,1])
plt.show()
# for i in range(1, 11):
#     p = t.Plane(0, 0, 1, -20-i*0.1)
#     v1 = p.get_plane_points(v, rel=0.005)
#     fig = plt.figure()
#     ax = fig.add_subplot(111)
#     ax.scatter(v1[:, 0], v1[:, 1])
#     plt.show()


