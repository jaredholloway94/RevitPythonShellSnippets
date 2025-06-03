import os
import csv

sheet_collector = FilteredElementCollector(doc).OfClass(ViewSheet)
title_block_collector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_TitleBlocks).WhereElementIsNotElementType()

with open('RPS_sheets_export.csv','w', newline='') as csv_file:

	csv_writer = csv.writer(csv_file,)

	headers = [
		'Sheet Number',
		'Sheet Name',
		'Title Block Family',
		'Title Block Type',
		'Discipline',
		'Discipline Order',
		'Sheet Order',
		]
		
	csv_writer.writerow(headers)
	
	for sheet in sheet_collector:
	
		tb = list(filter(lambda x: x.OwnerViewId == sheet.Id, title_block_collector))[0]
		tb_type = doc.GetElement(tb.GetTypeId())
		
		data = [
			sheet.SheetNumber,
			sheet.Name,
			tb_type.FamilyName,
			tb_type.LookupParameter('Type Name').AsString(),
			sheet.LookupParameter('Discipline').AsString(),
			sheet.LookupParameter('Discipline Order').AsString(),
			sheet.LookupParameter('Sheet Order').AsString()
			]
			
		csv_writer.writerow(data)