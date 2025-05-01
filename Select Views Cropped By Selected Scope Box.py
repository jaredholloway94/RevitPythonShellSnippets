import clr
clr.AddReference('System')
from System.Collections.Generic import List

view_collector = FilteredElementCollector(doc).OfClass(View)

selected_view_ids = []

for v in view_collector:
	sb = v.LookupParameter('Scope Box')
	if sb != None:
		if sb.AsElementId() == s0.Id:
			selected_view_ids.append(v.Id)
			
uidoc.Selection.SetElementIds(List[ElementId](selected_view_ids))
