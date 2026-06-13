BSDTAR = bsdtar
bsdtar = $(BSDTAR) --format=7zip --absolute-paths
OUTDIR = ../.files

ifeq "$(shell command -v $(BSDTAR);)" ""
$(error bsdtar(1) is needed to create 7zip samples)
endif

.PHONY: all clean FORCE
all:

clean:
	rm -rf $(OUTDIR)/*.7z tmp* moo* cur* par*

$(OUTDIR):
	mkdir -p $(@)

all: $(OUTDIR)/absolute1.7z
$(OUTDIR)/absolute1.7z: FORCE | $(OUTDIR)
	umask 022 && echo moo > moo
	$(bsdtar) -cf $(@) -s ,^,/tmp/, moo
	rm -f moo

# TODO: absolute2.7z
# bsdtar(1) doesn't like paths starting with “//”.
# https://github.com/libarchive/libarchive/issues/740

all: $(OUTDIR)/relative0.7z
$(OUTDIR)/relative0.7z: FORCE | $(OUTDIR)
	umask 022 && echo moo > moo
	$(bsdtar) -cf $(@) -s ,^,../, moo
	rm -f moo

all: $(OUTDIR)/relative2.7z
$(OUTDIR)/relative2.7z: FORCE | $(OUTDIR)
	umask 022 && echo moo > moo
	$(bsdtar) -cf $(@) -s ,^,tmp/../../, moo
	rm -f moo

all: $(OUTDIR)/symlink.7z
$(OUTDIR)/symlink.7z: FORCE | $(OUTDIR)
	ln -sf /tmp/moo moo
	umask 022 && echo moo > moo2
	$(bsdtar) -cf $(@) -s,2,, moo moo2
	rm -f moo moo2

all: $(OUTDIR)/dirsymlink.7z
$(OUTDIR)/dirsymlink.7z: FORCE | $(OUTDIR)
	ln -sf /tmp tmp
	umask 022 && echo moo > moo
	$(bsdtar) -cf $(@) -s,^moo,tmp/moo, tmp moo
	rm -f tmp moo

all: $(OUTDIR)/dirsymlink2a.7z
$(OUTDIR)/dirsymlink2a.7z: FORCE | $(OUTDIR)
	ln -sf . cur
	ln -sf cur/.. par
	mkdir -m 755 par2
	umask 022 && echo moo > par2/moo
	$(bsdtar) -cf $(@) -s,2,, cur par par2
	rm -rf cur par par2

all: $(OUTDIR)/dirsymlink2b.7z
$(OUTDIR)/dirsymlink2b.7z: FORCE | $(OUTDIR)
	ln -sf . cur
	ln -sf .. par
	mkdir -m 755 par2
	umask 022 && echo moo > par2/moo
	$(bsdtar) -cf $(@) -s,2,, cur cur/par par2
	rm -rf cur par par2

.error = GNU make is required

# vim:ts=4 sts=4 sw=4 noet
