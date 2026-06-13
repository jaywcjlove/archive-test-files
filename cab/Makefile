PERL = perl
OUTDIR = ../.files
cab = $(PERL) -e 'my ($$out, $$name, $$data) = @ARGV; $$data =~ s/\\n/\n/g; open my $$fh, ">:raw", $$out or die "$$out: $$!"; my $$coff_files = 36 + 8; my $$file = pack("V V v v v v", length($$data), 0, 0, 0, 0, 0x20) . $$name . "\0"; my $$coff_cab_start = 36 + 8 + length($$file); my $$cfdata = pack("V v v", 0, length($$data), length($$data)) . $$data; my $$cb_cabinet = $$coff_cab_start + length($$cfdata); print $$fh "MSCF", pack("V V V V V C C v v v v v", 0, $$cb_cabinet, 0, $$coff_files, 0, 3, 1, 1, 1, 0, 0, 0); print $$fh pack("V v v", $$coff_cab_start, 1, 0); print $$fh $$file, $$cfdata;'

.PHONY: all clean FORCE
all:

clean:
	rm -rf $(OUTDIR)/*.cab *'\\'*

ifeq "$(shell command -v $(PERL);)" ""
$(error perl(1) is needed to create Microsoft cabinet samples)
endif

$(OUTDIR):
	mkdir -p $(@)

all: $(OUTDIR)/absolute1.cab
$(OUTDIR)/absolute1.cab: FORCE | $(OUTDIR)
	$(cab) $(@) '\tmp\moo' 'moo\n'

all: $(OUTDIR)/absolute2.cab
$(OUTDIR)/absolute2.cab: FORCE | $(OUTDIR)
	$(cab) $(@) '\\tmp\moo' 'moo\n'

all: $(OUTDIR)/relative0.cab
$(OUTDIR)/relative0.cab: FORCE | $(OUTDIR)
	$(cab) $(@) '..\moo' 'moo\n'

all: $(OUTDIR)/relative2.cab
$(OUTDIR)/relative2.cab: FORCE | $(OUTDIR)
	$(cab) $(@) 'tmp\..\..\moo' 'moo\n'

.error = GNU make is required

# vim:ts=4 sts=4 sw=4 noet
