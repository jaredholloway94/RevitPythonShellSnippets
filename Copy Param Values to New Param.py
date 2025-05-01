OLD_PARAM_NAME = ''
NEW_PARAM_NAME = ''
elem_collector = FilteredElementCollector(doc)


def get_param_value_by_storage_type(p):
	if p.StorageType == StorageType.String:
		return p.AsString()
	elif p.StorageType == StorageType.Integer:
		return p.AsInteger()
	elif p.StorageType == StorageType.Double:
		return p.AsDouble()
	elif p.StorageType == StorageType.ElementId:
		return p.AsElementId()
	else:
		raise "Could not determine parameter storage type!"


def set_param_value_by_storage_type(p, v):
	if p.StorageType == StorageType.String:
		p.Set(str(v))
	elif p.StorageType == StorageType.Integer:
		p.Set(int(v))
	elif p.StorageType == StorageType.Double:
		p.Set(float(v))
	elif p.StorageType == StorageType.ElementId:
		p.Set(ElementId(v))
	else:
		raise "Could not determine parameter storage type!"


def main():
	t = Transaction(doc,'Copy Param Values to New Param')
	t.Start()
	
	try:
		for e in elem_collector:
			old_param = e.LookupParameter(OLD_PARAM_NAME)
			new_param = e.LookupParameter(NEW_PARAM_NAME)
			
			# check that both parameters exist on the element
			if old_param != None and new_param != None:
				set_param_value_by_storage_type(new_param, get_param_value_by_storage_type(old_param))
				
	except Exception as e:
		t.RollBack()
		print('Something went wrong!\n')
		print(e)
	
	else:
		t.Commit()
		print('Success!')
		

if __name__ == '__main__':
	main()