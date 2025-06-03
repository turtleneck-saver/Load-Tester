BACKEND_ROOT := $(shell pwd)

SRC_DIR := $(BACKEND_ROOT)/src

run:
	PYTHONPATH=$(SRC_DIR): uv run locust -f $(SRC_DIR)/app.py
	
commit:
	git add .
	git commit -m "updated $(shell date +%Y-%m-%d)"
	git push origin master


env:
	@echo source .venv/bin/activate
	
