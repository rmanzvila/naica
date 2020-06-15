
COMPOSE := docker-compose  -f compose-dev.yml

ARG=

help:
	@echo
	@echo ----------------------------------------------------------------------
	@echo "   Development commands file                                        "
	@echo ----------------------------------------------------------------------
	@echo
	@echo "	- up	     	            Server up locally"
	@echo "	- build			            Build the containers for development"
	@echo ----------------------------------------------------------------------

build:
	$(COMPOSE) build
	@echo "Building..."

up:
	@echo "Server up..."
	$(COMPOSE) up $(ARG)
