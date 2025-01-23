from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from controllers import math_controller

app = FastAPI()

app.include_router(math_controller.router)

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

