# app/db_setup.py

import asyncio
from models.user import Base
from models.kyc import Base
from core.database import engine

# Async function to create tables
async def create_tables():
    # Use async session to create tables
    async with engine.begin() as conn:
        # Create all tables in the database
        await conn.run_sync(Base.metadata.create_all)
    print("Tables created successfully.")

# Run the async function
if __name__ == "__main__":
    asyncio.run(create_tables())
