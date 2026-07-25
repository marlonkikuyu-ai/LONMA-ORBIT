from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.db import engine, Base
from modules.auth.router import router as auth_router
from modules.user.router import router as user_router
from modules.supermarket.router import router as supermarket_router
from modules.product.router import router as product_router
from modules.order.router import router as order_router
from modules.payment.router import router as payment_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="SupaShop SaaS API")

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

app.include_router(auth_router, prefix="/api/auth", tags=["Auth"])
app.include_router(user_router, prefix="/api/user", tags=["User"])
app.include_router(supermarket_router, prefix="/api/supermarket", tags=["Supermarket"])
app.include_router(product_router, prefix="/api/product", tags=["Product"])
app.include_router(order_router, prefix="/api/order", tags=["Order"])
app.include_router(payment_router, prefix="/api/payment", tags=["Payment"])

@app.get("/")
def root(): return {"message": "SupaShop Backend Running"}
