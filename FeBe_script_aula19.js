function trocaCor() {
    const cores = ["blue", "steelblue", "lightblue"];
    document.querySelectorAll(".divTrocaCor").forEach((div, i) => div.style.backgroundColor = cores[i]);
}
function resetarCor() {
    document.querySelectorAll(".divTrocaCor").forEach(div => div.style.backgroundColor = "");
}
function calcularOperacao() {
    const a = document.getElementById("num1").value;
    const b = document.getElementById("num2").value;
    const op = document.getElementById("operador").value;
    const saida = document.getElementById("resultado");
    if (a.trim() === "" || b.trim() === "") { saida.textContent = "Preencha os dois números."; return; }
    const n1 = Number(a), n2 = Number(b);
    if (!Number.isFinite(n1) || !Number.isFinite(n2)) { saida.textContent = "Informe números válidos."; return; }
    let r;
    switch (op) {
        case "+": r = n1 + n2; break;
        case "-": r = n1 - n2; break;
        case "*": r = n1 * n2; break;
        case "/": if (n2 === 0) { saida.textContent = "Divisão por zero não é permitida."; return; } r = n1 / n2; break;
        default: saida.textContent = "Operação inválida."; return;
    }
    saida.textContent = "Resultado: " + r;
}