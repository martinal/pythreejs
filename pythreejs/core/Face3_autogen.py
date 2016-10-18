from ipywidgets import Widget, DOMWidget, widget_serialization, Color
from traitlets import Unicode, Int, CInt, Instance, This, Enum, Tuple, List, Dict, Float, CFloat, Bool

from ..enums import *
from ..traits import *

from .._base.Three import ThreeWidget


class Face3(ThreeWidget):
    """Face3
    
    Autogenerated by generate-wrappers.js 
    Date: Tue Oct 18 2016 14:57:27 GMT-0700 (PDT) 
    See http://threejs.org/docs/#Reference/Core/Face3 
    """
    
    _view_name = Unicode('Face3View').tag(sync=True)
    _model_name = Unicode('Face3Model').tag(sync=True)

    a = CInt(0).tag(sync=True)
    b = CInt(1).tag(sync=True)
    c = CInt(2).tag(sync=True)
    normal = Vector3(default=[0,0,0]).tag(sync=True)
    color = Unicode("#ffffff").tag(sync=True)
    materialIndex = CInt(0).tag(sync=True)
