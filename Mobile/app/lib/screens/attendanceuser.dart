import 'package:entryqr/provider/como_gasto_localizations.dart';
import 'package:entryqr/provider/databasepetition.dart';
import 'package:entryqr/provider/provider.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../common.dart';

class AttendanceUser extends StatelessWidget {
  const AttendanceUser({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final AttendanceUserArguments arguments = ModalRoute
        .of(context)!
        .settings
        .arguments as AttendanceUserArguments;

    final provider = Provider.of<MyProvider>(context);

    ComoGastoLocalizations? localizations = Localizations.of<
        ComoGastoLocalizations>(context, ComoGastoLocalizations);

    if(arguments.type == 0){
      return Scaffold(
          backgroundColor: Colors.white,
          appBar: MainAppBar(),
          body: Padding(
            padding: EdgeInsets.fromLTRB(20.0, 0.0, 20.0, 0.0),
            child: ListView(
              children: [
                SubLabel(localizations!.t('asistencia.titulo')),
                SizedBox(height: 40.0,),
                Column(
                  mainAxisAlignment: MainAxisAlignment.start,
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Container(
                      color: Color(0xffd3d3d3),
                      width: 330.0,
                      height: 30.0,
                      child: Text(localizations.t('asistencia.nombre'),
                        style: TextStyle(fontSize: 15.0,
                          fontWeight: FontWeight.bold),
                      ),
                    ),
                    SizedBox(height: 7.0,),
                    Row(
                      children: [
                        SizedBox(width: 20.0,),
                        Text(provider.userCentre[arguments.entrySelected]['user']['name'],
                          style: TextStyle(fontSize: 15.0, fontWeight: FontWeight.bold),
                        ),
                      ],
                    ),
                    SizedBox(height: 20.0,),
                    Container(
                      color: Color(0xffd3d3d3),
                      width: 330.0,
                      height: 30.0,
                      child: Text(localizations.t('asistencia.apellidos'), style: TextStyle(fontSize: 15.0,
                          fontWeight: FontWeight.bold),
                      ),
                    ),
                    SizedBox(height: 7.0,),
                    Row(
                      children: [
                        SizedBox(width: 20.0,),
                        Text(provider.userCentre[arguments.entrySelected]['user']['surname'],
                          style: TextStyle(fontSize: 15.0, fontWeight: FontWeight.bold),
                        ),
                      ],
                    ),
                    SizedBox(height: 20.0,),
                    Container(
                      color: Color(0xffd3d3d3),
                      width: 330.0,
                      height: 30.0,
                      child: Text(localizations.t('asistencia.uuid'),
                        style: TextStyle(fontSize: 15.0,
                          fontWeight: FontWeight.bold),
                      ),
                    ),
                    SizedBox(height: 7.0,),
                    Row(
                      children: [
                        SizedBox(width: 20.0,),
                        Text(provider.userCentre[arguments
                            .entrySelected]['user']['uuid'],
                          style: TextStyle(fontSize: 15.0,
                              fontWeight: FontWeight.bold),
                        ),
                      ],
                    ),
                    SizedBox(height: 20.0,),
                    Container(
                      color: Color(0xffd3d3d3),
                      width: 330.0,
                      height: 30.0,
                      child: Text(localizations.t('asistencia.telefono'), style: TextStyle(fontSize: 15.0,
                          fontWeight: FontWeight.bold),
                      ),
                    ),
                    SizedBox(height: 7.0,),
                    Row(
                      children: [
                        SizedBox(width: 20.0,),
                        Text(provider.userCentre[arguments.entrySelected]['user']['phone'],
                          style: TextStyle(fontSize: 15.0, fontWeight: FontWeight.bold),
                        ),
                      ],
                    ),
                    SizedBox(height: 20.0,),
                    Container(
                      color: Color(0xffd3d3d3),
                      width: 330.0,
                      height: 30.0,
                      child: Text(localizations.t('asistencia.email'), style: TextStyle(fontSize: 15.0,
                          fontWeight: FontWeight.bold),
                      ),
                    ),
                    SizedBox(height: 7.0,),
                    Row(
                      children: [
                        SizedBox(width: 20.0,),
                        Text(provider.userCentre[arguments.entrySelected]['user']['email'],
                          style: TextStyle(fontSize: 15.0, fontWeight: FontWeight.bold),
                        ),
                      ],
                    ),
                    SizedBox(height: 20.0,),
                    Container(
                      color: Color(0xffd3d3d3),
                      width: 330.0,
                      height: 30.0,
                      child: Text(localizations.t('asistencia.vacunado'), style: TextStyle(fontSize: 15.0,
                          fontWeight: FontWeight.bold),
                      ),
                    ),
                    SizedBox(height: 7.0,),
                    Row(
                      children: [
                        SizedBox(width: 20.0,),
                        Text(provider.userCentre[arguments.entrySelected]['user']['is_vaccinated'].toString(),
                          style: TextStyle(fontSize: 15.0, fontWeight: FontWeight.bold),
                        ),
                      ],
                    ),
                    SizedBox(height: 20.0,),
                    Container(
                      color: Color(0xffd3d3d3),
                      width: 330.0,
                      height: 30.0,
                      child: Text(localizations.t('asistencia.fechaentrada'), style: TextStyle(fontSize: 15.0,
                          fontWeight: FontWeight.bold),
                      ),
                    ),
                    SizedBox(height: 7.0,),
                    Row(
                      children: [
                        SizedBox(width: 20.0,),
                        Text(formatoFechaApp(provider.userCentre[arguments.entrySelected]['timestamp'], localizations.localeName),
                          style: TextStyle(fontSize: 15.0, fontWeight: FontWeight.bold),
                        ),
                      ],
                    ),
                    SizedBox(height: 20.0,),
                    Container(
                      color: Color(0xffd3d3d3),
                      width: 330.0,
                      height: 30.0,
                      child: Text(localizations.t('asistencia.temperatura'), style: TextStyle(fontSize: 15.0,
                          fontWeight: FontWeight.bold),
                      ),
                    ),
                    SizedBox(height: 7.0,),
                    Row(
                      children: [
                        SizedBox(width: 20.0,),
                        Text(
                          formatoTemperaturaApp(provider.userCentre[arguments.entrySelected]['temperature'], localizations.localeName),
                          style: TextStyle(fontSize: 15.0,
                              fontWeight: FontWeight.bold),
                        ),
                      ],
                    ),
                    SizedBox(height: 20.0,)
                  ],
                ),
              ],
            ),
          )
      );
    }
    else{
      return Scaffold(
          backgroundColor: Colors.white,
          appBar: MainAppBar(),
          body: Padding(
            padding: EdgeInsets.fromLTRB(20.0, 0.0, 20.0, 0.0),
            child: ListView(
              children: [
                SubLabel(localizations!.t('asistencia.titulo')),
                SizedBox(height: 40.0,),
                Column(
                  mainAxisAlignment: MainAxisAlignment.start,
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Container(
                      color: Color(0xffd3d3d3),
                      width: 330.0,
                      height: 30.0,
                      child: Text(localizations.t('asistencia.nombre'), style: TextStyle(fontSize: 15.0,
                          fontWeight: FontWeight.bold),
                      ),
                    ),
                    SizedBox(height: 7.0,),
                    Row(
                      children: [
                        SizedBox(width: 20.0,),
                        Text(provider.userCentreExits[arguments.entrySelected]['user']['name'],
                          style: TextStyle(fontSize: 15.0, fontWeight: FontWeight.bold),
                        ),
                      ],
                    ),
                    SizedBox(height: 20.0,),
                    Container(
                      color: Color(0xffd3d3d3),
                      width: 330.0,
                      height: 30.0,
                      child: Text(localizations.t('asistencia.apellidos'), style: TextStyle(fontSize: 15.0,
                          fontWeight: FontWeight.bold),
                      ),
                    ),
                    SizedBox(height: 7.0,),
                    Row(
                      children: [
                        SizedBox(width: 20.0,),
                        Text(provider.userCentreExits[arguments.entrySelected]['user']['surname'],
                          style: TextStyle(fontSize: 15.0, fontWeight: FontWeight.bold),
                        ),
                      ],
                    ),
                    SizedBox(height: 20.0,),
                    Container(
                      color: Color(0xffd3d3d3),
                      width: 330.0,
                      height: 30.0,
                      child: Text(localizations.t('asistencia.uuid'), style: TextStyle(fontSize: 15.0,
                          fontWeight: FontWeight.bold),
                      ),
                    ),
                    SizedBox(height: 7.0,),
                    Row(
                      children: [
                        SizedBox(width: 20.0,),
                        Text(provider.userCentreExits[arguments
                            .entrySelected]['user']['uuid'],
                          style: TextStyle(fontSize: 15.0,
                              fontWeight: FontWeight.bold),
                        ),
                      ],
                    ),
                    SizedBox(height: 20.0,),
                    Container(
                      color: Color(0xffd3d3d3),
                      width: 330.0,
                      height: 30.0,
                      child: Text(localizations.t('asistencia.telefono'), style: TextStyle(fontSize: 15.0,
                          fontWeight: FontWeight.bold),
                      ),
                    ),
                    SizedBox(height: 7.0,),
                    Row(
                      children: [
                        SizedBox(width: 20.0,),
                        Text(provider.userCentreExits[arguments.entrySelected]['user']['phone'],
                          style: TextStyle(fontSize: 15.0, fontWeight: FontWeight.bold),
                        ),
                      ],
                    ),
                    SizedBox(height: 20.0,),
                    Container(
                      color: Color(0xffd3d3d3),
                      width: 330.0,
                      height: 30.0,
                      child: Text(localizations.t('asistencia.email'), style: TextStyle(fontSize: 15.0,
                          fontWeight: FontWeight.bold),
                      ),
                    ),
                    SizedBox(height: 7.0,),
                    Row(
                      children: [
                        SizedBox(width: 20.0,),
                        Text(provider.userCentreExits[arguments.entrySelected]['user']['email'],
                          style: TextStyle(fontSize: 15.0, fontWeight: FontWeight.bold),
                        ),
                      ],
                    ),
                    SizedBox(height: 20.0,),
                    Container(
                      color: Color(0xffd3d3d3),
                      width: 330.0,
                      height: 30.0,
                      child: Text(localizations.t('asistencia.vacunado'), style: TextStyle(fontSize: 15.0,
                          fontWeight: FontWeight.bold),
                      ),
                    ),
                    SizedBox(height: 7.0,),
                    Row(
                      children: [
                        SizedBox(width: 20.0,),
                        Text(provider.userCentreExits[arguments.entrySelected]['user']['is_vaccinated'].toString(),
                          style: TextStyle(fontSize: 15.0, fontWeight: FontWeight.bold),
                        ),
                      ],
                    ),
                    SizedBox(height: 20.0,),
                    Container(
                      color: Color(0xffd3d3d3),
                      width: 330.0,
                      height: 30.0,
                      child: Text(localizations.t('asistencia.fechasalida'), style: TextStyle(fontSize: 15.0,
                          fontWeight: FontWeight.bold),
                      ),
                    ),
                    SizedBox(height: 7.0,),
                    Row(
                      children: [
                        SizedBox(width: 20.0,),
                        Text(formatoFechaApp(provider.userCentreExits[arguments.entrySelected]['timestamp'], localizations.localeName),
                          style: TextStyle(fontSize: 15.0, fontWeight: FontWeight.bold),
                        ),
                      ],
                    ),
                    SizedBox(height: 20.0,),
                    Container(
                      color: Color(0xffd3d3d3),
                      width: 330.0,
                      height: 30.0,
                      child: Text(localizations.t('asistencia.temperatura'),
                        style: TextStyle(fontSize: 15.0,
                          fontWeight: FontWeight.bold),
                      ),
                    ),
                    SizedBox(height: 7.0,),
                    Row(
                      children: [
                        SizedBox(width: 20.0,),
                        Text(
                          formatoTemperaturaApp(provider.userCentreExits[arguments.entrySelected]['temperature'], localizations.localeName),
                          style: TextStyle(fontSize: 15.0,
                              fontWeight: FontWeight.bold),
                        ),
                      ],
                    ),
                    SizedBox(height: 20.0,)
                  ],
                ),
              ],
            ),
          )
      );
    }

  }
}
