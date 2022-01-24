import 'package:entryqr/provider/como_gasto_localizations.dart';
import 'package:entryqr/provider/provider.dart';
import 'package:flutter/material.dart';

AppBar MainAppBar() {
  return AppBar(
    backgroundColor: Color(0xff009688),
    title: Row(
      mainAxisAlignment: MainAxisAlignment.start,
      children: [
        Image.asset('app_files/appBar_icon.png'),
        Text("Rastreador",
          style: TextStyle(fontSize: 23.0,
              fontWeight: FontWeight.bold,
              color: Colors.white),),
      ],
    ),
  );
}

Widget SubLabel(String label) {
  return Container(
    alignment: Alignment.center,
    padding: EdgeInsets.fromLTRB(20.0, 20.0, 20.0, 0.0),
    child: Text(label,
      style: TextStyle(
          fontSize: 20.0, fontWeight: FontWeight.bold, color: Colors.black),),
  );
}

Widget ExplanationLabel(String label) {
  return Container(
    alignment: Alignment.centerLeft,
    padding: EdgeInsets.fromLTRB(20.0, 17.5, 20.0, 0.0),
    child: Text(label,
      style: TextStyle(fontSize: 17.0, color: Colors.black),),
  );
}

Widget TextEntry(String label) {
  return Container(
    alignment: Alignment.centerLeft,
    padding: EdgeInsets.fromLTRB(20.0, 10.0, 20.0, 0.0),
    child: TextField(
      decoration: InputDecoration(
        hintText: label,
        fillColor: Colors.white,
        filled: true,
      ),
    ),
  );
}

void requestFocus(BuildContext context, FocusNode focusNode){
  FocusScope.of(context).requestFocus(focusNode);
}

void infoDialog(BuildContext context, MyProvider provider, String title, String body, String button) {
    showDialog(
        barrierDismissible: false,
        context: context,
        builder: (_) =>
            AlertDialog(
              title: Text(title),
              content: Text(body),
              backgroundColor: Colors.white,
              actions: [
                TextButton(
                  child: Text(button,
                    style: TextStyle(color: Color(0xff009688), fontSize: 16.5),),
                  onPressed: () {
                    Navigator.pop(context);
                  },
                ),
              ],
            )
    );
}

void errorDialog(BuildContext context, MyProvider provider, String title, String body, String button) {

    showDialog(
        barrierDismissible: false,
        context: context,
        builder: (_) =>
            AlertDialog(
              title: Text(title),
              content: Text(body),
              backgroundColor: Colors.white,
              actions: [
                TextButton(
                  child: Text(button,
                    style: TextStyle(color: Color(0xff009688), fontSize: 16.5),),
                  onPressed: () {

                    Navigator.pop(context);
                  },
                ),
              ],
            )
    );
}

void signalControl(BuildContext context, MyProvider provider, int signal) {
  /* SIGNALS:
  * 0: OK
  * 1: SOME EMPTY
  * 2: PERSON DOES NOT EXIST
  * 3: BAD DATE FORMAT
  * 4: BAD TEMPERATURE FORMAT
  * 5: INITIAL DATE AFTER FINAL DATE
  */

  ComoGastoLocalizations? localizations = Localizations.of<
      ComoGastoLocalizations>(context, ComoGastoLocalizations);

  switch (signal) {
    case 0:
      break;
    case 1:
      infoDialog(
          context, provider, localizations!.t('infodialogos.vaciotitulo'),
          localizations.t('infodialogos.vacio'),
          localizations.t('infodialogos.boton'));
      break;
    case 2:
      infoDialog(
          context, provider, localizations!.t('infodialogos.personatitulo'),
          localizations.t('infodialogos.persona'),
          localizations.t('infodialogos.boton'));
      break;
    case 3:
      infoDialog(context, provider,
          localizations!.t('infodialogos.formatofechatitulo'),
          localizations.t('infodialogos.formatofecha') + "\n\n" +
              localizations.t('infodialogos.formatofechaejemplo'),
          localizations.t('infodialogos.boton'));
      break;
    case 4:
      infoDialog(
          context, provider, localizations!.t('infodialogos.temperaturatitulo'),
          localizations.t('infodialogos.temperatura'),
          localizations.t('infodialogos.boton'));
      break;
    case 5:
      infoDialog(
          context, provider, localizations!.t('infodialogos.ordenfechatitulo'),
          localizations.t('infodialogos.ordenfecha'),
          localizations.t('infodialogos.boton'));
      break;
  }
}

