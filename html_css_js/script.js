$(document).ready(function () {
    $("#btn_agregar").click(function () {
        let input = $("#txt_valor"); 
        let texto = input.val();
        if (texto == "") {
            alert("Por favor, ingresa una tarea."); return;
        }
        else {
            let lista = $("#lista_tareas");
            let nuevaTarea = $("<li></li>").text(texto);
            lista.append(nuevaTarea);
            input.val("");
        }
    });
});
/* function agregarTarea(){
            //alert("hiciste click en el boton agregar");
            let input = document.getElementById("txt_valor");
            let texto = input.value;
            if (texto == "") {
                alert("Por favor, ingresa una tarea.");
                return;
            }
            else {
                let lista = document.getElementById("lista_tareas");
                let nuevaTarea = document.createElement("li");
                nuevaTarea.textContent = texto;
                lista.appendChild(nuevaTarea);
                input.value = "";
            }
        } */