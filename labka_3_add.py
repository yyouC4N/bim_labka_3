import NemAll_Python_Geometry as ge
from lab3_beam import Lab2_Beam as lb


def tp_1(build_ele):
    data = lb.get(build_ele)
    poliline = ge.Polygon3D()
    poliline += ge.Point3D(data[0], data[1] - data[2] -
                           (data[1] - data[2] * 2 - data[3]) / 2, data[4] + data[5])
    poliline += ge.Point3D(data[0], data[6] -
                           (data[6] - data[1]) / 2, data[4] + data[5] + data[7])
    poliline += ge.Point3D(data[0], -(data[6] - data[1]) /
                           2, data[4] + data[5] + data[7])
    poliline += ge.Point3D(data[0], data[2] +
                           (data[1] - data[2] * 2 - data[3]) / 2, data[4] + data[5])
    poliline += ge.Point3D(data[0], data[1] - data[2] -
                           (data[1] - data[2] * 2 - data[3]) / 2, data[4] + data[5])
    tr = ge.Polyline3D()
    tr += ge.Point3D(data[0], data[1] - data[2] -
                     (data[1] - data[2] * 2 - data[3]) / 2, data[4] + data[5])
    tr += ge.Point3D(data[8] - data[0], data[1] -
                     data[2] - (data[1] - data[2] * 2 - data[3]) / 2, data[4] + data[5])

    error, fig = ge.CreatePolyhedron(poliline, tr)

    return fig


def tp_2(build_ele):
    data = lb.get(build_ele)
    poliline = ge.Polygon3D()
    poliline += ge.Point3D(data[8] - data[0],
                           data[1] - data[2], data[4] + data[5])
    poliline += ge.Point3D(data[8] - data[0] - data[9], data[1] -
                           data[2] - (data[1] - data[2] * 2 - data[3]) / 2, data[4] + data[5])
    poliline += ge.Point3D(data[8] - data[0] - data[9] - (data[1] - data[2] * 2 - data[3]) / 2, data[1] - (
        data[1] - data[2] * 2 - data[3]) / 2 + (data[6] - data[1]) / 2, data[4] + data[5] + data[7])
    poliline += ge.Point3D(data[8] - data[0] - (data[1] - data[2] * 2 - data[3]) / 2,
                           data[1] + (data[6] - data[1]) / 2, data[4] + data[5] + data[7])
    poliline += ge.Point3D(data[8] - data[0],
                           data[1] - data[2], data[4] + data[5])

    tr = ge.Polyline3D()
    tr += ge.Point3D(data[8] - data[0], data[1] - data[2], data[4] + data[5])
    tr += ge.Point3D(data[8] - data[0] +
                     10, data[1] - data[2] - 10, data[4] + data[5] + 10)

    error, fig = ge.CreatePolyhedron(poliline, tr)
    return fig


def tp_3(build_ele, sign=0):
    data = lb.get(build_ele)
    poliline = ge.Polygon3D()
    poliline += ge.Point3D(sign, data[2], data[4] + data[5])
    poliline += ge.Point3D(sign, data[1] - data[2], data[4] + data[5])
    poliline += ge.Point3D(sign, data[1] +
                           (data[6] - data[1]) / 2, data[4] + data[5] + data[7])
    poliline += ge.Point3D(sign, -
                           (data[6] - data[1]) / 2, data[4] + data[5] + data[7])
    poliline += ge.Point3D(sign, data[2], data[4] + data[5])

    tr = ge.Polyline3D()
    tr += ge.Point3D(sign, data[2], data[4] + data[5])
    tr += ge.Point3D(sign + data[0], data[2], data[4] + data[5])

    error, fig = ge.CreatePolyhedron(poliline, tr)
    return fig


def tp_4(build_ele, minus_1=0, minus_2=0, digit=-10):
    data = lb.get(build_ele)
    poliline = ge.Polygon3D()
    poliline += ge.Point3D(data[8] - data[0],
                           data[1] - data[2] - minus_1, data[4] + data[5])
    poliline += ge.Point3D(data[8] - data[0], data[6] -
                           (data[6] - data[1]) / 2 - minus_2, data[4] + data[5] + data[7])
    poliline += ge.Point3D(data[8] - data[0] - (data[1] - data[2] * 2 - data[3]) / 2,
                           data[1] + (data[6] - data[1]) / 2 - minus_2, data[4] + data[5] + data[7])
    poliline += ge.Point3D(data[8] - data[0],
                           data[1] - data[2] - minus_1, data[4] + data[5])

    tr = ge.Polyline3D()
    tr += ge.Point3D(data[8] - data[0],
                     data[1] - data[2] - minus_1, data[4] + data[5])
    tr += ge.Point3D(data[8] - data[0],
                     data[1] - data[2] + digit - minus_1, data[4] + data[5])
    error, fig = ge.CreatePolyhedron(poliline, tr)
    return fig


