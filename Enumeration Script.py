import arcpy

def ScriptTool(param0, param1, param2, param3, param4):
    arcpy.env.workspace = param0
    # sets param0 as a workspace input
    if param1 == "true":
        arcpy.AddMessage('Point features:')
        fcs1 = arcpy.ListFeatureClasses('','POINT')
        arcpy.AddMessage(fcs1)
        # lists all point feature classes within the workspace

    if param2 == "true":
        arcpy.AddMessage('Line features:')
        fcs2 = arcpy.ListFeatureClasses('','LINE')
        arcpy.AddMessage(fcs2)
        # lists all line feature classes within the workspace

    if param3 == "true":
        arcpy.AddMessage('Polygon features:')
        fcs3 = arcpy.ListFeatureClasses('','POLYGON')
        arcpy.AddMessage(fcs3)
        # lists all polygon feature classes within the workspace

    if param4 == "true":
        count1 = len(fcs1)
        count2 = len(fcs2)
        count3 = len(fcs3)
        # collects the count of feature classes returned from previous functions
        
        arcpy.AddMessage('Point features total:')
        arcpy.AddMessage(count1)
        arcpy.AddMessage('Line features total:')
        arcpy.AddMessage(count2)
        arcpy.AddMessage('Polygon features total:')
        arcpy.AddMessage(count3)
    return

if __name__ == "__main__":

    param0 = arcpy.GetParameterAsText(0)
    param1 = arcpy.GetParameterAsText(1)
    param2 = arcpy.GetParameterAsText(2)
    param3 = arcpy.GetParameterAsText(3)
    param4 = arcpy.GetParameterAsText(4)
    ScriptTool(param0, param1, param2, param3, param4)
