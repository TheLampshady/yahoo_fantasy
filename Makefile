api:
	cd api && pip install -t libs -r requirements.txt

local:
	ngrok http 8080

