"""Demo Buffer Plugin: entry point QGIS loads.

QGIS calls classFactory() to get the plugin class. Nothing else
in this file runs plugin logic; the work lives in plugin.py.
"""


def classFactory(iface):
    from .plugin import DemoBufferPlugin

    return DemoBufferPlugin(iface)
