"""Processing script: buffer a point layer by a given distance.

Execution context: add this file as a Processing script and run it
from the Processing Toolbox inside QGIS. Headless / standalone
execution is to confirm at validation and is not claimed here.

No credentials are used anywhere in this script.
"""

from qgis.core import (
    QgsProcessing,
    QgsProcessingAlgorithm,
    QgsProcessingException,
    QgsProcessingParameterDistance,
    QgsProcessingParameterFeatureSource,
    QgsProcessingParameterFeatureSink,
    QgsWkbTypes,
)


class BufferDemoPointsAlgorithm(QgsProcessingAlgorithm):
    """Buffer demo points; parameters and outputs declared for reuse."""

    INPUT = "INPUT"
    DISTANCE = "DISTANCE"
    OUTPUT = "OUTPUT"

    def name(self):
        return "bufferdemopoints"

    def displayName(self):
        return "Buffer demo points"

    def group(self):
        return "Demo"

    def groupId(self):
        return "demo"

    def createInstance(self):
        return BufferDemoPointsAlgorithm()

    def initAlgorithm(self, config=None):
        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.INPUT,
                "Input point layer",
                [QgsProcessing.TypeVectorPoint],
            )
        )
        self.addParameter(
            QgsProcessingParameterDistance(
                self.DISTANCE,
                "Buffer distance (in the input layer's map units)",
                defaultValue=0.01,
            )
        )
        self.addParameter(
            QgsProcessingParameterFeatureSink(
                self.OUTPUT,
                "Buffered output",
            )
        )

    def processAlgorithm(self, parameters, context, feedback):
        source = self.parameterAsSource(parameters, self.INPUT, context)
        if source is None:
            raise QgsProcessingException(
                "Input layer could not be loaded. "
                "Check the input path and that the file is readable."
            )
        if source.featureCount() == 0:
            raise QgsProcessingException(
                "Input layer has zero features; no output will be written."
            )

        distance = self.parameterAsDouble(parameters, self.DISTANCE, context)
        if distance < 0:
            raise QgsProcessingException(
                f"Buffer distance must not be negative; got {distance}."
            )

        (sink, dest_id) = self.parameterAsSink(
            parameters,
            self.OUTPUT,
            context,
            source.fields(),
            QgsWkbTypes.Polygon,
            source.sourceCrs(),
        )
        if sink is None:
            raise QgsProcessingException(
                "Output sink could not be created. "
                "Check the output path and that its folder is writable."
            )

        total = source.featureCount()
        for current, feature in enumerate(source.getFeatures()):
            if feedback.isCanceled():
                break
            geom = feature.geometry()
            if geom is None or geom.isEmpty():
                feedback.pushWarning(
                    f"Skipping feature with no geometry "
                    f"(attributes: {feature.attributes()})."
                )
                continue
            out_feature = feature
            out_feature.setGeometry(geom.buffer(distance, 8))
            sink.addFeature(out_feature)
            feedback.setProgress(int(100 * (current + 1) / total))

        return {self.OUTPUT: dest_id}
