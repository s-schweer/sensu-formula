.PHONY: bundle_install tests virtualenv setup 

bundle_install:
	bundle install

virtualenv:
	virtualenv .venv
	.venv/bin/pip install -r requirements.txt

setup: bundle_install virtualenv

tests:
	. .venv/bin/activate
	bundle exec kitchen test
	deactivate


	

