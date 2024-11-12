from fastapi import APIRouter, FastAPI, File, Response, UploadFile

from Services.image_bucket import ImageBucket

class Route :
 def __init__(self, app : FastAPI):
  self.router = APIRouter()
  self.image_bucket = ImageBucket()

  @self.router.post("/upload")
  async def upload_image(image: UploadFile = File(...)):
   return self.image_bucket.add_image(image.filename, image.file.read())

  @self.router.get("/get/{url}" )
  async def get_image(url:str):
   url = url.replace("%2f", "/")
   return Response(content=self.image_bucket.get_image(url), media_type="image/jpeg")
  
  @self.router.delete("/delete/{url}")
  async def delete_image(url: str):

   return Response(status_code=200) 
  
  app.include_router( prefix="/images", router=self.router)
 
