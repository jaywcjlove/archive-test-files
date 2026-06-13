PERL = perl
OUTDIR = ../.files
zoo = $(PERL) -e 'sub crc { my ($$s) = @_; my $$crc = 0; for my $$byte (unpack("C*", $$s)) { $$crc ^= $$byte; for (1 .. 8) { $$crc = ($$crc & 1) ? (($$crc >> 1) ^ 0xa001) : ($$crc >> 1); } } return $$crc & 0xffff; } sub dosname { my ($$name) = @_; $$name = uc $$name; $$name =~ s/[^A-Z0-9.]/_/g; $$name = substr($$name, 0, 12); return $$name . ("\0" x (13 - length($$name))); } sub splitpath { my ($$path) = @_; $$path =~ s{/+\z}{} unless $$path eq "/"; return $$path =~ m{^(.*)/(.*)\z} ? ($$1, $$2) : ("", $$path); } sub entry { my ($$path, $$data) = @_; my ($$dir, $$base) = splitpath($$path); my $$nam = "$$base\0"; my $$dirname = length($$dir) ? "$$dir\0" : ""; my $$var_len = length($$nam) + length($$dirname) + 10; my $$dir_len = 56 + $$var_len; my $$offset = 42 + $$dir_len + 5; my $$next = $$offset + length($$data); my $$fixed = pack("VCCVVvvvVVCCCCVV", 0xfdc4a7dc, 2, 0, $$next, $$offset, 0, 0, crc($$data), length($$data), length($$data), 1, 0, 0, 0, 0, 0) . dosname($$base) . pack("vCv", $$var_len, 127, 0); my $$tail = pack("CC", length($$nam), length($$dirname)) . $$nam . $$dirname . pack("v", 0) . pack("CCC", 0, 0, 0) . pack("Cv", 0xc0, 1); my $$entry = $$fixed . $$tail; substr($$entry, 54, 2) = pack("v", 0); substr($$entry, 54, 2) = pack("v", crc($$entry)); return ($$entry, $$offset); } my ($$out, $$path, $$data) = @ARGV; $$data =~ s/\\n/\n/g; my ($$entry, $$offset) = entry($$path, $$data); open my $$fh, ">:raw", $$out or die "$$out: $$!"; print $$fh "ZOO 2.10 Archive.\032\0\0", pack("VVVCCCVvC", 0xfdc4a7dc, 42, 0xffffffff - 41, 2, 0, 1, 0, 0, 0), $$entry, "@)\#(\0", $$data, ("\0" x 56);'

.PHONY: all clean FORCE
all:

clean:
	rm -rf $(OUTDIR)/*.zoo tmp* moo*

ifeq "$(shell command -v $(PERL);)" ""
$(error perl(1) is needed to create zoo samples)
endif

$(OUTDIR):
	mkdir -p $(@)

all: $(OUTDIR)/absolute1.zoo
$(OUTDIR)/absolute1.zoo: FORCE | $(OUTDIR)
	$(zoo) $(@) /tmp/moo 'moo\n'

all: $(OUTDIR)/absolute2.zoo
$(OUTDIR)/absolute2.zoo: FORCE | $(OUTDIR)
	$(zoo) $(@) //tmp/moo 'moo\n'

all: $(OUTDIR)/relative0.zoo
$(OUTDIR)/relative0.zoo: FORCE | $(OUTDIR)
	$(zoo) $(@) ../moo 'moo\n'

all: $(OUTDIR)/relative2.zoo
$(OUTDIR)/relative2.zoo: FORCE | $(OUTDIR)
	$(zoo) $(@) tmp/../../moo 'moo\n'

.error = GNU make is required

# vim:ts=4 sts=4 sw=4 noet
