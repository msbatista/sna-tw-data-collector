BASE_DIR := ./
PKG_NAME := sna-tw-data-collector
SRC_DIR := $(BASE_DIR)/$(PKG_NAME)
APP_NAME := sna-tw-data-collector

venv:
	@python3 -m venv .venv
	@source .venv/bin/activate

setup:
	@echo "Install package dependencies"
	@pip install -r requirements.txt --upgrade
	@if [ ! -f .env ]; then \
		cp .env-sample .env ; \
  	fi

docker_build:
	@echo "Building docker image"
	@docker build -t $(APP_NAME) .

docker_run:
	@echo "Starting up docker app"
	@docker run -i -t --rm -p 8003:5050 --name="$(APP_NAME)" $(APP_NAME)

run:
	@python app.py