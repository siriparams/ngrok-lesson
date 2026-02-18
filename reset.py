from db import engine, Base
import models from models

print("Dropping old table...")
Base.metadata.drop_all(bind=engine)

print("Creating new table with 'name' and 'password' columns...")
Base.metadata.create_all(bind=engine)

print("Success! Restart your server.")