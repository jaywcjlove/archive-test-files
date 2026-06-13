cpio = cpio -R 0:0
OUTDIR = ../.files

.PHONY: all clean FORCE
all:

clean:
	rm -rf $(OUTDIR)/*.cpio tmp* moo* zoo* cur par

ifeq "$(shell command -v cpio;)" ""
$(error cpio(1) is needed to create cpio samples)
endif

$(OUTDIR):
	mkdir -p $(@)

all: $(OUTDIR)/absolute1.cpio
$(OUTDIR)/absolute1.cpio: FORCE | $(OUTDIR)
	umask 022 && echo moo > mooooooo
	echo mooooooo | $(cpio) -o > moo.cpio
	rm mooooooo
	perl -pi -e s,mooooooo,/tmp/moo, moo.cpio
	mv moo.cpio $(@)

all: $(OUTDIR)/absolute2.cpio
$(OUTDIR)/absolute2.cpio: FORCE | $(OUTDIR)
	umask 022 && echo moo > moooooooo
	echo moooooooo | $(cpio) -o > moo.cpio
	rm moooooooo
	perl -pi -e s,moooooooo,//tmp/moo, moo.cpio
	mv moo.cpio $(@)

all: $(OUTDIR)/relative0.cpio
$(OUTDIR)/relative0.cpio: FORCE | $(OUTDIR)
	mkdir -m 755 tmp
	umask 022 && echo moo > moo
	cd ./tmp && echo ../moo | $(cpio) -o > ../moo.cpio
	rm -rf tmp moo
	mv moo.cpio $(@)

all: $(OUTDIR)/relative2.cpio
$(OUTDIR)/relative2.cpio: FORCE | $(OUTDIR)
	mkdir -p -m 755 tmp/tmp
	umask 022 && echo moo > moo
	cd ./tmp && echo tmp/../../moo | $(cpio) -o > ../moo.cpio
	rm -rf tmp moo
	mv moo.cpio $(@)

all: $(OUTDIR)/symlink.cpio
$(OUTDIR)/symlink.cpio: FORCE | $(OUTDIR)
	ln -sf /tmp/moo moo
	umask 022 && echo moo > zoo
	printf 'moo\nzoo\n' | $(cpio) -o > moo.cpio
	rm -f moo zoo
	perl -pi -e s/zoo/moo/ moo.cpio
	mv moo.cpio $(@)

all: $(OUTDIR)/dirsymlink.cpio
$(OUTDIR)/dirsymlink.cpio: FORCE | $(OUTDIR)
	ln -sf /tmp tmp
	mkdir -m 755 moo
	umask 022 && echo moo > moo/moo
	printf 'tmp\nmoo/moo\n' | $(cpio) -o > moo.cpio
	rm -rf tmp moo
	perl -pi -e s,moo/,tmp/, moo.cpio
	mv moo.cpio $(@)

all: $(OUTDIR)/dirsymlink2a.cpio
$(OUTDIR)/dirsymlink2a.cpio: FORCE | $(OUTDIR)
	ln -sf . cur
	ln -sf cur/.. par
	mkdir -m 755 moo
	umask 022 && echo moo > moo/moo
	printf 'cur\npar\nmoo/moo\n' | $(cpio) -o > moo.cpio
	rm -rf cur par moo
	perl -pi -e s,moo/,par/, moo.cpio
	mv moo.cpio $(@)

all: $(OUTDIR)/dirsymlink2b.cpio
$(OUTDIR)/dirsymlink2b.cpio: FORCE | $(OUTDIR)
	ln -sf . cur
	ln -sf .. par
	mkdir -m 755 moo
	umask 022 && echo moo > moo/moo
	printf 'cur\ncur/par\nmoo/moo\n' | $(cpio) -o > moo.cpio
	rm -rf cur par moo
	perl -pi -e s,moo/,par/, moo.cpio
	mv moo.cpio $(@)

.error = GNU make is required

# vim:ts=4 sts=4 sw=4 noet
