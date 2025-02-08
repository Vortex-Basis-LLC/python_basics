from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from .math.controllers import math_controller


def setup_app(static_img_file_path: str) -> FastAPI:

	app = FastAPI()

	# NOTE: Swagger docs will be available at /docs url.

	# Static image files in the provided directory will be available at /img url.
	app.mount("/img", StaticFiles(directory=static_img_file_path), name="img")

	app.include_router(math_controller.router)

	@app.get("/", response_class=HTMLResponse)
	async def home():
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
	async def json_hello_world():
		return { "msg": "Hello World" }

	@app.get("/client-ip")
	async def client_ip(request: Request):
		return { "client_ip": request.client.host }
	
	return app

