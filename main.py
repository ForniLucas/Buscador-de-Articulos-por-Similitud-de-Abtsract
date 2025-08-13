from src.data_processing import load_and_preprocess_data
from src.embedding import generate_embeddings
from src.database import insert_data_to_postgres, find_most_similar
from src.interface import create_gradio_interface

if __name__ == "__main__":
    # Load and preprocess data
    file_path = "Data/casos-test.jsonl"
    df = load_and_preprocess_data(file_path,50)
    print(f"Loaded {len(df)} rows into DataFrame.")
    print(df.head())
    
    # Generate embeddings
    df['abstract_embedding'] = df['abstract'].apply(generate_embeddings)
    
    # Insert data into PostgreSQL (run once, then comment out)
    insert_data_to_postgres(df)  # Sample with 2000 rows
    
    # Launch Gradio interface
    #demo = create_gradio_interface(find_most_similar, generate_embeddings)
    #demo.launch(share=False)