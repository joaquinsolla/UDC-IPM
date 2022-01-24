function generateTable(){
    let center = JSON.parse(localStorage.getItem("center"));
    let type = JSON.parse(localStorage.getItem("type"));
    let timestamp = JSON.parse(localStorage.getItem("timestamp"));
    let temperature = JSON.parse(localStorage.getItem("temperature"));

    // NUMBER OF ACCESSES
    let tablesize = document.getElementById("cellsN").value;

    // TABLE HEADERS
    let tableheaders = "            <tr>\n" +
        "              <th style=\"width:50%\">Centro</th>\n" +
        "              <th style=\"width:10%\">Tipo</th>\n" +
        "              <th style=\"width:25%\">Fecha</th>\n" +
        "              <th style=\"width:15%\">Temperatura</th>\n" +
        "            </tr>";

    let toinsert = "";
    for (let i = 0; i < tablesize; i++) {
        toinsert += "<tr>\n" +
        "              <td id=\"centro"+i+"\">" + center[i] +"</td>\n" +
        "              <td id=\"tipo"+i+"\">"+ type[i] + "</td>\n" +
        "              <td id=\"fecha"+i+"\">"+ timestamp[i].slice(0, 10) + "  " + timestamp[i].slice(11, 19) + "</td>\n" +
        "              <td id=\"temp"+i+"\">"+ temperature[i] +"</td>\n" +
        "            </tr>";

    }
    document.getElementById("mytable").innerHTML = tableheaders + toinsert;
}

function access() {

    let tablesize = document.getElementById("cellsN").value;

    if (tablesize > 0){
        fetch("http://localhost:8080/api/rest/user_access_log/" + localStorage.getItem('uuid') + "?limit=" + parseInt(tablesize), {
            headers: {"x-hasura-admin-secret":"myadminsecretkey"},
            method: 'GET'
        })
            .then(response=> {
                return response.json();
            })
            .catch(() => {
                alert("Ocurrió un error con la BD. Vuelve a intentarlo más tarde");
            })
            .then(data => accesslog(data));
    } else{
        alert("El valor de accesos a mostrar debe ser > 0");

    }


}

function accesslog(data) {

    let tablesize = document.getElementById("cellsN").value;
    let center = [];
    let type = [];
    let timestamp = [];
    let temperature = [];

    if(tablesize > 0) {

        for (let i = 0; i < parseInt(tablesize); i++) {
            center.push(data['access_log'][i]['facility'].name);
            type.push(data['access_log'][i].type);
            timestamp.push(data['access_log'][i].timestamp);
            temperature.push(data['access_log'][i].temperature);
        }
        localStorage.setItem("center", JSON.stringify(center));
        localStorage.setItem("type" , JSON.stringify(type));
        localStorage.setItem("timestamp" , JSON.stringify(timestamp));
        localStorage.setItem("temperature" , JSON.stringify(temperature));

        generateTable();
    }
}