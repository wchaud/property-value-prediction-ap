import psycopg2
import time

def populate():
    for attempt in range(10):
        try:
            conn = psycopg2.connect(
                dbname="property_db",
                user="chaud",
                password="teste",
                host="db",
                port=5432
            )
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS imoveis (
                    id SERIAL PRIMARY KEY,
                    metragem FLOAT NOT NULL,
                    valor FLOAT NOT NULL,
                    dormitorios INT NOT NULL
                );
            """)
            exemplos = [
                (50, 200000, 1),
                (60, 240000, 2),
                (70, 280000, 2),
                (80, 320000, 3),
                (90, 360000, 3),
                (100, 400000, 4),
            ]
            cursor.executemany("INSERT INTO imoveis (metragem, valor, dormitorios) VALUES (%s, %s, %s);", exemplos)
            conn.commit()
            cursor.close()
            conn.close()
            print("Banco populado com sucesso!")
            break
        except Exception as e:
            print(f"Tentativa {attempt+1}/10: Erro ao criar tabela ou popular dados: {e}")
            time.sleep(5)
    else:
        print("Não foi possível conectar ao banco de dados após várias tentativas.")

if __name__ == "__main__":
    populate()