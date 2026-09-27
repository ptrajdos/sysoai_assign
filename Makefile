ROOTDIR=$(realpath $(dir $(firstword $(MAKEFILE_LIST))))


PACKAGE_DIR=${ROOTDIR}/assignments
VENV_NAME := sysoai_venv
VENV_DIR := $(HOME)/$(VENV_NAME)

PYTHON=python

PIP=pip


ifeq ($(OS),Windows_NT)
	ACTIVATE:=. ${VENV_DIR}/Scripts/activate
else
	ACTIVATE:=. ${VENV_DIR}/bin/activate
endif

CATEGORIES := $(shell find $(PACKAGE_DIR) -mindepth 1 -maxdepth 1 -type d \
	! -name '*.egg-info' ! -name tools | xargs -n1 basename)

ZIP_DIR := $(ROOTDIR)/zips

.PHONY: all clean test install_assignments zip_categories

install_assignments:
	$(ACTIVATE); ${PYTHON} -m ${PIP} install -e ${PACKAGE_DIR}

zip_categories:
	@for cat in $(CATEGORIES); do \
		mkdir -p $(ZIP_DIR); \
		echo "Zipping category: $$cat"; \
		cd $(PACKAGE_DIR) && zip -r $(ZIP_DIR)/$$cat.zip $$cat; \
	done
clean_zips:
	rm -rf $(ZIP_DIR)
