ZIP = zip
zip = $(ZIP) -X
OUTDIR = ../docs

.PHONY: all clean
all:

clean:
	rm -rf $(OUTDIR)/*.zip tmp* moo* zoo* cur* par*

ifeq "$(shell command -v $(ZIP);)" ""
$(error zip(1) is needed to create zip samples)
endif

$(OUTDIR):
	mkdir -p $(@)

all: $(OUTDIR)/absolute1.zip
$(OUTDIR)/absolute1.zip: | $(OUTDIR)
	rm -f $(@)
	umask 022 && echo moo > mooooooo
	$(zip) -m $(@) mooooooo
	perl -pi -e s,mooooooo,/tmp/moo, $(@)

all: $(OUTDIR)/absolute2.zip
$(OUTDIR)/absolute2.zip: | $(OUTDIR)
	rm -f $(@)
	umask 022 && echo moo > moooooooo
	$(zip) -m $(@) moooooooo
	perl -pi -e s,moooooooo,//tmp/moo, $(@)

all: $(OUTDIR)/relative0.zip
$(OUTDIR)/relative0.zip: | $(OUTDIR)
	rm -f $(@)
	mkdir -m 755 tmp
	umask 022 && echo moo > moo
	cd ./tmp && $(zip) ../$(@) ../moo
	rm -rf tmp moo

all: $(OUTDIR)/relative2.zip
$(OUTDIR)/relative2.zip: | $(OUTDIR)
	rm -f $(@)
	mkdir -p -m 755 tmp/tmp
	umask 022 && echo moo > moo
	cd ./tmp && $(zip) ../$(@) tmp/../../moo
	rm -rf tmp moo

all: $(OUTDIR)/symlink.zip
$(OUTDIR)/symlink.zip: | $(OUTDIR)
	rm -f $(@)
	ln -sf /tmp/moo moo
	$(zip) -y -m $(@) moo
	umask 022 && echo moo > zoo
	$(zip) -m $(@) zoo
	perl -pi -e s/zoo/moo/ $(@)

all: $(OUTDIR)/dirsymlink.zip
$(OUTDIR)/dirsymlink.zip: | $(OUTDIR)
	rm -f $(@)
	ln -sf /tmp tmp
	$(zip) -y -m $(@) tmp
	mkdir -m 755 tmp
	umask 022 && echo moo > tmp/moo
	$(zip) $(@) tmp/moo
	rm -rf tmp

all: $(OUTDIR)/dirsymlink2a.zip
$(OUTDIR)/dirsymlink2a.zip: | $(OUTDIR)
	rm -f $(@)
	ln -sf . cur
	ln -sf cur/.. par
	$(zip) -y -m $(@) cur par
	mkdir -m 755 par
	umask 022 && echo moo > par/moo
	$(zip) $(@) par/moo
	rm -rf par

all: $(OUTDIR)/dirsymlink2b.zip
$(OUTDIR)/dirsymlink2b.zip: | $(OUTDIR)
	rm -f $(@)
	ln -sf . cur
	ln -sf .. par
	$(zip) -y $(@) cur cur/par
	rm -f cur par
	mkdir -m 755 par
	umask 022 && echo moo > par/moo
	$(zip) $(@) par/moo
	rm -rf par

.error = GNU make is required

# vim:ts=4 sts=4 sw=4 noet
