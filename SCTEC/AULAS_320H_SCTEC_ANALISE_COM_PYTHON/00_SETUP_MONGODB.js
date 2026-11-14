// BASE COMPLEMENTAR SINTÉTICA para a sequência de três aulas.
// O setup citado nos anexos não foi enviado; estes seis pedidos foram criados
// para viabilizar os exercícios. Não são a base original de pedidos da professora.
// O pedido 1001 mantém os preços do slide 5: Mouse 89.90 e Hub 159.90.
// Cole este arquivo no mongosh/Compass. O bloco impede carga sobre coleção ocupada.
// Para este material, todos os valores são BRL e os preços são históricos do pedido.
db = db.getSiblingDB("aula_loja_nosql_semana");

(function () {
  if (db.pedidos.countDocuments({}) !== 0) {
    throw new Error(
      "A coleção pedidos já contém dados. Confira o checkpoint da aula; " +
      "este setup não apaga nem recarrega uma coleção ocupada."
    );
  }

  db.pedidos.insertMany([
    {
      _id: 1001,
      cliente_id: "CLI001",
      cliente: { nome: "Ana", estado: "RJ" },
      data: ISODate("2026-11-01T12:00:00Z"),
      status: "entregue",
      moeda: "BRL",
      itens: [
        { produto_id: "P001", nome: "Mouse", quantidade: 2, preco: NumberDecimal("89.90") },
        { produto_id: "P005", nome: "Hub", quantidade: 1, preco: NumberDecimal("159.90") }
      ]
    },
    {
      _id: 1002,
      cliente_id: "CLI002",
      cliente: { nome: "Bruno", estado: "SP" },
      data: ISODate("2026-11-02T12:00:00Z"),
      status: "pendente",
      moeda: "BRL",
      itens: [
        { produto_id: "P002", nome: "Teclado", quantidade: 1, preco: NumberDecimal("249.90") },
        { produto_id: "P003", nome: "Monitor", quantidade: 1, preco: NumberDecimal("899.90") }
      ]
    },
    {
      _id: 1003,
      cliente_id: "CLI003",
      cliente: { nome: "Carla", estado: "RJ" },
      data: ISODate("2026-11-03T12:00:00Z"),
      status: "pendente",
      moeda: "BRL",
      itens: [
        { produto_id: "P001", nome: "Mouse", quantidade: 1, preco: NumberDecimal("89.90") },
        { produto_id: "P004", nome: "Webcam", quantidade: 2, preco: NumberDecimal("199.90") }
      ]
    },
    {
      _id: 1004,
      cliente_id: "CLI004",
      cliente: { nome: "Diego", estado: "MG" },
      data: ISODate("2026-11-04T12:00:00Z"),
      status: "entregue",
      moeda: "BRL",
      itens: [
        { produto_id: "P003", nome: "Monitor", quantidade: 1, preco: NumberDecimal("899.90") }
      ]
    },
    {
      _id: 1005,
      cliente_id: "CLI005",
      cliente: { nome: "Elisa", estado: "SP" },
      data: ISODate("2026-11-05T12:00:00Z"),
      status: "cancelado",
      moeda: "BRL",
      itens: [
        { produto_id: "P005", nome: "Hub", quantidade: 2, preco: NumberDecimal("159.90") }
      ]
    },
    {
      _id: 1006,
      cliente_id: "CLI006",
      cliente: { nome: "Fernanda", estado: "RJ" },
      data: ISODate("2026-11-06T12:00:00Z"),
      status: "entregue",
      moeda: "BRL",
      itens: [
        { produto_id: "P002", nome: "Teclado", quantidade: 2, preco: NumberDecimal("249.90") },
        { produto_id: "P004", nome: "Webcam", quantidade: 1, preco: NumberDecimal("199.90") }
      ]
    }
  ]);

  print("Carga concluída. Esperado: 6 pedidos; 3 entregues; 2 pendentes; 1 cancelado.");
  printjson({ pedidos: db.pedidos.countDocuments({}) });
})();