def tp_2_2(build_ele):
    data = lb.get(build_ele)
    poliline = ge.Polygon3D()
    poliline += ge.Point3D(data[8] - data[0], data[2], data[4] + data[5])
    poliline += ge.Point3D(data[8] - data[0] - data[9],
                           data[2] + (data[1] - data[2] * 2 - data[3]) / 2, data[4] + data[5])
    poliline += ge.Point3D(data[8] - data[0] - data[9] - (data[1] - data[2] * 2 - data[3]) / 2,
                           (data[1] - data[2] * 2 - data[3]) / 2 - (data[6] - data[1]) / 2, data[4] + data[5] + data[7])
    poliline += ge.Point3D(data[8] - data[0] - (data[1] - data[2] *
                                                2 - data[3]) / 2, -(data[6] - data[1]) / 2, data[4] + data[5] + data[7])
    poliline += ge.Point3D(data[8] - data[0],  data[2], data[4] + data[5])

    tr = ge.Polyline3D()
    tr += ge.Point3D(data[8] - data[0], data[2], data[4] + data[5])
    tr += ge.Point3D(data[8] - data[0] +
                     10, data[2] + 10, data[4] + data[5] + 10)

    error, fig = ge.CreatePolyhedron(poliline, tr)
    return fig


def tp_2_3(build_ele):
    data = lb.get(build_ele)
    poliline = ge.Polygon3D()
    poliline += ge.Point3D(data[0], data[1] - data[2], data[4] + data[5])
    poliline += ge.Point3D(data[0] + data[9], data[1] -
                           data[2] - (data[1] - data[2] * 2 - data[3]) / 2, data[4] + data[5])
    poliline += ge.Point3D(data[0] + data[9] + (data[1] - data[2] * 2 - data[3]) / 2, data[1] - (
        data[1] - data[2] * 2 - data[3]) / 2 + (data[6] - data[1]) / 2, data[4] + data[5] + data[7])
    poliline += ge.Point3D(data[0] + (data[1] - data[2] * 2 - data[3]) / 2,
                           data[1] + (data[6] - data[1]) / 2, data[4] + data[5] + data[7])
    poliline += ge.Point3D(data[0], data[1] - data[2], data[4] + data[5])

    tr = ge.Polyline3D()
    tr += ge.Point3D(data[0], data[1] - data[2], data[4] + data[5])
    tr += ge.Point3D(data[0] - 10,
                     data[1] - data[2] - 10, data[4] + data[5] - 10)
    error, fig = ge.CreatePolyhedron(poliline, tr)

    return fig


def tp_4_2(build_ele, minus_1=0, minus_2=0, digit=-10):
    data = lb.get(build_ele)
    poliline = ge.Polygon3D()
    poliline += ge.Point3D(data[0], data[1] -
                           data[2] - minus_1, data[4] + data[5])
    poliline += ge.Point3D(data[0], data[1] + (data[6] - data[1]) /
                           2 - minus_2, data[4] + data[5] + data[7])
    poliline += ge.Point3D(data[0] + (data[1] - data[2] * 2 - data[3]) / 2,
                           data[1] + (data[6] - data[1]) / 2 - minus_2, data[4] + data[5] + data[7])
    poliline += ge.Point3D(data[0], data[1] -
                           data[2] - minus_1, data[4] + data[5])

    tr = ge.Polyline3D()
    tr += ge.Point3D(data[0], data[1] - data[2] - minus_1, data[4] + data[5])
    tr += ge.Point3D(data[0], data[1] -
                     data[2] - minus_1 + digit, data[4] + data[5])

    error, fig = ge.CreatePolyhedron(poliline, tr)

    return fig


