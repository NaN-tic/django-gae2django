default:
	@echo "Run 'make all' to fetch required sources to run this example."

all: templates static codereview feeds login views
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
	hg clone https://bitbucket.org/nantic/rietveld rietveld.hg

codereview: rietveld.hg
	ln -s rietveld.hg/codereview .
	patch -p1 < patches/download.link.diff

static: upload.py
	ln -s rietveld.hg/static .
	@if [ -f django-120x30.gif ]; then mv django-120x30.gif static; fi;
	@if [ -f python-120x30.gif ]; then mv python-120x30.gif static; fi;
	patch -p1 < patches/template_base.diff

templates: rietveld.hg
	ln -s rietveld.hg/templates .
	patch -p1 < patches/account-login-links.diff

upload.py: templates
	ln -s rietveld.hg/upload.py .
	patch -p0 < patches/upload.diff
	patch -p1 < patches/upload_html.diff

feeds: codereview templates
	patch -p1 < patches/feeds.diff

login: codereview
	patch -p1 < patches/login_required.diff

views: codereview
	patch -p1 < patches/views.diff
