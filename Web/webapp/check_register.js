function check_register(username, password, confirm_password, name, surname, phone, email, vaccinated){
    if(username.value === "" || password.value === "" || confirm_password.value === ""
        || name.value === "" || surname.value === "" || phone.value === "" || email.value === ""
        || vaccinated.value === ""){
        alert("Todos los campos deben estar cubiertos")
    } else{
        if (password.value !== confirm_password.value){
            alert("Las contraseñas no coinciden.");
        } else {
            register(username, password, name, surname, phone, email, vaccinated);
            alert("Usuario Registrado");
            login(username, password);
        }
    }
}

function jsonRegister (username, password, name, surname, phone, email,  vaccinated){
    return JSON.stringify({
        "username":username.value,
        "password":password.value,
        "name":name.value,
        "surname":surname.value,
        "phone":phone.value,
        "email":email.value,
        "is_vaccinated":vaccinated.value === "true",
    })
}

function register (username, password, name, surname, phone, email,  isVaccinated){

    let json = jsonRegister(username,password,name,surname,phone,email,isVaccinated);

    fetch("http://localhost:8080/api/rest/user", {
        headers: {"x-hasura-admin-secret":"myadminsecretkey"},
        method: 'POST',
        body: json,
        }).then(res => res.json())
        .then(res => console.log(res))
        .catch(() => {
            alert("Ocurrió un error con la BD. Vuelve a intentarlo más tarde");
        });
}