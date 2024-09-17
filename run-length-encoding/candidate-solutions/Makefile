SHELL := /bin/bash

# If the first argument is "check"...
ifeq (check,$(firstword $(MAKECMDGOALS)))
  # use the rest as arguments for "check"
  CANDIDATE_NUMBER := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
  # ...and turn them into do-nothing targets
  $(eval $(CANDIDATE_NUMBER):;@:)
endif

ifeq (pytest,$(firstword $(MAKECMDGOALS)))
  CANDIDATE_NUMBER := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
  $(eval $(CANDIDATE_NUMBER):;@:)
endif

ifndef CANDIDATE_NUMBER
$(error Please, provide CANDIDATE_NUMBER as argument -> i.e. `make check 1234567890`)
endif

export CANDIDATE_NUMBER

.PHONY: help
help: ## Shows this help message
	@echo -e "\033[1;32mAvailable targets:\033[0m"
	@awk 'BEGIN {FS = ":.*?## "}; /^[a-zA-Z].*:.*##/ {printf "  %-30s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.PHONY: check
check: ## Given the candidate ID number as $CANDIDATE_NUMBER, validates exercise with UnitTest
	@pytest --tb=line ./test_solution_unittest.py

.PHONY: pytest
pytest: ## Given the candidate ID number as $CANDIDATE_NUMBER, validates exercise with PyTest
	@pytest --tb=line ./test_solution_pytest.py

