generate-html:
	PYTHONPATH=src python src/generate-docs.py html

generate-schemas:
	PYTHONPATH=src python src/generate-docs.py schemas

generate-core-schemas:
	PYTHONPATH=src python src/generate-docs.py core-schemas

generate-all: generate-html generate-schemas
