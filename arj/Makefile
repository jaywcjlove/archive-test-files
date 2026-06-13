PERL = perl
OUTDIR = ../docs
arj = $(PERL) -e 'sub crc32 { my ($$s) = @_; my $$crc = 0xffffffff; for my $$byte (unpack("C*", $$s)) { $$crc ^= $$byte; for (1 .. 8) { $$crc = ($$crc & 1) ? (($$crc >> 1) ^ 0xedb88320) : ($$crc >> 1); } } return ($$crc ^ 0xffffffff) & 0xffffffff; } sub header { my ($$fh, $$body) = @_; print $$fh pack("v", 0xea60), pack("v", length($$body)), $$body, pack("V", crc32($$body)); } sub first_header { my ($$method, $$type, $$comp, $$orig, $$crc, $$mode) = @_; my $$rest = pack("C*", 11, 1, 2, 0, $$method, $$type, 0, 0) . pack("V", 0) . pack("V", $$comp) . pack("V", $$orig) . pack("V", $$crc) . pack("v", 0) . pack("v", $$mode); return pack("C", length($$rest) + 1) . $$rest; } my $$out = shift @ARGV; open my $$fh, ">:raw", $$out or die "$$out: $$!"; header($$fh, first_header(0, 2, 0, 0, 0, 0) . "$$out\0\0"); while (@ARGV) { my ($$mode, $$name, $$data) = splice(@ARGV, 0, 3); $$data =~ s/\\n/\n/g; my $$type = (oct($$mode) & 0170000) == 0040000 ? 3 : 0; header($$fh, first_header(0, $$type, length($$data), length($$data), crc32($$data), oct($$mode)) . "$$name\0\0"); print $$fh $$data; } print $$fh pack("v", 0xea60), pack("v", 0);'

.PHONY: all clean
all:

clean:
	rm -rf $(OUTDIR)/*.arj tmp* moo* zoo* cur* par*

ifeq "$(shell command -v $(PERL);)" ""
$(error perl(1) is needed to create ARJ samples)
endif

$(OUTDIR):
	mkdir -p $(@)

all: $(OUTDIR)/absolute1.arj
$(OUTDIR)/absolute1.arj: | $(OUTDIR)
	$(arj) $(@) 0100644 /tmp/moo 'moo\n'

all: $(OUTDIR)/absolute2.arj
$(OUTDIR)/absolute2.arj: | $(OUTDIR)
	$(arj) $(@) 0100644 //tmp/moo 'moo\n'

all: $(OUTDIR)/relative0.arj
$(OUTDIR)/relative0.arj: | $(OUTDIR)
	$(arj) $(@) 0100644 ../moo 'moo\n'

all: $(OUTDIR)/relative2.arj
$(OUTDIR)/relative2.arj: | $(OUTDIR)
	$(arj) $(@) 0100644 tmp/../../moo 'moo\n'

all: $(OUTDIR)/symlink.arj
$(OUTDIR)/symlink.arj: | $(OUTDIR)
	$(arj) $(@) 0120777 moo /tmp/moo 0100644 moo 'moo\n'

all: $(OUTDIR)/dirsymlink.arj
$(OUTDIR)/dirsymlink.arj: | $(OUTDIR)
	$(arj) $(@) 0120777 tmp /tmp 0100644 tmp/moo 'moo\n'

all: $(OUTDIR)/dirsymlink2a.arj
$(OUTDIR)/dirsymlink2a.arj: | $(OUTDIR)
	$(arj) $(@) 0120777 cur . 0120777 par cur/.. 0100644 par/moo 'moo\n'

all: $(OUTDIR)/dirsymlink2b.arj
$(OUTDIR)/dirsymlink2b.arj: | $(OUTDIR)
	$(arj) $(@) 0120777 cur . 0120777 cur/par .. 0100644 par/moo 'moo\n'

.error = GNU make is required

# vim:ts=4 sts=4 sw=4 noet
