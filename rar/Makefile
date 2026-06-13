RAR = rar
OUTDIR = ../.files
RAR_PASSWORD = 123
VOLUME_SIZE = 1k
rar = $(RAR) a -idq -ep -m0
rename = $(RAR) rn -idq

.PHONY: all clean FORCE
all:

clean:
	rm -rf $(OUTDIR)/*.rar tmp* moo* zoo* cur par

ifeq "$(shell command -v $(RAR);)" ""
$(error rar(1) is needed to create RAR samples)
endif

$(OUTDIR):
	mkdir -p $(@)

all: $(OUTDIR)/absolute1.rar
$(OUTDIR)/absolute1.rar: FORCE | $(OUTDIR)
	rm -f $(@)
	umask 022 && echo moo > moo
	$(rar) $(@) moo
	$(rename) $(@) moo /tmp/moo
	rm -f moo

all: $(OUTDIR)/absolute2.rar
$(OUTDIR)/absolute2.rar: FORCE | $(OUTDIR)
	rm -f $(@)
	umask 022 && echo moo > moo
	$(rar) $(@) moo
	$(rename) $(@) moo //tmp/moo
	rm -f moo

all: $(OUTDIR)/relative0.rar
$(OUTDIR)/relative0.rar: FORCE | $(OUTDIR)
	rm -f $(@)
	umask 022 && echo moo > moo
	$(rar) $(@) moo
	$(rename) $(@) moo ../moo
	rm -f moo

all: $(OUTDIR)/relative2.rar
$(OUTDIR)/relative2.rar: FORCE | $(OUTDIR)
	rm -f $(@)
	umask 022 && echo moo > moo
	$(rar) $(@) moo
	$(rename) $(@) moo tmp/../../moo
	rm -f moo

all: $(OUTDIR)/symlink.rar
$(OUTDIR)/symlink.rar: FORCE | $(OUTDIR)
	rm -f $(@)
	ln -sf /tmp/moo moo
	umask 022 && echo moo > zoo
	$(rar) -ol $(@) moo zoo
	$(rename) $(@) zoo moo
	rm -f moo zoo

all: $(OUTDIR)/dirsymlink.rar
$(OUTDIR)/dirsymlink.rar: FORCE | $(OUTDIR)
	rm -f $(@)
	ln -sf /tmp tmp
	umask 022 && echo moo > moo
	$(rar) -ol $(@) tmp moo
	$(rename) $(@) moo tmp/moo
	rm -f tmp moo

all: $(OUTDIR)/dirsymlink2a.rar
$(OUTDIR)/dirsymlink2a.rar: FORCE | $(OUTDIR)
	rm -f $(@)
	ln -sf . cur
	ln -sf cur/.. par
	umask 022 && echo moo > moo
	$(rar) -ol $(@) cur par moo
	$(rename) $(@) moo par/moo
	rm -f cur par moo

all: $(OUTDIR)/dirsymlink2b.rar
$(OUTDIR)/dirsymlink2b.rar: FORCE | $(OUTDIR)
	rm -f $(@)
	ln -sf . cur
	ln -sf .. par
	umask 022 && echo moo > moo
	$(rar) -ol $(@) cur cur/par moo
	$(rename) $(@) moo par/moo
	rm -f cur par moo

all: $(OUTDIR)/volume.part01.rar
$(OUTDIR)/volume.part01.rar: FORCE | $(OUTDIR)
	rm -f $(OUTDIR)/volume.part*.rar $(OUTDIR)/volume.rar
	i=0; while [ $$i -lt 4096 ]; do echo moo; i=$$((i + 1)); done > moo
	$(rar) -v$(VOLUME_SIZE) $(OUTDIR)/volume.rar moo
	rm -f moo

all: $(OUTDIR)/password.rar
$(OUTDIR)/password.rar: FORCE | $(OUTDIR)
	rm -f $(@)
	umask 022 && echo moo > moo
	$(rar) -p$(RAR_PASSWORD) $(@) moo
	rm -f moo

.error = GNU make is required

# vim:ts=4 sts=4 sw=4 noet
