# db_config.py
import pyodbc

conn = pyodbc.connect(
    'DRIVER={SQL Server Native Client 11.0};SERVER=localhost;DATABASE=Anyel;UID=sa;PWD=contra'
)
