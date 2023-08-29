import remoting

remoting.launchApplication()

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
# Start 
# 

def doSketch_1():
    part_1 = model_1.getCurrentPart()
    if part_1 is None:
        part_1 = model_1.createPart()
    sketch_1 = part_1.createSketchOnGlobalPlane(
        name = 'Sketch 1',
        plane = apex.construct.GlobalPlane.XY,
        alignSketchViewWithViewport = True
    )

    time.sleep(5)

    rectangle_1 = sketch_1.createRectangle2Point(
        name = "Rectangle 1",
        location = Point2D( -6.400000000000000e+02, 3.600000000000000e+02 ),
        diagonal = Point2D( -1.800000000000000e+02, 8.000000000000000e+01 )
    )

    time.sleep(5)

    rectangle_2 = sketch_1.createRectangle3Point(
        name = "Rectangle 2",
        location = Point2D( 1.000000000000000e+02, 4.400000000000000e+02 ),
        orientationPoint = Point2D( 4.000000000000000e+01, 3.200000000000000e+02 ),
        heightPoint = Point2D( 3.840000000000000e+02, 1.4799999999999997e+02 )
    )

    time.sleep(5)

    _pointList = [
        Point2D( -5.400000000000000e+02, -8.000000000000000e+01 ),
        Point2D( -1.800000000000000e+02, -8.000000000000000e+01 )
    ]
    polyline_1 = sketch_1.createPolyline(
        name = "Polyline 1",
        points = _pointList
    )

    time.sleep(5)

    _pointList = [
        Point2D( -4.000000000000000e+01, -2.000000000000000e+02 ),
        Point2D( 2.000000000000000e+01, -1.000000000000000e+02 ),
        Point2D( 2.200000000000000e+02, -2.200000000000000e+02 ),
        Point2D( 3.600000000000000e+02, -1.200000000000000e+02 ),
        Point2D( 4.200000000000000e+02, -8.000000000000000e+01 )
    ]
    spline_1 = sketch_1.createSpline(
        name = "Spline 1",
        points = _pointList,
        asPolyline = False
    )

    time.sleep(5)

    circle_1 = sketch_1.createCircleCenterPoint(
        name = "Circle 1",
        centerPoint = Point2D( 6.200000000000000e+02, 3.800000000000000e+02 ),
        pointOnCircle = Point2D( 7.200000000000000e+02, 3.800000000000000e+02 )
    )

    time.sleep(5)

    circle_2 = sketch_1.createCircle3Point(
        name = "Circle 2",
        point1 = Point2D( 6.400000000000000e+02, 1.000000000000000e+02 ),
        point2 = Point2D( 6.200000000000000e+02, 2.000000000000000e+01 ),
        point3 = Point2D( 5.000000000000000e+02, 0.0 )
    )

    time.sleep(5)

    ellipse_1 = sketch_1.createEllipse3Point(
        name = "Ellipse 1",
        centerPoint = Point2D( -7.000000000000000e+02, -3.200000000000000e+02 ),
        pointAxis1 = Point2D( -6.000000000000000e+02, -3.200000000000000e+02 ),
        pointAxis2 = Point2D( -5.800000000000000e+02, -2.800000000000000e+02 )
    )

    time.sleep(5)

    return sketch_1.completeSketch( fillSketches = True )

newbodies = doSketch_1()


_target = apex.EntityCollection()
part_2 = apex.getPart( pathName = apex.currentModel().name + "/Part 1" )
surface_1 = part_2.getSurface( name = "Surface 1" )
_ids = '1'
_target.extend( surface_1.getFaces( ids = _ids ) )
result = apex.geometry.pushPull(
    target = _target,
    method = apex.geometry.PushPullMethod.Normal,
    behavior = apex.geometry.PushPullBehavior.Extrude,
    removeInnerLoops = False,
    createBooleanUnion = False,
    distance = 1.8723630905151367e+02,
    direction = [ 0.0, 0.0, 1.000000000000000 ]
)

