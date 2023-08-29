# coding: utf-8
# Macro created by MSC Apex 2023.1 GA - Version CLR:005559-1d0c64b2
# Macro created on Aug 29, 2023 at 12:03:48
# 
# Macro Name = 
# 
# Macro Description = 
# 
# Macro Hot Key = 
# 
# Initialize environment for macro execution
# 

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
# Start of recorded operations
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
    ok = apex.runPythonScript( filename = "C:/Users/taccuser/Documents/MSC_Apex Workspace/Custom Tools 2023.1/Apex Utilities/Views/Aircraft Views/Front View/src/aircraftFrontView.py" )
    time.sleep(2)
    ok = apex.runPythonScript( filename = "C:/Users/taccuser/Documents/MSC_Apex Workspace/Custom Tools 2023.1/Apex Utilities/Views/Aircraft Views/Rear View/src/aircraftRearView.py" )
    time.sleep(2)
    ok = apex.runPythonScript( filename = "C:/Users/taccuser/Documents/MSC_Apex Workspace/Custom Tools 2023.1/Apex Utilities/Views/Aircraft Views/Top View/src/aircraftTopView.py" )
    time.sleep(2)
    ok = apex.runPythonScript( filename = "C:/Users/taccuser/Documents/MSC_Apex Workspace/Custom Tools 2023.1/Apex Utilities/Views/Aircraft Views/Bottom View/src/aircraftBottomView.py"  )
    time.sleep(2)
    ok = apex.runPythonScript( filename = "C:/Users/taccuser/Documents/MSC_Apex Workspace/Custom Tools 2023.1/Apex Utilities/Views/Aircraft Views/RHS View/src/aircraftRhsView.py" )
    time.sleep(2)
    ok = apex.runPythonScript( filename = "C:/Users/taccuser/Documents/MSC_Apex Workspace/Custom Tools 2023.1/Apex Utilities/Views/Aircraft Views/LHS View/src/aircraftLhsView.py" )
    time.sleep(2)
    ok = apex.runPythonScript( filename = "C:/Users/taccuser/Documents/MSC_Apex Workspace/Custom Tools 2023.1/Apex Utilities/Views/Aircraft Views/Iso 1/src/aircraftIso1View.py" )
    time.sleep(2)
    ok = apex.runPythonScript( filename = "C:/Users/taccuser/Documents/MSC_Apex Workspace/Custom Tools 2023.1/Apex Utilities/Views/Aircraft Views/Iso 2/src/aircraftIso2View.py" )
    time.sleep(2)
    ok = apex.runPythonScript( filename = "C:/Users/taccuser/Documents/MSC_Apex Workspace/Custom Tools 2023.1/Apex Utilities/Views/Aircraft Views/Iso 3/src/aircraftIso3View.py" )
    time.sleep(2)
    ok = apex.runPythonScript( filename = "C:/Users/taccuser/Documents/MSC_Apex Workspace/Custom Tools 2023.1/Apex Utilities/Views/Aircraft Views/Iso 4/src/aircraftIso4View.py" )
    time.sleep(2)


_geometryFileNames = [
    "D:/Apex2023.1_Manual/Quicklook_Models/Demo_Models_folder/2_Import Parasolid/Demo_02_MidSurface_Gap_Close.xmt_txt"
]

time.sleep (2)
prerequisite()
views()

time.sleep (2)

model_1 = model_1.close()

_geometryFileNames = [
    "D:/Apex2023.1_Manual/Quicklook_Models/Demo_Models_folder/2_Import Parasolid/engine_block.xmt_txt"
]

time.sleep (2)
prerequisite()
views()

model_1 = model_1.close()

_geometryFileNames = [
    "D:/Apex2023.1_Manual/Quicklook_Models/Demo_Models_folder/2_Import Parasolid/floor2_1.X_T"
]

time.sleep (2)
prerequisite()
views()

model_1 = model_1.close()

_geometryFileNames = [
    "D:/Apex2023.1_Manual/Quicklook_Models/Demo_Models_folder/2_Import Parasolid/天线_model.xmt"
]

time.sleep (2)
prerequisite()
views()

model_1 = model_1.close()

# 
# Macro recording stopped on Aug 29, 2023 at 12:06:02
# 
