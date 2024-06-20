import pymongo
import time
import os

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

# Função para medir tempo de consulta com failover
def test_failover_performance(collection, num_queries=100):
    # Simular falha no nó local (exemplo: desligar o servidor local)
    os.system("sudo systemctl stop mongod")  # Comando para parar o MongoDB local (Linux)
    time.sleep(10)  # Esperar um tempo para garantir que o nó local está desligado
    
    start_time = time.time()
    for _ in range(num_queries):
        product_id = "some_product_id"  # Substitua por IDs reais ou gere aleatoriamente
        collection.find_one({"product_id": product_id})
    end_time = time.time()
    
    # Restaurar o serviço local
    os.system("sudo systemctl start mongod")  # Comando para iniciar o MongoDB local (Linux)
    
    return (end_time - start_time) / num_queries

# Executar testes de failover
num_queries = 100
for location, collection in collections.items():
    avg_time = test_failover_performance(collection, num_queries)
    print(f"Tempo médio de consulta com failover para {location}: {avg_time:.6f} segundos")

print("Testes de failover finalizados.")