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

.PHONY: all clean test

install_assignments:
	$(ACTIVATE); ${PYTHON} -m ${PIP} install -e ${PACKAGE_DIR}