from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1 import users, auth, kyc, transaction

# Create FastAPI app
app = FastAPI()

# CORS configuration
origins = [
    "http://localhost:3000",  # Allow localhost:3000 (your frontend)
    "http://127.0.0.1:3000",  # Also allow 127.0.0.1:3000 (if needed)
]

# Add CORSMiddleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows only these origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

# Include routers
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(transaction.router, prefix="/transactions", tags=["transactions"])
# app.include_router(payments.router, prefix="/payments", tags=["payments"])
# app.include_router(currency.router, prefix="/currency", tags=["currency"])
app.include_router(kyc.router, prefix="/kyc", tags=["kyc"])

# Root endpoint
@app.get("/")
async def read_root():
    return {"message": "Welcome to the Cross-Border Finance App!"}
