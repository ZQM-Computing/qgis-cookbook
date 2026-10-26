"""Demo Buffer Plugin: toolbar button that buffers a point layer.

This is the working-script logic from patterns 01-02, moved
unchanged in structure into a plugin class: initGui() adds the
button, unload() removes it, and run() does the buffering.
No credentials are used anywhere in this plugin.
"""

from qgis.core import QgsProject, QgsVectorLayer
from qgis.PyQt.QtWidgets import QAction, QFileDialog, QMessageBox
import processing


class DemoBufferPlugin:
    """Minimal plugin: one button, one action, clean unload."""

    BUFFER_DISTANCE = 0.01  # map units (degrees for the synthetic CRS84 input)

    def __init__(self, iface):
        self.iface = iface
        self.action = None

    def initGui(self):
        self.action = QAction("Buffer demo layer", self.iface.mainWindow())
        self.action.triggered.connect(self.run)
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("Demo Buffer Plugin", self.action)

    def unload(self):
        if self.action is not None:
            self.iface.removeToolBarIcon(self.action)
            self.iface.removePluginMenu("Demo Buffer Plugin", self.action)
            self.action = None

    def run(self):
        layer = self.iface.activeLayer()
        if layer is None or not isinstance(layer, QgsVectorLayer):
            self.iface.messageBar().pushWarning(
                "Demo Buffer Plugin",
                "Select a vector layer first.",
            )
            return
        if layer.geometryType() != 0:  # 0 = point geometry
            self.iface.messageBar().pushWarning(
                "Demo Buffer Plugin",
                "Selected layer is not a point layer.",
            )
            return
        if not layer.isValid():
            self.iface.messageBar().pushCritical(
                "Demo Buffer Plugin",
                f"Selected layer failed to load: {layer.name()}",
            )
            return
        if layer.featureCount() == 0:
            self.iface.messageBar().pushWarning(
                "Demo Buffer Plugin",
                "Selected layer has zero features; nothing will be written.",
            )
            return

        output_path, _ = QFileDialog.getSaveFileName(
            self.iface.mainWindow(),
            "Save buffered output",
            "buffered_demo.gpkg",
            "GeoPackage (*.gpkg)",
        )
        if not output_path:
            return  # Dialog cancelled; not a failure.

        try:
            result = processing.run(
                "native:buffer",
                {
                    "INPUT": layer,
                    "DISTANCE": self.BUFFER_DISTANCE,
                    "SEGMENTS": 8,
                    "END_CAP_STYLE": 0,
                    "JOIN_STYLE": 0,
                    "MITER_LIMIT": 2,
                    "DISSOLVE": False,
                    "OUTPUT": output_path,
                },
            )
        except Exception as exc:  # Processing reports via exception here
            self.iface.messageBar().pushCritical(
                "Demo Buffer Plugin",
                f"Buffer failed: {exc}",
            )
            return

        out_path = result.get("OUTPUT", output_path)
        out_layer = QgsVectorLayer(out_path, "buffered_demo", "ogr")
        if not out_layer.isValid():
            self.iface.messageBar().pushCritical(
                "Demo Buffer Plugin",
                f"Output failed to load for verification: {out_path}",
            )
            return
        QgsProject.instance().addMapLayer(out_layer)
        self.iface.messageBar().pushSuccess(
            "Demo Buffer Plugin",
            f"Buffered {layer.featureCount()} feature(s) to {out_path}",
        )
