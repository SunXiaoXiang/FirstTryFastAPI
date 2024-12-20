from fastapi import FastAPI, UploadFile
app = FastAPI()

@app.post("/uploadfiles/")
async def create_upload_files(files: list[UploadFile]):
    return {"filenames": [file.filename for file in files]}
