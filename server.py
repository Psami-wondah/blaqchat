import uvicorn

if __name__ == "__main__":
    uvicorn.run("blaqchat.asgi:application", reload=True)
