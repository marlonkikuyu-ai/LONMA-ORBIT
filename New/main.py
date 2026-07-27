from modules.user.router import router as user_router
app.include_router(user_router, prefix="/api/user", tags=["User"])
