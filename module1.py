import apex
from apex.construct import Point3D, Point2D
import time

apex.setScriptUnitSystem(unitSystemName = r'''mm-kg-s-N-K''')
applicationSettingsGeometry = apex.setting.ApplicationSettingsGeometry()
applicationSettingsGeometry.createGeometryInNewPart = apex.setting.CreateGeometryInNewPart.CurrentPart
applicationSettingsGeometry.geometryTessellationIsWatertight = False
applicationSettingsGeometry.geometryEdgeTesselationTolerance = apex.setting.GeometryTessellationTolerance.Medium
applicationSettingsGeometry.geometryFaceTesselationTolerance = apex.setting.GeometryTessellationTolerance.Medium
apex.setting.setApplicationSettingsGeometry(applicationSettingsGeometry = applicationSettingsGeometry)
model_1 = apex.currentModel()

# 
# Start of operations
# 

def prerequisite():
    _importFilter = {
    
}
    model_1.importGeometry(
        geometryFileNames = _geometryFileNames,
        importSolids = True,     #defaults to True
        importSurfaces = True,     #defaults to True
        importCurves = True,     #defaults to True
        importPoints = True,     #defaults to True
        importGeneralBodies = True,     #defaults to True
        importHiddenGeometry = False,     #defaults to False
        importCoordinate = False,     #defaults to True
        importDatumPlane = False,     #defaults to True
        cleanOnImport = True,     #defaults to True
        removeRedundantTopoOnimport = False,     #defaults to False
        loadCompleteTopology = True,     #defaults to True
        sewOnImport = False,     #defaults to False
        skipUnmodified = False,     #defaults to False
        importFilter = _importFilter,
        preview = False,     #defaults to False
        importReviewMode3dxmlCleanOnImport = True,     #defaults to True
        importReviewMode3dxmlSplitOnFeatureVertexAngle = True,     #defaults to True
        importReviewMode3dxmlFeatureAngle = 4.000000000000000e+01,     #defaults to 40.0 degrees
        importReviewMode3dxmlVertexAngle = 4.000000000000000e+01,     #defaults to 40.0 degrees
        importReviewMode3dxmlDetectMachinedFaces = False,     #defaults to False
        importAttributes = False,     #defaults to False
        importPublications = False     #defaults to False
)

def views():
    time.sleep(2)
    apex.disableShowOutput()

    myCamera = apex.display.getCamera()

    myCamera.viewFromZ(reverse=False, viewUp = [0.0, 1.0, 0.0], reset=True)

    myCamera.setViewUp(apex.construct.Vector3D(0.0, 1.0, 0.0))
    
    myCamera.viewFromX(reverse=False, viewUp = [0.0, 0.0, 1.0], reset=True)

    myCamera.setViewUp(apex.construct.Vector3D(0.0, 0.0, 1.0))
    
    myCamera.reset()
    


_geometryFileNames = [
    "D:/Apex2023.1_Manual/Quicklook_Models/Demo_Models_folder/2_Import Parasolid/Demo_02_MidSurface_Gap_Close.xmt_txt"
]

time.sleep (2)
prerequisite()
views()

time.sleep (2)

model_1 = model_1.close()
