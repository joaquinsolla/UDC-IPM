function login(username, password){

    if (login.value === "" || password.value === ""){
        alert("Debe introducir un usuario y una contraseña.");
    }
    else {
        fetch("http://localhost:8080/api/rest/login?username=" + username.value + "&password=" + password.value, {
            method: 'POST',
            headers: {"x-hasura-admin-secret":"myadminsecretkey"}
        })
            .then((response) => {
                return response.json();
            })
            .catch(() => {
                alert("Ocurrió un error con la BD. Vuelve a intentarlo más tarde");
            })
            .then(data => mostrarData(data));
    }
}

function mostrarData(data){

    if(data['users'].length === 0){
        alert("La contraseña no es correcta")
    }
    else {
        localStorage.setItem("uuid", data['users'][0]['uuid']);
        localStorage.setItem("names", data['users'][0]['name']);
        localStorage.setItem("email", data['users'][0]['email']);
        localStorage.setItem("surname", data['users'][0]['surname']);
        localStorage.setItem("phone", data['users'][0]['phone']);
        localStorage.setItem("vaccinated", data['users'][0]['is_vaccinated']);
        window.location.href = "userdata.html";
    }

}