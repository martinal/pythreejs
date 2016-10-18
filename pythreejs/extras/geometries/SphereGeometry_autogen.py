from ipywidgets import Widget, DOMWidget, widget_serialization, Color
from traitlets import Unicode, Int, CInt, Instance, This, Enum, Tuple, List, Dict, Float, CFloat, Bool

from ...enums import *
from ...traits import *

from ...core.Geometry_autogen import Geometry


class SphereGeometry(Geometry):
    """SphereGeometry
    
    Autogenerated by generate-wrappers.js 
    Date: Tue Oct 18 2016 14:57:27 GMT-0700 (PDT) 
    See http://threejs.org/docs/#Reference/Extras.Geometries/SphereGeometry 
    """
    
    _view_name = Unicode('SphereGeometryView').tag(sync=True)
    _model_name = Unicode('SphereGeometryModel').tag(sync=True)

    radius = CInt(50).tag(sync=True)
    widthSegments = CInt(8).tag(sync=True)
    heightSegments = CInt(6).tag(sync=True)
    phiStart = CFloat(0).tag(sync=True)
    phiLength = CFloat(6.283185307179586).tag(sync=True)
    thetaStart = CFloat(0).tag(sync=True)
    thetaLength = CFloat(3.141592653589793).tag(sync=True)
