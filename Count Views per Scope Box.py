from Autodesk.Revit.DB import *
from pprint import pprint

view_collector = FilteredElementCollector(doc).OfClass(View)
view_scope_boxes = {}
for v in view_collector:
	sb = v.LookupParameter('Scope Box')
	if sb != None:
		view_scope_boxes[v.Id] = sb.AsElementId()

scope_box_collector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_VolumeOfInterest).WhereElementIsNotElementType()
scope_box_view_counts = {sb.Name: len([v for v in view_scope_boxes if view_scope_boxes[v] == sb.Id]) for sb in scope_box_collector}

pprint(scope_box_view_counts)