def tp_3_3(build_ele):
    data = lb.get(build_ele)
    poliline = ge.Polygon3D()
    poliline += ge.Point3D(data[0], data[2], data[4] + data[5])
    poliline += ge.Point3D(data[0] + data[9], data[2] +
                           (data[1] - data[2] * 2 - data[3]) / 2, data[4] + data[5])
    poliline += ge.Point3D(data[0] + data[9] + (data[1] - data[2] * 2 - data[3]) / 2,
                           (data[1] - data[2] * 2 - data[3]) / 2 - (data[6] - data[1]) / 2, data[4] + data[5] + data[7])
    poliline += ge.Point3D(data[0] + (data[1] - data[2] * 2 - data[3]) /
                           2, -(data[6] - data[1]) / 2, data[4] + data[5] + data[7])
    poliline += ge.Point3D(data[0], data[2], data[4] + data[5])

    tr = ge.Polyline3D()
    tr += ge.Point3D(data[0], data[2], data[4] + data[5])
    tr += ge.Point3D(data[0] - 10, data[2] + 10, data[4] + data[5] - 10)

    error, fig = ge.CreatePolyhedron(poliline, tr)

    return fig


def tp_last(build_ele):
    data = lb.get(build_ele)
    poliline = ge.Polygon3D()
    poliline += ge.Point3D(0, -(data[6] - data[1]) / 2,
                           data[4] + data[5] + data[7])
    poliline += ge.Point3D(0, data[6] - (data[6] -
                           data[1]) / 2, data[4] + data[5] + data[7])
    poliline += ge.Point3D(0, data[6] - (data[6] -
                           data[1]) / 2, data[4] + data[5] + data[7])
    poliline += ge.Point3D(0, data[6] - (data[6] - data[1]) /
                           2 - data[10], data[4] + data[5] + data[7])
    poliline += ge.Point3D(0, data[6] - (data[6] - data[1]) /
                           2 - data[10], data[4] + data[5] + data[7] + build_ele.hp.value)
    poliline += ge.Point3D(0, - (data[6] - data[1]) / 2 +
                           data[10], data[4] + data[5] + data[7] + build_ele.hp.value)
    poliline += ge.Point3D(0, - (data[6] - data[1]) /
                           2 + data[10], [4] + data[5] + data[7])
    poliline += ge.Point3D(0, - (data[6] - data[1]) /
                           2, data[4] + data[5] + data[7])
    poliline += ge.Point3D(0, -(data[6] - data[1]) / 2,
                           data[4] + data[5] + data[7])

    tr = ge.Polyline3D()
    tr += ge.Point3D(0, -(data[6] - data[1]) / 2, data[4] + data[5] + data[7])
    tr += ge.Point3D(data[8], -(data[6] - data[1]) /
                     2, data[4] + data[5] + data[7])
    error, fig = ge.CreatePolyhedron(poliline, tr)

    return fig


def bp_1(build_ele):
    data = lb.get(build_ele)
    poliline = ge.Polygon3D()
    poliline += ge.Point3D(data[0], data[1], data[4] - data[10])
    poliline += ge.Point3D(data[0], data[1] - data[2] -
                           (data[1] - data[2] * 2 - data[3]) / 2, data[4])
    poliline += ge.Point3D(data[0], data[1] - data[2] -
                           (data[1] - data[2] * 2 - data[3]) / 2 - data[3], data[4])
    poliline += ge.Point3D(data[0], 0, data[4] - data[10])
    poliline += ge.Point3D(data[0], data[1], data[4] - data[10])

    tr = ge.Polyline3D()
    tr += ge.Point3D(data[0], data[1], data[4] - data[10])
    tr += ge.Point3D(data[8] - data[0], data[1], data[4] - data[10])
    error, fig = ge.CreatePolyhedron(poliline, tr)

    return fig


def bp_2(build_ele):
    data = lb.get(build_ele)
    poliline = ge.Polygon3D()
    poliline += ge.Point3D(data[0], data[1] - data[2], data[4])
    poliline += ge.Point3D(data[0] + data[9], data[1] -
                           data[2] - (data[1] - data[2] * 2 - data[3]) / 2, data[4])
    poliline += ge.Point3D(data[0] + data[9] + (data[1] - data[2] * 2 - data[3]) / 2,
                           data[1] - (data[1] - data[2] * 2 - data[3]) / 2, data[4] - data[10])
    poliline += ge.Point3D(data[0] + (data[1] - data[2]
                                      * 2 - data[3]) / 2, data[1], data[4] - data[10])
    poliline += ge.Point3D(data[0], data[1] - data[2], data[4])

    tr = ge.Polyline3D()
    tr += ge.Point3D(data[0], data[1] - data[2], data[4])
    tr += ge.Point3D(data[0] - 10, data[1] - data[2] - 10, data[4] - 10)

    error, fig = ge.CreatePolyhedron(poliline, tr)
    return fig


