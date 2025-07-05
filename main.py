import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from random import randint, uniform
from dotenv import load_dotenv
import os
from mysql.connector import pooling
from fastapi.responses import JSONResponse

logger = logging.getLogger('uvicorn.error')
logger.setLevel(logging.DEBUG)

# Load environment variables from .env
load_dotenv()

# Fetch variables
USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
PORT = os.getenv("port")
DBNAME = os.getenv("dbname")

app = FastAPI()

# Allow CORS for your frontend (adjust origins as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Change port if your frontend runs elsewhere
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize MySQL connection pool at startup
db_pool = pooling.MySQLConnectionPool(
    pool_name="mypool",
    pool_size=10,
    user=USER,
    password=PASSWORD,
    host=HOST,
    port=PORT,
    database=DBNAME,
    charset='utf8mb4',
    autocommit=True
)

@app.get("/api/stats")
def get_stats():
    # REGIONS removed, so return an empty list or static data
    return []

@app.get("/api/test-db")
def test_db():
    connection = db_pool.get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM medecins_par_departement;")
        columns = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        result = [dict(zip(columns, row)) for row in rows]
        cursor.close()
        return JSONResponse(content=result)
    finally:
        connection.close()

@app.get("/api/passages")
def get_passages():
    connection = db_pool.get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM moyenne_passages_par_dep;")
        columns = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        result = [dict(zip(columns, row)) for row in rows]
        cursor.close()
        return JSONResponse(content=result)
    finally:
        connection.close()

@app.get("/api/medecins_dep")
def get_nb_medecins_par_dep():
    connection = db_pool.get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT id, departement, effectif FROM medecins_par_departement;")
        columns = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        result = [dict(zip(columns, row)) for row in rows]
        cursor.close()
        return JSONResponse(content=result)
    finally:
        connection.close()

@app.get("/api/part-medecins-sup-55")
def get_part_medecins_sup_55():
    connection = db_pool.get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM part_medecins_sup_55;")
        columns = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        result = [dict(zip(columns, row)) for row in rows]
        cursor.close()
        return JSONResponse(content=result)
    finally:
        connection.close()

@app.get("/api/medecins-retraites-actifs")
def get_medecins_retraites_actifs():
    connection = db_pool.get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM medecins_retraites_actifs;")
        columns = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        result = [dict(zip(columns, row)) for row in rows]
        cursor.close()
        return JSONResponse(content=result)
    finally:
        connection.close()

@app.get("/api/apl-dep")
def get_apl_dep():
    connection = db_pool.get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM apl_dep;")
        columns = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        result = [dict(zip(columns, row)) for row in rows]
        cursor.close()
        return JSONResponse(content=result)
    finally:
        connection.close()


