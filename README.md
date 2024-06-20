## Neste exemplo não está contemplado as configurações com o
## serviço mongo Atlas em cloud, somente o teste local, utilizando 
## docker

##Subir o serviço do docker

docker-compose up -d


##Conectar em cada servidor e executar o comando abaixo

docker exec -it mongo1 mongo

rs.initiate({
  _id: "rsSP",
  members: [
    { _id: 0, host: "mongo1:27017" }
  ]
})


docker exec -it mongo2 mongo

rs.initiate({
  _id: "rsRJ",
  members: [
    { _id: 0, host: "mongo2:27017" }
  ]
})


docker exec -it mongo3 mongo

rs.initiate({
  _id: "rsMG",
  members: [
    { _id: 0, host: "mongo3:27017" }
  ]
})


docker exec -it mongo4 mongo

rs.initiate({
  _id: "rsRS",
  members: [
    { _id: 0, host: "mongo4:27017" }
  ]
})


docker exec -it mongo5 mongo

rs.initiate({
  _id: "rsPR",
  members: [
    { _id: 0, host: "mongo5:27017" }
  ]
})

## Adicionar os shards e a colection

docker exec -it mongos mongo

sh.addShard("rsSP/mongo1:27017")
sh.addShard("rsRJ/mongo2:27017")
sh.addShard("rsMG/mongo3:27017")
sh.addShard("rsRS/mongo4:27017")
sh.addShard("rsPR/mongo5:27017")


sh.enableSharding("supermarket_inventory")
sh.shardCollection("supermarket_inventory.products", { "product_id": 1 })

## Executar a carga de dados.
## Necessário instalar a bibilioteca de acesso ao mongo db e 
## para gerar os dados de teste

pip install pymongo faker

python generate_test_data.py


## Verificar os dados via console do mongodb

mongo
use supermarket_inventory
db.products_SP.find().pretty()

## Executar os testes

python test_query_performance.py

python test_update_performance.py

python test_failover_performance.py