def bp_3(build_ele):
    data = lb.get(build_ele)
    poliline = ge.Polygon3D()
    poliline += ge.Point3D(0, data[1], data[4] - data[10])
    poliline += ge.Point3D(0, data[1] - data[2], data[4])
    poliline += ge.Point3D(0, data[2], data[4])
    poliline += ge.Point3D(0, 0, data[4] - data[10])
    poliline += ge.Point3D(0, data[1], data[4] - data[10])

    tr = ge.Polyline3D()
    tr += ge.Point3D(0, data[1], data[4] - data[10])
    tr += ge.Point3D(data[0], data[1], data[4] - data[10])

    error, fig = ge.CreatePolyhedron(poliline, tr)

    return fig


def bp_4(build_ele):
    data = lb.get(build_ele)
    poliline = ge.Polygon3D()
    poliline += ge.Point3D(data[0], data[1] - data[2], data[4])
    poliline += ge.Point3D(data[0], data[1], data[4] - data[10])
    poliline += ge.Point3D(data[0] + (data[1] - data[2]
                                      * 2 - data[3]) / 2, data[1], data[4] - data[10])
    poliline += ge.Point3D(data[0], data[1] - data[2], data[4])

    tr = ge.Polyline3D()
    tr += ge.Point3D(data[0], data[1] - data[2], data[4])
    tr += ge.Point3D(data[0], data[1] - data[2] - 10, data[4])

    error, fig = ge.CreatePolyhedron(poliline, tr)
    return fig


def bp_2_2(build_ele):
    data = lb.get(build_ele)
    poliline = ge.Polygon3D()
    poliline += ge.Point3D(data[0], data[2], data[4])
    poliline += ge.Point3D(data[0] + data[9], data[2] +
                           (data[1] - data[2] * 2 - data[3]) / 2, data[4])
    poliline += ge.Point3D(data[0] + data[9] + (data[1] - data[2] * 2 - data[3]) / 2,
                           (data[1] - data[2] * 2 - data[3]) / 2, data[4] - data[10])
    poliline += ge.Point3D(data[0] + (data[1] - data[2]
                                      * 2 - data[3]) / 2, 0, data[4] - data[10])
    poliline += ge.Point3D(data[0], data[2], data[4])

    tr = ge.Polyline3D()
    tr += ge.Point3D(data[0], data[2], data[4])
    tr += ge.Point3D(data[0] - 10, data[2] + 10, data[4] - 10)

    error, fig = ge.CreatePolyhedron(poliline, tr)

    return fig


def bp_3_2(build_ele):
    data = lb.get(build_ele)
    poliline = ge.Polygon3D()
    poliline += ge.Point3D(data[8] - data[0], data[1], data[4] - data[10])
    poliline += ge.Point3D(data[8] - data[0], data[1] - data[2], data[4])
    poliline += ge.Point3D(data[8] - data[0], data[2], data[4])
    poliline += ge.Point3D(data[8] - data[0], 0, data[4] - data[10])
    poliline += ge.Point3D(data[8] - data[0], data[1], data[4] - data[10])

    tr = ge.Polyline3D()
    tr += ge.Point3D(data[8] - data[0], data[1], data[4] - data[10])
    tr += ge.Point3D(data[8], data[1], data[4] - data[10])

    error, fig = ge.CreatePolyhedron(poliline, tr)
    return fig


def bp_4_2(build_ele):
    data = lb.get(build_ele)
    poliline = ge.Polygon3D()
    poliline += ge.Point3D(data[0], data[2], data[4])
    poliline += ge.Point3D(data[0], 0, data[4] - data[10])
    poliline += ge.Point3D(data[0] + (data[1] - data[2]
                                      * 2 - data[3]) / 2, 0, data[4] - data[10])
    poliline += ge.Point3D(data[0], data[2], data[4])

    tr = ge.Polyline3D()
    tr += ge.Point3D(data[0], data[2], data[4])
    tr += ge.Point3D(data[0], data[2] + 10, data[4])

    error, fig = ge.CreatePolyhedron(poliline, tr)
    return fig


