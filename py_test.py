import numpy as np
import math
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
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
    res = [0, 0]
    for i in points:
        res += i
    return res/len(points)


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
