# -*- coding: utf-8 -*-

from . import single_page_renderers
from . import multi_page_renderer

# The renderers registry
_RENDERERS = [
    single_page_renderers.SinglePageRendererNoIndex,
    single_page_renderers.SinglePageRendererIndexBottom,
    single_page_renderers.SinglePageRendererIndexOnSide,
    multi_page_renderer.MultiPageRenderer,
    ]

def get_renderer_class_by_name(name):
    """Retrieves a renderer class, by name."""
    for renderer in _RENDERERS:
        if renderer.name == name:
            return renderer
    raise LookupError('The requested renderer %s was not found!' % name)

def get_renderers():
    """Returns the list of available renderers' names."""
    return _RENDERERS