_target = apex.EntityCollection()
part_2 = apex.getPart( pathName = apex.currentModel().name + "/Part 1" )
surface_2 = part_2.getSurface( name = "Surface 2" )
_ids = '21'
_target.extend( surface_2.getFaces( ids = _ids ) )
result = apex.geometry.pushPull(
    target = _target,
    method = apex.geometry.PushPullMethod.Normal,
    behavior = apex.geometry.PushPullBehavior.Extrude,
    removeInnerLoops = False,
    createBooleanUnion = False,
    distance = 1.1293315887451172e+02,
    direction = [ 0.0, 0.0, 1.000000000000000 ]
)

_target = apex.EntityCollection()
part_2 = apex.getPart( pathName = apex.currentModel().name + "/Part 1" )
surface_3 = part_2.getSurface( name = "Surface 3" )
_ids = '51'
_target.extend( surface_3.getFaces( ids = _ids ) )
result = apex.geometry.pushPull(
    target = _target,
    method = apex.geometry.PushPullMethod.Normal,
    behavior = apex.geometry.PushPullBehavior.Extrude,
    removeInnerLoops = False,
    createBooleanUnion = False,
    distance = 9.646892547607422e+01,
    direction = [ 0.0, 0.0, 1.000000000000000 ]
)

_target = apex.EntityCollection()
part_2 = apex.getPart( pathName = apex.currentModel().name + "/Part 1" )
surface_4 = part_2.getSurface( name = "Surface 4" )
_ids = '41'
_target.extend( surface_4.getFaces( ids = _ids ) )
result = apex.geometry.pushPull(
    target = _target,
    method = apex.geometry.PushPullMethod.Normal,
    behavior = apex.geometry.PushPullBehavior.Extrude,
    removeInnerLoops = False,
    createBooleanUnion = False,
    distance = 1.2671470642089844e+02,
    direction = [ 0.0, 0.0, 1.000000000000000 ]
)

_target = apex.EntityCollection()
part_2 = apex.getPart( pathName = apex.currentModel().name + "/Part 1" )
surface_5 = part_2.getSurface( name = "Surface 5" )
_ids = '31'
_target.extend( surface_5.getFaces( ids = _ids ) )
result = apex.geometry.pushPull(
    target = _target,
    method = apex.geometry.PushPullMethod.Normal,
    behavior = apex.geometry.PushPullBehavior.Extrude,
    removeInnerLoops = False,
    createBooleanUnion = False,
    distance = 1.0381460189819336e+02,
    direction = [ 0.0, 0.0, 1.000000000000000 ]
)

_target = apex.EntityCollection()
part_2 = apex.getPart( pathName = apex.currentModel().name + "/Part 1" )
curve_1 = part_2.getCurve( name = "Curve 2" )
_ids = '61'
_target.extend( curve_1.getEdges( ids = _ids ) )
result = apex.mesh.createCurveMesh(
    name = "",
    target = _target,
    meshSize = 10.,
    elementOrder = apex.mesh.ElementOrder.Linear
)

_target = apex.EntityCollection()
part_2 = apex.getPart( pathName = apex.currentModel().name + "/Part 1" )
curve_2 = part_2.getCurve( name = "Curve 1" )
_ids = '71'
_target.extend( curve_2.getEdges( ids = _ids ) )
result = apex.mesh.createCurveMesh(
    name = "",
    target = _target,
    meshSize = 10.,
    elementOrder = apex.mesh.ElementOrder.Linear
)