bool checkUserName(MyProvider provider, String name, String surname) {
  for (int i = 0; i < provider.usersTotal.length; i++) {
    if (provider.usersTotal[i]['name'] == name &&
        provider.usersTotal[i]['surname'] == surname) {
      provider.uuid = provider.usersTotal[i]['uuid'];
      return true;
    }
  }
  return false;
}

bool checkUserUUID(MyProvider provider, String uuid,  String name, String surname) {
  for (int i = 0; i < provider.usersTotal.length; i++) {
    if (provider.usersTotal[i]['uuid'] == uuid &&
        provider.usersTotal[i]['name'] == name &&
        provider.usersTotal[i]['surname'] == surname) {
      return true;
    }
  }
  return false;
}


bool checkDate(String date, String language) {
  //Returns true if date format is ok,
  //false if date format is wrong.

  String dateformat = "";
  if (language == "es"){
    dateformat = "diamesaño";
  } else if (language == "en"){
    dateformat = "mesdiaaño";
  }

  switch (dateformat){
    case "diamesaño":
      if (date.length != 16) return false;
      if (int.parse(date.substring(0, 2)) < 1 || int.parse(date.substring(0, 2)) > 31) return false;
      if (date.substring(2, 3) != "/") return false;
      if (int.parse(date.substring(3, 5)) < 1 || int.parse(date.substring(3, 5)) > 12) return false;
      if (date.substring(5, 6) != "/") return false;
      if (isNumericInt(date.substring(6, 10)) == false) return false;
      if (date.substring(10, 11) != " ") return false;
      if (int.parse(date.substring(11, 13)) < 0 || int.parse(date.substring(11, 13)) > 23) return false;
      if (date.substring(13, 14) != ":") return false;
      if (int.parse(date.substring(14)) < 0 || int.parse(date.substring(14)) > 59) return false;
      break;

    case "mesdiaaño":
      if (date.length != 16) return false;
      if (int.parse(date.substring(0, 2)) < 1 || int.parse(date.substring(0, 2)) > 12) return false;
      if (date.substring(2, 3) != "/") return false;
      if (int.parse(date.substring(3, 5)) < 1 || int.parse(date.substring(3, 5)) > 31) return false;
      if (date.substring(5, 6) != "/") return false;
      if (isNumericInt(date.substring(6, 10)) == false) return false;
      if (date.substring(10, 11) != " ") return false;
      if (int.parse(date.substring(11, 13)) < 0 || int.parse(date.substring(11, 13)) > 23) return false;
      if (date.substring(13, 14) != ":") return false;
      if (int.parse(date.substring(14)) < 0 || int.parse(date.substring(14)) > 59) return false;
      break;
  }


  return true;
}

bool checkTemperature(String t, String language) {
  //Returns true if temperature format is ok,
  //false if temperature format is wrong.

  String temperatura = "";
  if (language == "es"){
    temperatura = "celsius";
  } else if (language == "en"){
    temperatura = "fahrenheit";
  }

  if (isNumericDouble(t) == false) return false;

  switch (temperatura){
    case "celsius":
      if (double.parse(t) < 30 || double.parse(t) > 45) return false;
      break;

    case "fahrenheit":
      if (double.parse(t) < 86 || double.parse(t) > 113) return false;
      break;

    case "kelvin":
      if (double.parse(t) < 303.15 || double.parse(t) > 318.15) return false;
      break;
  }



  return true;
}

bool isNumericInt(String s) {
  return int.tryParse(s) != null;
}

bool isNumericDouble(String s) {
  return double.tryParse(s) != null;
}

