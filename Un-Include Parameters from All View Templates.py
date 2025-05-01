import clr
clr.AddReference('System')
from System.Collections.Generic import List


PARAMETER_NAMES = []

view_collector = FilteredElementCollector(doc).OfClass(View)
view_templates = [ v for v in view_collector if v.IsTemplate ]


t = Transaction(doc,'Un-Include Parameters from All Templates')
t.Start()

try:
	for vt in view_templates:
		params = []
		
		for pn in PARAMETER_NAMES:
			p = vt.LookupParameter(pn)
			if p != None: params.append(p.Id)
			
		vt.SetNonControlledTemplateParameterIds(List[ElementId](params))
except:
	t.Rollback()
	print('Something went wrong!')

else:
	t.Commit()
	print('Success!')