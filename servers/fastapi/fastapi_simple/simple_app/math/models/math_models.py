from pydantic import BaseModel

class AddRequest(BaseModel):
	x: float
	y: float

class AddResponse(BaseModel):
	total: float