def bp_2_3(build_ele):
    data = lb.get(build_ele)
    poliline = ge.Polygon3D()
    poliline += ge.Point3D(data[8] - data[0], data[1] - data[2], data[4])
    poliline += ge.Point3D(data[8] - data[0] - data[9],
                           data[1] - data[2] - (data[1] - data[2] * 2 - data[3]) / 2, data[4])
    poliline += ge.Point3D(data[8] - data[0] - data[9] - (data[1] - data[2] * 2 - data[3]) / 2,
                           data[1] - (data[1] - data[2] * 2 - data[3]) / 2, data[4] - data[10])
    poliline += ge.Point3D(data[8] - data[0] -
                           (data[1] - data[2] * 2 - data[3]) / 2, data[1], data[4] - data[10])
    poliline += ge.Point3D(data[8] - data[0], data[1] - data[2], data[4])

    tr = ge.Polyline3D()
    tr += ge.Point3D(data[8] - data[0], data[1] - data[2], data[4])
    tr += ge.Point3D(data[8] - data[0] +
                     10, data[1] - data[2] - 10, data[4] + 10)

    error, fig = ge.CreatePolyhedron(poliline, tr)

    return fig


def bp_3_3(build_ele):
    data = lb.get(build_ele)
    poliline = ge.Polygon3D()
    poliline += ge.Point3D(data[8] - data[0], data[1] - data[2], data[4])
    poliline += ge.Point3D(data[8] - data[0], data[1], data[4] - data[10])
    poliline += ge.Point3D(data[8] - data[0] -
                           (data[1] - data[2] * 2 - data[3]) / 2, data[1], data[4] - data[10])
    poliline += ge.Point3D(data[8] - data[0], data[1] - data[2], data[4])

    tr = ge.Polyline3D()
    tr += ge.Point3D(data[8] - data[0], data[1] - data[2], data[4])
    tr += ge.Point3D(data[8] - data[0], data[1] - data[2] - 10, data[4])

    error, fig = ge.CreatePolyhedron(poliline, tr)
    return fig


def bp_2_4(build_ele):
    data = lb.get(build_ele)
    poliline = ge.Polygon3D()
    poliline += ge.Point3D(data[8] - data[0], data[2], data[4])
    poliline += ge.Point3D(data[8] - data[0] - data[9],
                           data[2] + (data[1] - data[2] * 2 - data[3]) / 2, data[4])
    poliline += ge.Point3D(data[8] - data[0] - data[9] - (data[1] - data[2]
                                                          * 2 - data[3]) / 2, (data[1] - data[2] * 2 - data[3]) / 2, data[4] - data[10])
    poliline += ge.Point3D(data[8] - data[0] -
                           (data[1] - data[2] * 2 - data[3]) / 2, 0, data[4] - data[10])
    poliline += ge.Point3D(data[8] - data[0], data[2], data[4])

    tr = ge.Polyline3D()
    tr += ge.Point3D(data[8] - data[0], data[2], data[4])
    tr += ge.Point3D(data[8] - data[0] - 10, data[2] + 10, data[4] - 10)

    error, fig = ge.CreatePolyhedron(poliline, tr)

    return fig


def bp_3_4(build_ele):
    data = lb.get(build_ele)
    poliline = ge.Polygon3D()
    poliline += ge.Point3D(data[8] - data[0], data[2], data[4])
    poliline += ge.Point3D(data[8] - data[0], 0, data[4] - data[10])
    poliline += ge.Point3D(data[8] - data[0] -
                           (data[1] - data[2] * 2 - data[3]) / 2, 0, data[4] - data[10])
    poliline += ge.Point3D(data[8] - data[0], data[2], data[4])

    tr = ge.Polyline3D()
    tr += ge.Point3D(data[8] - data[0], data[2], data[4])
    tr += ge.Point3D(data[8] - build_ele.widme.value, data[2] + 10, data[4])

    error, fig = ge.CreatePolyhedron(poliline, tr)

    return fig


def bp_last(build_ele):
    data = lb.get(build_ele)
    poliline = ge.Polygon3D()
    poliline += ge.Point3D(0, 20, 0)
    poliline += ge.Point3D(0, data[1] - 20, 0)
    poliline += ge.Point3D(0, data[1], 20)
    poliline += ge.Point3D(0, data[1], data[4] - data[10])
    poliline += ge.Point3D(0, 0, data[4] - data[10])
    poliline += ge.Point3D(0, 0, 20)
    poliline += ge.Point3D(0, 20, 0)

    tr = ge.Polyline3D()
    tr += ge.Point3D(0, 20, 0)
    tr += ge.Point3D(data[8], 20, 0)
    error, fig = ge.CreatePolyhedron(poliline, tr)
    return fig