String fechaActual(DateTime time, String language) {

  String formatofecha = "";

  if (language == "es") {
    formatofecha = "diamesaño";
  } else if (language == "en") {
    formatofecha = "mesdiaaño";
  }

  String date = "";

  switch (formatofecha){
    case "diamesaño":
      date = time.day.toString().padLeft(2, '0') + "/" +
          time.month.toString().padLeft(2, '0') + "/" +
          time.year.toString() + " " + time.hour.toString().padLeft(2, '0') +
          ":" +
          time.minute.toString().padLeft(2, '0');
      break;

    case "mesdiaaño":
      date = time.month.toString().padLeft(2, '0') + "/" +
          time.day.toString().padLeft(2, '0') + "/" +
          time.year.toString() + " " + time.hour.toString().padLeft(2, '0') +
          ":" +
          time.minute.toString().padLeft(2, '0');
      break;
  }

  return date;

}


String formatoFechaApp(String fechaOriginal, String language){

  String date = "";
  if (language == "es"){
    date = "diamesaño";
  } else if(language == "en"){
    date = "mesdiaaño";
  }

  String auxFecha = "";

  switch (date){
    case "diamesaño":
      auxFecha += fechaOriginal.substring(8, 10);
      auxFecha += "/";
      auxFecha += fechaOriginal.substring(5, 7);
      auxFecha += "/";
      auxFecha += fechaOriginal.substring(0, 4);
      auxFecha += " ";
      auxFecha += fechaOriginal.substring(11, 16);
      break;

    case "mesdiaaño":
      auxFecha += fechaOriginal.substring(5, 7);
      auxFecha += "/";
      auxFecha += fechaOriginal.substring(8, 10);
      auxFecha += "/";
      auxFecha += fechaOriginal.substring(0, 4);
      auxFecha += " ";
      auxFecha += fechaOriginal.substring(11, 16);
      break;
  }



  return auxFecha;

}

String formatoFechaBaseDatos(String fechaModificada, String language) {

  String date = "";
  if (language == "es"){
    date = "diamesaño";
  } else if (language == "en"){
    date = "mesdiaaño";
  }

  String auxFecha = "";

  switch (date){
    case "diamesaño":
      auxFecha += fechaModificada.substring(6, 10);
      auxFecha += "-";
      auxFecha += fechaModificada.substring(3, 5);
      auxFecha += "-";
      auxFecha += fechaModificada.substring(0, 2);
      auxFecha += "T";
      auxFecha += fechaModificada.substring(11, 16);
      auxFecha += ":00.000+0000";
      break;

    case "mesdiaaño":
      auxFecha += fechaModificada.substring(6, 10);
      auxFecha += "-";
      auxFecha += fechaModificada.substring(0, 2);
      auxFecha += "-";
      auxFecha += fechaModificada.substring(3, 5);
      auxFecha += "T";
      auxFecha += fechaModificada.substring(11, 16);
      auxFecha += ":00.000+0000";
      break;
  }


  return auxFecha;

}

String formatoTemperaturaBaseDatos(String temperatura, String language){

  String formatoTemperatura = "";
  if (language == "es"){
    formatoTemperatura = "centigrados";
  } else if (language == "en"){
    formatoTemperatura = "fahrenheit";
  }

  double temperaturaBD = double.parse(temperatura);

  switch (formatoTemperatura){
    case "centigrados":
      break;
    case "fahrenheit":
      temperaturaBD = (temperaturaBD - 32) * 5/9;
      break;
    case "kelvin":
      temperaturaBD = temperaturaBD - 273.15;
  }

  return temperaturaBD.toString();
}

String formatoTemperaturaApp(String temperatura, String language){

  String formatoTemperatura = "";
  if (language == "es"){
    formatoTemperatura = "centigrados";
  } else if (language == "en"){
    formatoTemperatura = "fahrenheit";
  }

  double temperaturaBD = double.parse(temperatura);

  switch (formatoTemperatura){
    case "centigrados":
      break;
    case "fahrenheit":
      temperaturaBD = (temperaturaBD * 9/5) + 32;
      break;
    case "kelvin":
      temperaturaBD = temperaturaBD + 273.15;
  }

  return temperaturaBD.toString();
}


