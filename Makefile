SRC = main.tex
PDF = main.pdf
AUX = main.aux
TEXC := xelatex
TEXC_OPTS += -shell-escape --synctex=1
TEXC_OPTS_AUX = $(TEXC_OPTS) --no-pdf

all:$(PDF)

$(AUX): $(BIB)
	$(TEXC) $(TEXC_OPTS_AUX) $(SRC)
	bibtex main
	$(TEXC) $(TEXC_OPTS_AUX) $(SRC)

$(PDF): clean $(AUX) $(SRC)
	$(TEXC) $(TEXC_OPTS) $(SRC)

clean:
	@rm -f $(AUX) $(PDF)
	# @git clean -Xf
