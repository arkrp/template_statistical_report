TARGETS := Rplots.pdf
all: $(TARGETS)
Rplots.pdf: example_r_experiment.r
	Rscript example_r_experiment.r
clean:
	rm -f $(TARGETS)
.PHONY: clean all
