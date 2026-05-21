function verificaAprovacao()
{
    let nota = document.getElementById("nota").value;
    console.log("nota inserida: ", nota)
    if(nota>=7)
    {
            document.getElementById("resultado").innerHTML = "Parabéns, você foi aprovado!"
            alert("Aluno(a) aprovado(a)!");
    }
    else
    {
            document.getElementById("resultado").innerHTML = "Deu ruim, você foi reprovado!"
            alert("Aluno(a) reprovado(a)!");
    }
}









/*function varTeste1()
{
    var num1 = 1;
    var num1 = 2;

    console.log(num1);
}
varTeste1();*/