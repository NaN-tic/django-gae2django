default:
	@echo "Run 'make all' to fetch required sources to run this example."

all: static templates codereview
	@echo
	@echo "Remember to copy the 'gae2django' directory from the main source where you have taken this rietveld directory to here."
	@echo "Configure the database and other django things in the settings.py file."
	@echo "Run './manage.py syncdb' to config Rietveld."
	@echo "Run './manage.py runserver' to run Rietveld."

clean: clean_local clean_external

clean_external: clean_rietveld

clean_rietveld:
	@if [ -x codereview ]; then unlink codereview; fi;
	@if [ -x static ]; then unlink static; fi;
	@if [ -x templates ]; then unlink templates; fi;
	@if [ -x upload.py ]; then unlink upload.py; fi;
	@rm -rf rietveld.hg

clean_local:
	@if [ -x gae2django ]; then unlink gae2django; fi;
	@if [ -x dev.db ]; rm -f dev.db; fi;

rietveld.hg:
    hg clone -u https://bitbucket.org/nantic/rietveld rietveld.hg

codereview: rietveld.hg
	ln -s rietveld.hg/codereview .
	patch -p1 < patches/download.link.diff

static: rietveld.hg upload.py
	ln -s rietveld.hg/static .

upload.py: rietveld.hg
	ln -s rietveld.hg/upload.py .
	patch -p0 < patches/upload.diff

templates: rietveld.hg
	ln -s rietveld.hg/templates .
	patch -p1 < patches/account-login-links.diff
