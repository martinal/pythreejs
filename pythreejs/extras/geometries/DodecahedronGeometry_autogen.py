from ipywidgets import Widget, DOMWidget, widget_serialization, Color
from traitlets import Unicode, Int, CInt, Instance, This, Enum, Tuple, List, Dict, Float, CFloat, Bool

from ...enums import *
from ...traits import *

from ...core.Geometry_autogen import Geometry


class DodecahedronGeometry(Geometry):
    """DodecahedronGeometry
    
    Autogenerated by generate-wrappers.js 
    Date: Tue Oct 18 2016 14:57:27 GMT-0700 (PDT) 
    See http://threejs.org/docs/#Reference/Extras.Geometries/DodecahedronGeometry 
    """
    
    _view_name = Unicode('DodecahedronGeometryView').tag(sync=True)
    _model_name = Unicode('DodecahedronGeometryModel').tag(sync=True)

    radius = CFloat(1).tag(sync=True)
    detail = CInt(0).tag(sync=True)