_target = apex.EntityCollection()
part_2 = apex.getPart( pathName = apex.currentModel().name + "/Part 1" )
solid_1 = part_2.getSolid( name = "Solid 1" )
_target.append( solid_1 )
featuremeshtypes_1 = apex.mesh.FeatureMeshTypeVector()
result = apex.mesh.createSurfaceMesh(
    name = "",
    target = _target,
    meshSize = 10.,
    meshType = apex.mesh.SurfaceMeshElementShape.Mixed,
    meshMethod = apex.mesh.SurfaceMeshMethod.Auto,
    mappedMeshDominanceLevel = 2,
    elementOrder = apex.mesh.ElementOrder.Linear,
    allQuadBoundary = False,
    refineMeshUsingCurvature = False,
    curvatureType = apex.mesh.CurvatureType.EdgeAndFace,
    elementGeometryDeviationRatio = 0.10,
    elementMinEdgeLengthRatio = 0.20,
    proximityRefinement = False,
    growFaceMeshSize = False,
    faceMeshGrowthRatio = 1.2,
    createFeatureMeshes = False,
    featureMeshTypes = featuremeshtypes_1,
    projectMidsideNodesToGeometry = True,
    useMeshFlowOptimization = True,
    meshFlow = apex.mesh.MeshFlow.Grid,
    minimalMesh = False
)

_target = apex.EntityCollection()
part_2 = apex.getPart( pathName = apex.currentModel().name + "/Part 1" )
solid_2 = part_2.getSolid( name = "Solid 2" )
_target.append( solid_2 )
featuremeshtypes_2 = apex.mesh.FeatureMeshTypeVector()
result = apex.mesh.createSurfaceMesh(
    name = "",
    target = _target,
    meshSize = 10.,
    meshType = apex.mesh.SurfaceMeshElementShape.Mixed,
    meshMethod = apex.mesh.SurfaceMeshMethod.Auto,
    mappedMeshDominanceLevel = 2,
    elementOrder = apex.mesh.ElementOrder.Linear,
    allQuadBoundary = False,
    refineMeshUsingCurvature = False,
    curvatureType = apex.mesh.CurvatureType.EdgeAndFace,
    elementGeometryDeviationRatio = 0.10,
    elementMinEdgeLengthRatio = 0.20,
    proximityRefinement = False,
    growFaceMeshSize = False,
    faceMeshGrowthRatio = 1.2,
    createFeatureMeshes = False,
    featureMeshTypes = featuremeshtypes_2,
    projectMidsideNodesToGeometry = True,
    useMeshFlowOptimization = True,
    meshFlow = apex.mesh.MeshFlow.Grid,
    minimalMesh = False
)

_target = apex.EntityCollection()
part_2 = apex.getPart( pathName = apex.currentModel().name + "/Part 1" )
solid_3 = part_2.getSolid( name = "Solid 5" )
_target.append( solid_3 )
featuremeshtypes_3 = apex.mesh.FeatureMeshTypeVector()
result = apex.mesh.createSolidMesh(
    name = "",
    target = _target,
    meshSize = 10.,
    elementOrder = apex.mesh.ElementOrder.Quadratic,
    refineMeshUsingCurvature = True,
    elementGeometryDeviationRatio = 0.10,
    elementMinEdgeLengthRatio = 0.20,
    autoimprove = True,
    growFaceMeshSize = False,
    faceMeshGrowthRatio = 1.5,
    coarsenMeshInternally = True,
    interiorCoarseningFactor = 10.,
    ignoreBadEdges = True,
    collapseShortElementEdges = False,
    edgeLengthCollapseLimit = 0.5,
    createFeatureMeshes = False,
    featureMeshTypes = featuremeshtypes_3,
    createMinLayers = False,
    approximateNumLayers = 2.0,
    projectMidsideNodesToGeometry = True
)

_target = apex.EntityCollection()
part_2 = apex.getPart( pathName = apex.currentModel().name + "/Part 1" )
solid_4 = part_2.getSolid( name = "Solid 4" )
_target.append( solid_4 )
featuremeshtypes_4 = apex.mesh.FeatureMeshTypeVector()
result = apex.mesh.createSolidMesh(
    name = "",
    target = _target,
    meshSize = 10.,
    elementOrder = apex.mesh.ElementOrder.Quadratic,
    refineMeshUsingCurvature = True,
    elementGeometryDeviationRatio = 0.10,
    elementMinEdgeLengthRatio = 0.20,
    autoimprove = True,
    growFaceMeshSize = False,
    faceMeshGrowthRatio = 1.5,
    coarsenMeshInternally = True,
    interiorCoarseningFactor = 10.,
    ignoreBadEdges = True,
    collapseShortElementEdges = False,
    edgeLengthCollapseLimit = 0.5,
    createFeatureMeshes = False,
    featureMeshTypes = featuremeshtypes_4,
    createMinLayers = False,
    approximateNumLayers = 2.0,
    projectMidsideNodesToGeometry = True
)

