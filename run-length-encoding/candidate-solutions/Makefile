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

.PHONY: check
check:
	@pytest --tb=line ./test_solution_unittest.py

.PHONY: pytest
pytest:
	@pytest --tb=line ./test_solution_pytest.py