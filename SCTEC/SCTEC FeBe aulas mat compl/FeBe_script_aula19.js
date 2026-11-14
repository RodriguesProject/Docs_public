function trocaCor() 
{
    const div1 = document.getElementById("div-1");
    const div2 = document.getElementById("div-2");
    const div3 = document.getElementById("div-3");
    div1.style.backgroundColor = "blue";
    div2.style.backgroundColor = "steelblue";
    div3.style.backgroundColor = "lightblue";
}
function resetarCor()
{
    const div1 = document.getElementById("div-1");
    const div2 = document.getElementById("div-2");
    const div3 = document.getElementById("div-3");
    div1.style.backgroundColor = "white";
    div2.style.backgroundColor = "white";
    div3.style.backgroundColor = "white";
}
function calcularOperacao()
{
    let num1 = parseFloat(document.getElementById("num1").value);
    let num2 = parseFloat(document.getElementById("num2").value);
    let operador = document.getElementById("operador").value;
    let resultado;

    switch(operador)
    {
        case "+":
            resultado = num1 + num2;
            break;
        case "-":
            resultado = num1 - num2;
            break;
        case "*":
            resultado = num1 * num2;
            break;
        case "/":
            if(num2 !== 0)
                {
                resultado = num1 / num2;
                }
            else
                {
                resultado = "Erro: Divisão por zero não é permitida.";
                }
                break;
            default:
                resultado = "Operação inválida.";
    }
    document.getElementById("resultado").innerHTML = "Resultado: " + resultado;
}
