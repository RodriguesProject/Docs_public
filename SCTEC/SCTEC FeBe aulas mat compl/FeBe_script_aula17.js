function verificaAprovacao() {
    const campoNota = document.getElementById("nota");
    const resultado = document.getElementById("resultado");
    const nota = Number(campoNota.value);
    if (campoNota.value.trim() === "" || !Number.isFinite(nota) || nota < 0 || nota > 10) {
        resultado.textContent = "Informe uma nota válida entre 0 e 10.";
        return;
    }
    resultado.textContent = nota >= 7 ? "Parabéns! Você foi aprovado." : "Você não atingiu a nota mínima.";
}