from db import engine, Base
import models  # noqa: F401 - needed so Base knows about User table

print("Dropping old table...")
Base.metadata.drop_all(bind=engine)

print("Creating new table with 'name' and 'password' columns...")
Base.metadata.create_all(bind=engine)

print("Done! Restart your server.")