from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
	return """<html>
	<head>
		<title>FastAPI Simple Sample</title>
	</head>
	<body>
		<h1>Welcome</h1>
		<div>This is a simple sample for FastAPI.</div>
	</body>
</html>
"""

@app.get("/some-json")
def json_hello_world():
	return { "msg": "Hello World" }

