import 'dart:async';
import 'dart:core';
import 'dart:io';

import 'package:entryqr/common.dart';
import 'package:flutter/material.dart';

import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:charts_flutter/flutter.dart' as charts;

import 'como_gasto_localizations.dart';
import 'provider.dart';


//String ip = "10.0.2.2";
String ip = "172.21.1.248";

class User{

  var uuid;
  var username;
  var name;
  var surname;
  var email;
  var phone;
  var isVacinnated;
  DateTime time;

  User(this.uuid, this.username, this.name, this.surname, this.email, this.phone, this.isVacinnated, this.time);

}

class Register{

  var type;
  var name;
  var surname;
  var uuid;
  var centre;
  var timestamp;
  var temperature;

  Register(this.type, this.name, this.surname, this.uuid, this.centre, this.timestamp, this.temperature);


}

class GradesData {
  final String gradeSymbol;
  final int numberOfPeople;
  final charts.Color color;


  GradesData(this.gradeSymbol, this.numberOfPeople, this.color);
}


class AttendanceSearchArguments{
  final String centro;
  final String initialDate;
  final String finalDate;

  final List centroList = [];

  AttendanceSearchArguments(this.centro, this.initialDate, this.finalDate);
}

class AttendanceUserArguments {

  var entrySelected;
  var type;

  AttendanceUserArguments(this.entrySelected, this.type);

}


void listCentros(MyProvider provider, BuildContext context) async {

  ComoGastoLocalizations? localizations = Localizations.of<
      ComoGastoLocalizations>(context, ComoGastoLocalizations);

  try {
    final url = Uri.parse("http://" + ip + ":8080/api/rest/facilities");
    final response = await http.get(
        url, headers: {"x-hasura-admin-secret": "myadminsecretkey"})
        .timeout(const Duration(seconds: 20));


    var datos = json.decode(response.body);

    List centros = [];
    List centrosData = [];

    for (int i = 0; i < datos['facilities'].length; i++) {
      centros.add(datos['facilities'][i]['name']);
      centrosData.add(datos['facilities'][i]);
    }

    provider.centresData = centrosData;
    provider.centres = centros.map((e) => e as String).toList();
  } on SocketException catch (e){
    if (provider.dialogShow == 0){
      provider.dialogShow == 1;
      errorDialog(context, provider, localizations!.t('errordialogos.conexiontitulo'),
          localizations.t('errordialogos.conexion'), localizations.t('errordialogos.boton'));
      provider.dialogShow == 0;
    }
  } on TimeoutException catch (e) {
    if (provider.dialogShow == 0){
      provider.dialogShow == 1;
      errorDialog(context, provider, localizations!.t('errordialogos.conexiontitulo'),
          localizations.t('errordialogos.conexion'), localizations.t('errordialogos.boton'));
      provider.dialogShow == 0;
    }
  } on Error catch (e) {
    print("INTERNAL ERROR");
  }
}


void listUser(MyProvider provider, BuildContext context) async {
  ComoGastoLocalizations? localizations = Localizations.of<
      ComoGastoLocalizations>(context, ComoGastoLocalizations);

  try {
    final url = Uri.parse("http://" + ip + ":8080/api/rest/users");
    final response = await http.get(
        url, headers: {"x-hasura-admin-secret": "myadminsecretkey"})
        .timeout(const Duration(seconds: 20));

    var datos = json.decode(response.body);


    List users = [];

    for (int i = 0; i < datos['users'].length; i++) {
      users.add(datos['users'][i]);
    }

    provider.usersTotal = users;
  } on SocketException catch (e) {
    if (provider.dialogShow == 0){
      provider.dialogShow == 1;
      errorDialog(
          context, provider, localizations!.t('errordialogos.conexiontitulo'),
          localizations.t('errordialogos.conexion'),
          localizations.t('errordialogos.boton')
      );
      provider.dialogShow == 0;
    }
  } on TimeoutException catch (e) {
    if (provider.dialogShow == 0){
      provider.dialogShow == 1;
      errorDialog(
          context, provider, localizations!.t('errordialogos.conexiontitulo'),
          localizations.t('errordialogos.conexion'),
          localizations.t('errordialogos.boton')
      );
      provider.dialogShow == 0;
    }
  } on Error catch (e) {
    print("INTERNAL ERROR");
  }
}


