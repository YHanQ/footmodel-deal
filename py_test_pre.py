import numpy as np
import math
from matplotlib import pyplot as plt
from scipy.spatial import ConvexHull


def get_vertex(file_path):
    vertex = []
    with open(file_path, 'r') as f:
        for line in f:
            if line.startswith("v "):
                s = line.rstrip("\n").lstrip("v ").split(' ')
                vertex.append([float(s[0]), float(s[1]), float(s[2])])
    vertex = np.array(vertex)
    f.close()
    return vertex


def convexhull(points):
    if points is None:
        return None
    cv = ConvexHull(points)
    res_pointlist = []
    for i in cv.vertices:
        point = points[i]
        res_pointlist.append(point)
    return res_pointlist


def cal_dis(points):
    if points is None:
        return None
    dis = 0
    for i in range(len(points)-1):
        dis += np.sqrt(np.sum(np.square(points[i]-points[i+1])))
    return dis


def cal_centroid(points):
    if points is None:
        return None
    res = [0, 0, 0]
    for i in points:
        res += i
    return res/len(points)


def cal_shape_girth(points):
    if points is None:
        return None
    center = cal_centroid(points)
    for i in range(len(points)-1):
        for j in range(len(points)-1-i):
            if point_cmp(points[j], points[j+1], center):
                points[[j, j+1], :] = points[[j+1, j], :]
    girth = 0
    dis_list = []
    for i in range(len(points)-1):
        temp = np.sqrt((points[i][0]-points[i+1][0])**2 + (points[i][1]-points[i+1][1])**2)
        girth += temp
        dis_list.append(temp)
    temp = np.sqrt((points[0][0] - points[len(points)-1][0]) ** 2 + (points[0][1] - points[len(points)-1][1]) ** 2)
    girth += temp
    dis_list.append(temp)
    return girth, dis_list, center


def cal_ld_curve(points):
    if points is None:
        return None
    ld_curve = []
    girth, dis_list, center = cal_shape_girth(points)
    # for i in dis_list:
    #     dis =



def point_cmp(a, b, center):
    if a[0] >= 0 and b[0] <= 0:
        return True
    if a[0] == 0 and b[0] == 0:
        return a[1] > b[1]
    det = int((a[0] - center[0]) * (b[1] - center[1]) - (b[0] - center[0]) * (a[1] - center[1]))
    if det < 0:
        return True
    elif det > 0:
        return False
    d1 = (a[0] - center[0])**2 + (a[1] - center[1])**2
    d2 = (b[0] - center[0])**2 + (b[1] - center[1])**2
    return d1 > d2


class Plane:
    def __init__(self,a=0.0,b=0.0,c=0.0,d=0.0):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d

    def get_plane_points(self, vertex, rel=1e-9):
        plane_vertex = []
        for x in vertex:
            b=self.__a*x[0]+self.__b*x[1]+self.__c*x[2]
            if math.isclose(a=self.__d, b=b, rel_tol=rel):
                plane_vertex.append(x)
        plane_vertex = np.array(plane_vertex)
        return plane_vertex


if __name__ == '__main__':
    v = get_vertex("model/nor3.obj")
    p1 = Plane(.0, .0, 1, 0.02)
    v1 = p1.get_plane_points(v, rel=0.005)
    fig = plt.figure()
    ax = fig.add_subplot(121,projection='3d')
    bx = fig.add_subplot(122)
    ax.scatter(v1[:,0], v1[:,1],v1[:,2])
    bx.scatter(v[:,0], v[:,1])
    plt.show()
