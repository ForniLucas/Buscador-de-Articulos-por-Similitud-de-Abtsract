import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

def get_db_connection():
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )

def insert_data_to_postgres(df):
    conn = get_db_connection()
    try:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS papersprueba (
                id SERIAL PRIMARY KEY,
                authors TEXT,
                title TEXT,
                abstract TEXT,
                abstract_embedding VECTOR(1024)
            );
        """)
        # Insert data
        for _, row in df.iterrows():
            if row['abstract_embedding'] is not None:
                cur.execute(
                    "INSERT INTO papersprueba (authors, title, abstract, abstract_embedding) VALUES (%s, %s, %s, %s)",
                    (row['authors'], row['title'], row['abstract'], row['abstract_embedding'].tolist())
                )
        conn.commit()
        print("Todo cargado a la db")
    except Exception as e:
        print(f"Error inserting data: {e}")
    finally:
        cur.close()
        conn.close()

def find_most_similar(abstract_text, embedding_func, top_n=10):
    input_embedding = embedding_func(abstract_text)
    if input_embedding is None:
        return "Error generando los embedding"
    
    conn = get_db_connection()
    try:
        cur = conn.cursor()
        cur.execute("""
            SELECT title, authors, abstract, abstract_embedding <=> CAST(%s AS vector) AS distance
            FROM papers
            ORDER BY distance
            LIMIT %s;
        """, (input_embedding.tolist(), top_n))
        
        results = cur.fetchall()
        output = []
        for title, authors, abstract, distance in results:
            similarity = 1 - distance
            result = f"""
Similitud: {similarity:.4f}
Titulo: {title}
Autores: {authors}
Abstract: {abstract}
                    {'='*50}
                    """
            output.append(result)
        return "\n".join(output)
    except Exception as e:
        return f"Error buscando en la db: {e}"
    finally:
        cur.close()
        conn.close()