.PHONY: help
help: # Show help for each of the Makefile target.
	@grep -E '^[a-zA-Z0-9 _]+:.*#'  Makefile | sort | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done

install_requirements_test: # Installl packages requirements for test and linter
	python -m pip install -r requirements_test.txt

linter:
	flake8 .
