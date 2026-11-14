[{
  : ** Examinar a estrutura de um pedido

db.pedidos.findOne({ _id: 1001 });
},
{
  : ** Listando todos os pedidos

db.pedidos.find();
},
{
  : ** Listar somente pedidos entregues

db.pedidos.find({
  status: "entregue"
});
},
{
  : ** Pedidos de clientes do Estado do RJ

db.pedidos.find({
  "cliente.estado": "RJ"
});
},
{
  : ** Pedidos que contém P001

db.pedidos.find({
  "itens.produto_id": "P001"
});
},
{
  : ** Mostrando apenas alguns campos

db.pedidos.find(
  {},
  {
    _id: 1,
    status: 1,
    "cliente.nome": 1
  }
);
},
{
  : ** Atualizando status de pedido

db.pedidos.updateOne(
  { _id: 1003 },
  { $set: { status: "entregue" }}
);

** Acrescentando campo de visão

db.pedidos.updateOne(
  { _id: 1003 },
  { $set: { revisado: true }}
);
},
{
  : ** Entendendo duas condições no mesmo item

//Quais pedidos possuem pelo menos duas unidades do produto P001

db.pedidos.find({
  "itens.produto_id": "P001",
  "itens.quantidade": { $gte: 2 }
});

//Ambas no mesmo item

db.pedidos.find({
  itens: {
    $elemMatch: {
      produto_id: "P001",
      quantidade: { $gte: 2 }
    }
  }
});
},
{
  : ** Contar pedidos por estado

db.pedidos.aggregate([
  {
    $group: {
      _id: "$cliente.estado",
      quantidade_pedidos: { $sum: 1 }
    }
  },
  {
    $sort: {
      quantidade_pedidos: -1,
      _id: 1
    }
  }
]);
},
{
  : ** Encontrar os pedidos entregues no RJ

db.pedidos.find({
  status: "entregue",
  "cliente.estado": "RJ"
});
},
{
  : // Qual é o valor dos itens dos pedidos entregues e quais produtos contribuem para esse valor

db.pedidos.aggregate([
  { $unwind: "$itens" }
]);

** Contagem de linhas

db.pedidos.aggregate([
  { $unwind: "$itens" },
  { $count: "linhas_de_itens" }
]);
}
]