_target = apex.EntityCollection()
part_2 = apex.getPart( pathName = apex.currentModel().name + "/Part 1" )
solid_5 = part_2.getSolid( name = "Solid 3" )
_target.append( solid_5 )
featuremeshtypes_5 = apex.mesh.FeatureMeshTypeVector()
result = apex.mesh.createSolidMesh(
    name = "",
    target = _target,
    meshSize = 10.,
    elementOrder = apex.mesh.ElementOrder.Quadratic,
    refineMeshUsingCurvature = True,
    elementGeometryDeviationRatio = 0.10,
    elementMinEdgeLengthRatio = 0.20,
    autoimprove = True,
    growFaceMeshSize = False,
    faceMeshGrowthRatio = 1.5,
    coarsenMeshInternally = True,
    interiorCoarseningFactor = 10.,
    ignoreBadEdges = True,
    collapseShortElementEdges = False,
    edgeLengthCollapseLimit = 0.5,
    createFeatureMeshes = False,
    featureMeshTypes = featuremeshtypes_5,
    createMinLayers = False,
    approximateNumLayers = 2.0,
    projectMidsideNodesToGeometry = True
)

_target = apex.EntityCollection()
part_2 = apex.getPart( pathName = apex.currentModel().name + "/Part 1" )
solid_4 = part_2.getSolid( name = "Solid 4" )
_target.append( solid_4 )
featuremeshtypes_6 = apex.mesh.FeatureMeshTypeVector()
result = apex.mesh.createSolidMesh(
    name = "",
    target = _target,
    meshSize = 0.0,
    elementOrder = apex.mesh.ElementOrder.Quadratic,
    refineMeshUsingCurvature = True,
    elementGeometryDeviationRatio = 0.10,
    elementMinEdgeLengthRatio = 0.20,
    autoimprove = True,
    growFaceMeshSize = False,
    faceMeshGrowthRatio = 1.5,
    coarsenMeshInternally = True,
    interiorCoarseningFactor = 10.,
    ignoreBadEdges = True,
    collapseShortElementEdges = False,
    edgeLengthCollapseLimit = 0.5,
    createFeatureMeshes = False,
    featureMeshTypes = featuremeshtypes_6,
    createMinLayers = False,
    approximateNumLayers = 2.0,
    projectMidsideNodesToGeometry = True
)

_target = apex.EntityCollection()
part_2 = apex.getPart( pathName = apex.currentModel().name + "/Part 1" )
solid_5 = part_2.getSolid( name = "Solid 3" )
_target.append( solid_5 )
featuremeshtypes_7 = apex.mesh.FeatureMeshTypeVector()
result = apex.mesh.createSolidMesh(
    name = "",
    target = _target,
    meshSize = 78.,
    elementOrder = apex.mesh.ElementOrder.Quadratic,
    refineMeshUsingCurvature = True,
    elementGeometryDeviationRatio = 0.10,
    elementMinEdgeLengthRatio = 0.20,
    autoimprove = True,
    growFaceMeshSize = False,
    faceMeshGrowthRatio = 1.5,
    coarsenMeshInternally = True,
    interiorCoarseningFactor = 10.,
    ignoreBadEdges = True,
    collapseShortElementEdges = False,
    edgeLengthCollapseLimit = 0.5,
    createFeatureMeshes = False,
    featureMeshTypes = featuremeshtypes_7,
    createMinLayers = False,
    approximateNumLayers = 2.0,
    projectMidsideNodesToGeometry = True
)

# 
# stopped
# 
