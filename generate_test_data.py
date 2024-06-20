import pymongo
from faker import Faker
import random

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

# Gerador de dados fictícios
faker = Faker()

# Função para gerar produtos
def generate_product():
    return {
        "product_id": faker.unique.ean13(),
        "name": faker.word(),
        "category": faker.word(),
        "price": round(random.uniform(1.0, 100.0), 2),
        "quantity": random.randint(1, 100),
        "description": faker.sentence()
    }

# Inserir dados de teste nas coleções
def insert_test_data(collection, num_records):
    products = [generate_product() for _ in range(num_records)]
    collection.insert_many(products)

# Número de registros a serem gerados para cada filial
num_records = 1000

for location, collection in collections.items():
    print(f"Inserindo dados para a filial {location}")
    insert_test_data(collection, num_records)

print("Dados de teste inseridos com sucesso.")
