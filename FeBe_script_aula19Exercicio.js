document.addEventListener("DOMContentLoaded", () => {
    const a = document.getElementById("valorA");
    const b = document.getElementById("valorB");
    const saida = document.getElementById("saida");
    document.getElementById("somar").addEventListener("click", () => {
        if (a.value.trim() === "" || b.value.trim() === "") { saida.textContent = "Preencha os dois campos."; return; }
        const n1 = Number(a.value), n2 = Number(b.value);
        if (!Number.isFinite(n1) || !Number.isFinite(n2)) { saida.textContent = "Digite números válidos."; return; }
        saida.textContent = "Soma: " + (n1 + n2);
    });
});