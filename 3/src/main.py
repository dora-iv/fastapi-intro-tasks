from fastapi import FastAPI, Path

app = FastAPI()

# BEGIN (write your solution here)
@app.get("/users/{user_id}")
async def get_user(user_id: int = Path(..., gt=0, description="User ID must be greater than 0")):
    if user_id <= 0:
        raise HTTPException(status_code=422, detail="user_id must be greater than 0")
    return {"user_id": user_id}
# END
