from Autodesk.Revit.DB.ExtensibleStorage import Schema

SCHEMA_FILTER = lambda schema: schema.SchemaName.startswith('JH94') # FILL THIS OUT
schemas = list(filter(SCHEMA_FILTER, Schema.ListSchemas()))
	
t = Transaction(doc,'Erase Schemas')
t.Start()
	
for schema in schemas:
	doc.EraseSchemaAndAllEntities(schema)
	
t.Commit()