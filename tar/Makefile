PERL = perl
OUTDIR = ../.files
tar = $(PERL) -e 'sub pad { my ($$s, $$n) = @_; return $$s . ("\0" x ($$n - length($$s))); } sub octal { my ($$v, $$n) = @_; return sprintf("%0*o\0 ", $$n - 2, $$v); } sub entry { my ($$fh, $$type, $$name, $$payload) = @_; my $$is_link = $$type eq "2"; my $$data = $$is_link ? "" : $$payload; my $$link = $$is_link ? $$payload : ""; my $$hdr = pad($$name, 100) . octal($$is_link ? 0777 : 0644, 8) . octal(0, 8) . octal(0, 8) . octal(length($$data), 12) . octal(0, 12) . "        " . $$type . pad($$link, 100) . "ustar\0" . "00" . pad("root", 32) . pad("root", 32) . pad("", 8) . pad("", 8) . pad("", 155) . pad("", 12); my $$sum = 0; $$sum += $$_ for unpack("C*", $$hdr); substr($$hdr, 148, 8) = sprintf("%06o\0 ", $$sum); print $$fh $$hdr; return if $$is_link; print $$fh $$data; print $$fh "\0" x ((512 - length($$data) % 512) % 512); } my $$out = shift @ARGV; open my $$fh, ">:raw", $$out or die "$$out: $$!"; while (@ARGV) { my ($$type, $$name, $$payload) = splice(@ARGV, 0, 3); $$payload =~ s/\\n/\n/g; entry($$fh, $$type, $$name, $$payload); } print $$fh "\0" x 1024;'

.PHONY: all clean FORCE
all:

clean:
	rm -rf $(OUTDIR)/*.tar tmp* moo* cur* par*

ifeq "$(shell command -v $(PERL);)" ""
$(error perl(1) is needed to create tar samples)
endif

$(OUTDIR):
	mkdir -p $(@)

all: $(OUTDIR)/absolute1.tar
$(OUTDIR)/absolute1.tar: FORCE | $(OUTDIR)
	$(tar) $(@) 0 /tmp/moo 'moo\n'

all: $(OUTDIR)/absolute2.tar
$(OUTDIR)/absolute2.tar: FORCE | $(OUTDIR)
	$(tar) $(@) 0 //tmp/moo 'moo\n'

all: $(OUTDIR)/relative0.tar
$(OUTDIR)/relative0.tar: FORCE | $(OUTDIR)
	$(tar) $(@) 0 ../moo 'moo\n'

all: $(OUTDIR)/relative2.tar
$(OUTDIR)/relative2.tar: FORCE | $(OUTDIR)
	$(tar) $(@) 0 tmp/../../moo 'moo\n'

all: $(OUTDIR)/symlink.tar
$(OUTDIR)/symlink.tar: FORCE | $(OUTDIR)
	$(tar) $(@) 2 moo /tmp/moo 0 moo 'moo\n'

all: $(OUTDIR)/dirsymlink.tar
$(OUTDIR)/dirsymlink.tar: FORCE | $(OUTDIR)
	$(tar) $(@) 2 tmp /tmp 0 tmp/moo 'moo\n'

all: $(OUTDIR)/dirsymlink2a.tar
$(OUTDIR)/dirsymlink2a.tar: FORCE | $(OUTDIR)
	$(tar) $(@) 2 cur . 2 par cur/.. 0 par/moo 'moo\n'

all: $(OUTDIR)/dirsymlink2b.tar
$(OUTDIR)/dirsymlink2b.tar: FORCE | $(OUTDIR)
	$(tar) $(@) 2 cur . 2 cur/par .. 0 par/moo 'moo\n'

.error = GNU make is required

# vim:ts=4 sts=4 sw=4 noet