void buscar(BuildContext context, MyProvider provider, String uuid) async {
  ComoGastoLocalizations? localizations = Localizations.of<
      ComoGastoLocalizations>(context, ComoGastoLocalizations);

  try {
    final url = Uri.parse("http://" + ip + ":8080/api/rest/users/" + uuid);
    final response = await http.get(
        url, headers: {"x-hasura-admin-secret": "myadminsecretkey"})
        .timeout(const Duration(seconds: 20));

    var datos = json.decode(response.body);

    DateTime now = DateTime.now();

    Navigator.pushNamed(context, "/qrform",
        arguments: User(
            datos['users'][0]['uuid'],
            datos['users'][0]['username'],
            datos['users'][0]['name'],
            datos['users'][0]['surname'],
            datos['users'][0]['email'],
            datos['users'][0]['phone'],
            datos['users'][0]['is_vaccinated'],
            now));
  } on SocketException catch (e) {
    errorDialog(
        context, provider, localizations!.t('errordialogos.conexiontitulo'),
        localizations.t('errordialogos.conexion'),
        localizations.t('errordialogos.boton'));
  } on TimeoutException catch (e) {
    errorDialog(
        context, provider, localizations!.t('errordialogos.conexiontitulo'),
        localizations.t('errordialogos.conexion'),
        localizations.t('errordialogos.boton'));
  } on Error catch (e) {
    print("INTERNAL ERROR");
  }
}


void confirmar(BuildContext context, MyProvider provider,  Register register) async {

  ComoGastoLocalizations? localizations = Localizations.of<
      ComoGastoLocalizations>(context, ComoGastoLocalizations);

  try {
    var access = {

      "user_id": register.uuid,
      "facility_id": register.centre,
      "timestamp": formatoFechaBaseDatos(register.timestamp, localizations!.localeName),
      "type": register.type,
      "temperature": formatoTemperaturaBaseDatos(register.temperature, localizations.localeName),
    };

    final url = Uri.parse("http://" + ip + ":8080/api/rest/access_log");
    final response = await http.post(
      url,
      headers: {"x-hasura-admin-secret": "myadminsecretkey"
      },
      body: json.encode(access),
    ).timeout(const Duration(seconds: 20));

    infoDialog(context, provider, localizations.t('infodialogos.oktitulo'), localizations.t('infodialogos.ok') ,
        localizations.t('infodialogos.boton'));

  } on SocketException catch (e){
    errorDialog(context, provider, localizations!.t('errordialogos.conexiontitulo'), localizations.t('errordialogos.conexion'),
        localizations.t('errordialogos.boton'));
  } on TimeoutException catch (e) {
    errorDialog(context,provider, localizations!.t('errordialogos.conexiontitulo'), localizations.t('errordialogos.conexion'),
        localizations.t('errordialogos.boton'));  } on Error catch (e) {
    print("INTERNAL ERROR");
  }
}


void asistenciaActual(BuildContext context, MyProvider provider, String centre) async {
  ComoGastoLocalizations? localizations = Localizations.of<
      ComoGastoLocalizations>(context, ComoGastoLocalizations);

  try {
    final url = Uri.parse(
        "http://" + ip + ":8080/api/rest/facility_access_log/" + centre);
    final response = await http.get(
        url, headers: {"x-hasura-admin-secret": "myadminsecretkey"})
        .timeout(const Duration(seconds: 20));


    var datos = json.decode(response.body);

    int attendanceIn = 0;
    int attendanceOut = 0;

    int attendanceActual = 0;
    double attendanceMax = 1;

    print(DateTime.now().toString());
    for (int i = 0; i < datos['access_log'].length; i++) {
      if (DateTime.parse(datos['access_log'][i]['timestamp']).isBefore(DateTime.now().add(new Duration(hours: 1)))) {
        if (datos['access_log'][i]['type'] == "IN") {
          attendanceIn++;
        }
        else if (datos['access_log'][i]['type'] == "OUT") {
          attendanceOut++;
        }
      }
    }

    attendanceActual = attendanceIn - attendanceOut;

    for (int i = 0; i < provider.centresData.length; i++) {
      if (provider.centresData[i]['id'].toString() == centre) {
        attendanceMax = provider.centresData[i]['max_capacity'] *
            (provider.centresData[i]['percentage_capacity_allowed'] / 100);
        break;
      }
    }


    List<GradesData> data = [
      GradesData('IN', ((attendanceActual / attendanceMax) * 100).toInt(),
          charts.MaterialPalette.red.shadeDefault),
      GradesData('OUT',
          (((attendanceMax - attendanceActual) / attendanceMax) * 100).toInt(),
          charts.MaterialPalette.green.shadeDefault),
    ];

    provider.maxCapacity = attendanceMax.toInt();
    provider.peopleInside = attendanceActual;
    provider.actualAttendance = data;
  } on SocketException catch (e) {
    errorDialog(
        context, provider, localizations!.t('errordialogos.conexiontitulo'),
        localizations.t('errordialogos.conexion'),
        localizations.t('errordialogos.boton'));
  } on TimeoutException catch (e) {
    errorDialog(
        context, provider, localizations!.t('errordialogos.conexiontitulo'),
        localizations.t('errordialogos.conexion'),
        localizations.t('errordialogos.boton')
    );
  }
  on Error catch (e) {
    print("INTERNAL ERROR");
  }
}


