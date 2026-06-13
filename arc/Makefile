PERL = perl
OUTDIR = ../.files
arc = $(PERL) -e 'sub crc { my ($$s) = @_; my $$crc = 0; for my $$byte (unpack("C*", $$s)) { $$crc ^= $$byte; for (1 .. 8) { $$crc = ($$crc & 1) ? (($$crc >> 1) ^ 0xA001) : ($$crc >> 1); } } return $$crc & 0xffff; } my ($$out, $$name, $$data) = @ARGV; open my $$fh, ">:raw", $$out or die "$$out: $$!"; print $$fh pack("CCa13VvvvV", 0x1a, 2, $$name, length($$data), 0, 0, crc($$data), length($$data)); print $$fh $$data; print $$fh pack("CC", 0x1a, 0);'

.PHONY: all clean FORCE
all:

clean:
	rm -rf $(OUTDIR)/*.arc tmp* moo*

ifeq "$(shell command -v $(PERL);)" ""
$(error perl(1) is needed to create arc samples)
endif

$(OUTDIR):
	mkdir -p $(@)

all: $(OUTDIR)/absolute1.arc
$(OUTDIR)/absolute1.arc: FORCE | $(OUTDIR)
	$(arc) $(@) /tmp/moo moo

all: $(OUTDIR)/absolute2.arc
$(OUTDIR)/absolute2.arc: FORCE | $(OUTDIR)
	$(arc) $(@) //tmp/moo moo

all: $(OUTDIR)/relative0.arc
$(OUTDIR)/relative0.arc: FORCE | $(OUTDIR)
	$(arc) $(@) ../moo moo

.error = GNU make is required

# vim:ts=4 sts=4 sw=4 noet
