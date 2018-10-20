install-libs:
	# pip install everything in requirements.txt to lib
	pip install -t lib -r lib_requirements.txt


deploy-app:
	#deploys to dev
	# appcfg.py --oauth2 list_versions -A nfl-database
	deployer/shell.py --build_path=./ --app=nfl-database --app_version=init \
	-v -i -d -q -c --modules app
