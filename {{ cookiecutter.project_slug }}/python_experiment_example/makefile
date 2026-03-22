TARGETS := example_plot.png example_data_table.csv
all: $(TARGETS)
example_plot.png: example_python_experiment.py
	"$(project_directory)"/venv/bin/python example_python_experiment.py
example_data_table.csv: example_python_experiment.py
	"$(project_directory)"/venv/bin/python example_python_experiment.py
clean:
	rm -f $(TARGETS)
.PHONY: clean all
