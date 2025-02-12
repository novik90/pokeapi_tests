CHROME?= --browser chrome
FF?= --browser firefox

test-all:
	pytest tests/ -v

test-ui:
	pytest -m UI -v --headed
test-api:
	pytest -m "not UI" -v