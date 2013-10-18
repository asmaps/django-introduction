STATICDIR = static
PORT = 8080

.PHONY: help clean static serve

help:
	@echo "Please use 'make <target>' where <target> is one of"
	@echo "  clean    delete static files"
	@echo "  static   create static files"
	@echo "  serve    serve static files"

clean:
	rm -rf $(STATICDIR)

static: clean
	mkdir -p $(STATICDIR)/reveal.js
	cp -R css img js index*.html AUTHORS LICENSE README.rst static
	cp _htaccess static/.htaccess
	find ./reveal.js/* -maxdepth 1 ! -name ".*" -exec cp -R {} $(STATICDIR)/reveal.js \;
	cd $(STATICDIR); ln -s reveal.js/plugin .
	@echo
	@echo "Created static files in directory '$(STATICDIR)'."

serve: static
	cd $(STATICDIR); python -m webbrowser -n http://127.0.0.1:$(PORT)/index.html; python -m SimpleHTTPServer $(PORT)
