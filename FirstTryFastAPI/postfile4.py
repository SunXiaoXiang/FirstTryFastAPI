from fastapi import FastAPI, File, Form, UploadFile
app = FastAPI()

@app.post("/files/")
async def create_file(
    file: UploadFile = File(), token: str = Form()
):
    return {
        "token": token,
        "file_name": file.filename,
    }
