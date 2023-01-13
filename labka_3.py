import NemAll_Python_Geometry as ge
import NemAll_Python_BaseElements as b
import NemAll_Python_BasisElements as bs
from labka_3_info import get
from labka_3_add import *


def check_allplan_version(build_ele, version):
    del build_ele
    del version
    return True


def create_element(build_ele, doc):
    el = labka_3(doc)
    return el.create(build_ele)


class labka_3:
    def __init__(self, doc):
        self.model_ele_list = []
        self.handle_list = []
        self.document = doc

    def create(self, build_ele):
        self.union(build_ele)
        self.bottom(build_ele)
        return (self.model_ele_list, self.handle_list)

    def union(self, build_ele):
        style = b.CommonProperties()
        style.GetGlobalProperties()
        style.Pen = 1
        style.Color = 3
        style.Stroke = 1
        btn = self.bottom(build_ele)
        cnt = self.cnt(build_ele)
        tp = self.top(build_ele)
        er, fig = ge.MakeUnion(btn, cnt)
        er, fig = ge.MakeUnion(fig, tp)
        self.model_ele_list.append(
            bs.ModelElement3D(style, fig))

    def bottom(self, build_ele):
        fig = self.bp_1(build_ele)
        er, fig = ge.MakeUnion(fig, self.bp_2(build_ele))
        er, fig = ge.MakeUnion(fig, self.bp_3(build_ele))
        er, fig = ge.MakeUnion(fig, self.bp_4(build_ele))
        er, fig = ge.MakeUnion(fig, self.bp_2_2(build_ele))
        er, fig = ge.MakeUnion(fig, self.bp_3_2(build_ele))
        er, fig = ge.MakeUnion(fig, self.bp_4_2(build_ele))
        er, fig = ge.MakeUnion(fig, self.bp_2_3(build_ele))
        er, fig = ge.MakeUnion(fig, self.bp_3_3(build_ele))
        er, fig = ge.MakeUnion(fig, self.bp_2_4(build_ele))
        er, fig = ge.MakeUnion(fig, self.bp_3_4(build_ele))
        er, fig = ge.MakeUnion(fig, self.bp_last(build_ele))
        return fig

    def top(self, build_ele):
        sign = (build_ele.len.value - build_ele.widme.value)
        fig = self.tp_1(build_ele)
        er, fig = ge.MakeUnion(fig, self.tp_3(build_ele))
        er, fig = ge.MakeUnion(fig, self.tp_2(build_ele))
        er, fig = ge.MakeUnion(
            fig, self.tp_3(build_ele, sign=sign))
        er, fig = ge.MakeUnion(fig, self.tp_4(build_ele))
        er, fig = ge.MakeUnion(fig, self.tp_2_2(build_ele))
        er, fig = ge.MakeUnion(fig, self.tp_4(
            build_ele, build_ele.widl.value - build_ele.cutll.value * 2, build_ele.widt.value, 10))
        er, fig = ge.MakeUnion(fig, self.tp_2_3(build_ele))
        er, fig = ge.MakeUnion(fig, self.tp_4_2(build_ele))
        er, fig = ge.MakeUnion(fig, self.tp_4_2(
            build_ele, build_ele.widl.value - build_ele.cutll.value * 2, build_ele.widt.value, 10))
        er, fig = ge.MakeUnion(fig, self.tp_3_3(build_ele))
        er, fig = ge.MakeUnion(fig, self.tp_last(build_ele))
        return fig

    def cnt(self, build_ele):
        data = get(build_ele)
        poliline = ge.Polygon3D()
        poliline += ge.Point3D(0, data[0], data[1])
        poliline += ge.Point3D(0, data[2] - data[0], data[1])
        poliline += ge.Point3D(data[3], data[2] - data[0], data[1])
        poliline += ge.Point3D(data[3] + data[4], data[2] -
                               data[0] - (data[2] - data[0] * 2 - data[5]) / 2, data[1])
        poliline += ge.Point3D(data[6] - (data[3] + data[4]),
                               data[2] - data[0] - (data[2] - data[0] * 2 - data[5]) / 2, data[1])
        poliline += ge.Point3D(data[6] - data[3], data[2] - data[0], data[1])
        poliline += ge.Point3D(data[6], data[2] - data[0], data[1])
        poliline += ge.Point3D(data[6], data[0], data[1])
        poliline += ge.Point3D(data[6] - data[3], data[0], data[1])
        poliline += ge.Point3D(data[6] - data[3] - data[4],
                               data[0] + (data[2] - data[0] * 2 - data[5]) / 2, data[1])
        poliline += ge.Point3D(data[3] + data[4],
                               data[0] + (data[2] - data[0] * 2 - data[5]) / 2, data[1])
        poliline += ge.Point3D(data[3], data[0], data[1])
        poliline += ge.Point3D(0, data[0], data[1])

        tr = ge.Polyline3D()
        tr += ge.Point3D(0, data[0], data[1])
        tr += ge.Point3D(0, data[0], data[1] + build_ele.him.value)

        er, fig = ge.CreatePolyhedron(poliline, tr)
        return fig
