
# Admin Backend
Endpoints build with Google endpoints v2 hosted in the api folder.

[Backend Readme](api/Readme.md)

## Install Dependencies
```bash
pip install -r api/requirements.txt -t api/libs
```

## Run the app locally
Google Endpoints has a web app for using your new api. This even connects to your localhost.
```bash
dev_appserver.py api/api.yaml --host localhost --port 8080
```

**Local Site:**
```
http://localhost:8080/api/fantasy/v1/get/test
```

**Local Endpoint Tool:**
```
https://apis-explorer.appspot.com/apis-explorer/?base=http://localhost:8080/api#p/
```


## Deploy the app
Now we will deploy an additional service and a config for routing. Take note of the dispatch.yaml file

Using the project id, deploy both services
Run: 
```bash
gcloud app deploy --project <my-project> api/api.yaml
```

**Endpoint:**
https://PROJECT-ID.appspot.com/<base_path>/<api_name>/<v1>/<path>

**Tool Endpoint Tool:**
```
https://apis-explorer.appspot.com/apis-explorer/?base=https://<PROJECT_ID>.googleplex.com/api#p/
```
