AR = ar
OUTDIR = ../.files

.PHONY: all clean FORCE
all:

clean:
	rm -rf $(OUTDIR)/*.a tmp* moo*

ifeq "$(shell command -v $(AR);)" ""
$(error ar(1) is needed to create ar samples)
endif

$(OUTDIR):
	mkdir -p $(@)

all: $(OUTDIR)/absolute1.a
$(OUTDIR)/absolute1.a: FORCE | $(OUTDIR)
	echo moo > mooooooo
	$(AR) rcS moo.a mooooooo
	rm mooooooo
	perl -pi -e s,mooooooo,/tmp/moo, moo.a
	mv moo.a $(@)

all: $(OUTDIR)/absolute2.a
$(OUTDIR)/absolute2.a: FORCE | $(OUTDIR)
	echo moo > moooooooo
	$(AR) rcS moo.a moooooooo
	rm moooooooo
	perl -pi -e s,moooooooo,//tmp/moo, moo.a
	mv moo.a $(@)

all: $(OUTDIR)/relative0.a
$(OUTDIR)/relative0.a: FORCE | $(OUTDIR)
	echo moo > mooooo
	$(AR) rcS moo.a mooooo
	rm mooooo
	perl -pi -e s,mooooo,../moo, moo.a
	mv moo.a $(@)

all: $(OUTDIR)/relative2.a
$(OUTDIR)/relative2.a: FORCE | $(OUTDIR)
	echo moo > moooooooooooo
	$(AR) rcS moo.a moooooooooooo
	rm moooooooooooo
	perl -pi -e s,moooooooooooo,tmp/../../moo, moo.a
	mv moo.a $(@)

.error = GNU make is required

# vim:ts=4 sts=4 sw=4 noet
