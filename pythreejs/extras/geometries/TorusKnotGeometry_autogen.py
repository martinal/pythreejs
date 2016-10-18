from ipywidgets import Widget, DOMWidget, widget_serialization, Color
from traitlets import Unicode, Int, CInt, Instance, This, Enum, Tuple, List, Dict, Float, CFloat, Bool

from ...enums import *
from ...traits import *

from ...core.Geometry_autogen import Geometry


class TorusKnotGeometry(Geometry):
    """TorusKnotGeometry
    
    Autogenerated by generate-wrappers.js 
    Date: Tue Oct 18 2016 14:57:27 GMT-0700 (PDT) 
    See http://threejs.org/docs/#Reference/Extras.Geometries/TorusKnotGeometry 
    """
    
    _view_name = Unicode('TorusKnotGeometryView').tag(sync=True)
    _model_name = Unicode('TorusKnotGeometryModel').tag(sync=True)

    radius = CFloat(100).tag(sync=True)
    tube = CFloat(40).tag(sync=True)
    tubularSegments = CInt(64).tag(sync=True)
    radialSegments = CInt(8).tag(sync=True)
    p = CInt(2).tag(sync=True)
    q = CInt(3).tag(sync=True)
