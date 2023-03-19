import numpy
import arcgis
import arcpy
import os

os.chdir(r'C:\Calluna\Dokument\Tutorial\ArcPy\GIS_Python_Tutorial_VS_Code_Conda')
os.listdir()


outPath = r'C:\Calluna\Dokument\Tutorial\ArcPy\GIS_Python_Tutorial_VS_Code_Conda\out'
rootDir = r'C:\\Calluna\Dokument\\Tutorial\ArcPy\\GIS_Python_Tutorial_VS_Code_Conda\\'

arcpy.env.overwriteOutput = True

myPoints = rootDir+'AFG_Conflict_Event.shp'
myArea = rootDir+'MyArea.shp'

arcpy.MakeFeatureLayer_management(myPoints, 'myPointLayer')
arcpy.MakeFeatureLayer_management(myArea, 'myAreaLayer', """ "Valley" = 'Bigvalley' """)  

arcpy.FeatureClassToFeatureClass_conversion('myAreaLayer', outPath, 'areaSubset.shp')
arcpy.SelectLayerByLocation_management('myPointLayer','WITHIN','myAreaLayer')

arcpy.FeatureClassToFeatureClass_conversion('myPointLayer', outPath, 'pointSubset2.shp')






arcpy.management.SelectLayerByLocation(
    in_layer="AFG_Conflict_Event",
    overlap_type="INTERSECT",
    select_features="MyArea",
    search_distance=None,
    selection_type="NEW_SELECTION",
    invert_spatial_relationship="NOT_INVERT"
)

