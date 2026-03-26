let index = 0;
const projetos = document.querySelectorAll(".projetos-card");

function mostrarProjeto(i) {
    projetos.forEach(p => p.classList.remove("ativo"));
    projetos[i].classList.add("ativo");
}

mostrarProjeto(index);

function proximo() {
    index = (index + 1) % projetos.length;
    mostrarProjeto(index);
}

function anterior() {
    index = (index - 1 + projetos.length) % projetos.length;
    mostrarProjeto(index);
}

function abrirModal(titulo, descricao) {
    document.getElementById("modal").style.display = "block";
    document.getElementById("modal-titulo").innerText = titulo;
    document.getElementById("modal-descricao").innerText = descricao;
}

function fecharModal() {
    document.getElementById("modal").style.display = "none";
}

window.onclick = function(event) {
    const modal = document.getElementById("modal");
    if (event.target == modal) {
        fecharModal();
    }
}