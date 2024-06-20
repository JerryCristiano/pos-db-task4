import pymongo
import time

# Configurações de conexão
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["supermarket_inventory"]

# Coleções para cada filial
collections = {
    "SP": db["products_SP"],
    "RJ": db["products_RJ"],
    "MG": db["products_MG"],
    "RS": db["products_RS"],
    "PR": db["products_PR"]
}

# Função para medir tempo de consulta
def test_query_performance(collection, num_queries=100):
    start_time = time.time()
    for _ in range(num_queries):
        product_id = "some_product_id"  # Substitua por IDs reais ou gere aleatoriamente
        collection.find_one({"product_id": product_id})
    end_time = time.time()
    return (end_time - start_time) / num_queries

# Executar testes de consulta
num_queries = 100
for location, collection in collections.items():
    avg_time = test_query_performance(collection, num_queries)
    print(f"Tempo médio de consulta para {location}: {avg_time:.6f} segundos")

print("Testes de consulta finalizados.")