void asistenciaEntrada(BuildContext context, MyProvider provider, String centre, String initialDate, String finalDate) async {

  ComoGastoLocalizations? localizations = Localizations.of<
      ComoGastoLocalizations>(context, ComoGastoLocalizations);

  try {
    final url = Uri.parse(
        "http://" + ip + ":8080/api/rest/facility_access_log/" + centre);
    final response = await http.get(
        url, headers: {"x-hasura-admin-secret": "myadminsecretkey"})
        .timeout(const Duration(seconds: 20));


    var datos = json.decode(response.body);

    List users = [];

    for (int i = 0; i < datos['access_log'].length; i++) {
      if (DateTime.parse(datos['access_log'][i]['timestamp']).isAfter(
          DateTime.parse(formatoFechaBaseDatos(initialDate, localizations!.localeName))) &&
          DateTime.parse(datos['access_log'][i]['timestamp']).isBefore(
              DateTime.parse(formatoFechaBaseDatos(finalDate, localizations.localeName)))) {
        if (datos['access_log'][i]['type'] == "IN") {
          users.add(datos['access_log'][i]);
        }
      }
    }

    provider.userCentre = users;
  } on SocketException catch (e){
    errorDialog(context, provider, localizations!.t('errordialogos.conexiontitulo'), localizations.t('errordialogos.conexion'),
        localizations.t('errordialogos.boton'));
  } on TimeoutException catch (e) {
    errorDialog(context, provider, localizations!.t('errordialogos.conexiontitulo'), localizations.t('errordialogos.conexion'),
        localizations.t('errordialogos.boton'));
  } on Error catch (e) {
    print("INTERNAL ERROR");
  }
}


void asistenciaSalida(BuildContext context, MyProvider provider, String centre, String initialDate, String finalDate) async {
  ComoGastoLocalizations? localizations = Localizations.of<
      ComoGastoLocalizations>(context, ComoGastoLocalizations);

  try {
    final url = Uri.parse(
        "http://" + ip + ":8080/api/rest/facility_access_log/" + centre);
    final response = await http.get(
        url, headers: {"x-hasura-admin-secret": "myadminsecretkey"})
        .timeout(const Duration(seconds: 20));


    var datos = json.decode(response.body);

    List users = [];

    for (int i = 0; i < datos['access_log'].length; i++) {
      if (DateTime.parse(datos['access_log'][i]['timestamp']).isAfter(
          DateTime.parse(
              formatoFechaBaseDatos(initialDate, localizations!.localeName))) &&
          DateTime.parse(datos['access_log'][i]['timestamp']).isBefore(
              DateTime.parse(formatoFechaBaseDatos(
                  finalDate, localizations.localeName)))) {
        if (datos['access_log'][i]['type'] == "OUT") {
          users.add(datos['access_log'][i]);
        }
      }
    }

    provider.userCentreExits = users;
  } on SocketException catch (e) {
    errorDialog(
        context, provider, localizations!.t('errordialogos.conexiontitulo'),
        localizations.t('errordialogos.conexion'),
        localizations.t('errordialogos.boton'));
  } on TimeoutException catch (e) {
    errorDialog(
        context, provider, localizations!.t('errordialogos.conexiontitulo'),
        localizations.t('errordialogos.conexion'),
        localizations.t('errordialogos.boton'));
  } on Error catch (e) {
    print("INTERNAL ERROR");
  }
}




