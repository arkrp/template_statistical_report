DEPENDENCIES := venv
TOPTARGETS := run clean
SUBDIRS := python_experiment_example r_experiment_example

project_directory=$(shell pwd)
export project_directory
data_directory=$(project_directory)/data
export data_directory

run: pdf/paper.pdf
	zathura pdf/paper.pdf

pdf/paper.pdf: paper.tex refs.bib pdf $(SUBDIRS)
	latexmk -pdf -output-directory="./pdf" paper

venv:
	python3 -m venv venv
	venv/bin/pip install matplotlib
	venv/bin/pip install pandas

pdf:
	mkdir pdf

clean:
	-rm -rf pdf
	-rm -rf venv


$(TOPTARGETS): $(SUBDIRS)
$(SUBDIRS): $(DEPENDENCIES)
	$(MAKE) -C $@ $(MAKECMDGOALS)

.PHONY: run clean
.PHONY: $(TOPTARGETS) $(SUBDIRS)
