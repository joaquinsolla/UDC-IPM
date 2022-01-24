import 'package:entryqr/provider/como_gasto_localizations.dart';
import 'package:entryqr/provider/databasepetition.dart';
import 'package:entryqr/provider/provider.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../common.dart';


class AttendanceSearch extends StatelessWidget {
  const AttendanceSearch({Key? key}) : super(key: key);


  @override
  Widget build(BuildContext context) {
    final AttendanceSearchArguments arguments = ModalRoute
        .of(context)!
        .settings
        .arguments as AttendanceSearchArguments;

    final provider = Provider.of<MyProvider>(context);

    ComoGastoLocalizations? localizations = Localizations.of<
        ComoGastoLocalizations>(context, ComoGastoLocalizations);

    return DefaultTabController(
      length: 2,
      child: Scaffold(
        backgroundColor: Colors.white,
        appBar: AppBar(
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
          bottom: TabBar(
            tabs: [
              Text(localizations!.t('asistencia.entradatitulo') + "\n"),
              Text(localizations.t('asistencia.salidatitulo') + "\n"),
            ],
          ),
        ),

        body: TabBarView(
          children: [
            Padding(
                padding: const EdgeInsets.fromLTRB(20.0, 0.0, 20.0, 0.0),
                child: ListView(
                  children: <Widget>[
                    SubLabel(localizations.t('asistencia.asistenciaentradas')),
                    SizedBox(height: 70.0,),
                    Row(
                      children: [
                        Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Text(localizations.t('asistencia.centro'), style: TextStyle(fontSize: 15.0,
                                fontWeight: FontWeight.bold),),
                            SizedBox(height: 20.0,),
                            Text(localizations.t('asistencia.inicial'), style: TextStyle(fontSize: 15.0,
                                fontWeight: FontWeight.bold),),
                            SizedBox(height: 20.0,),
                            Text(localizations.t('asistencia.final'), style: TextStyle(fontSize: 15.0,
                                fontWeight: FontWeight.bold),),
                            SizedBox(height: 20.0,),
                            Text(localizations.t('asistencia.entradas'), style: TextStyle(fontSize: 15.0,
                                fontWeight: FontWeight.bold),),
                          ],


                        ),
                        SizedBox(width: 20.0,),
                        Column(

                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Text(arguments.centro,
                              style: TextStyle(fontSize: 15.0),),
                            SizedBox(height: 20.0,),
                            Text(arguments.initialDate,
                              style: TextStyle(fontSize: 15.0),),
                            SizedBox(height: 20.0,),
                            Text(arguments.finalDate,
                              style: TextStyle(fontSize: 15.0),),
                            SizedBox(height: 20.0,),
                            Text(provider.userCentre.length.toString(),
                              style: TextStyle(fontSize: 15.0),),
                          ],


                        )
                      ],
                    ),
                    SizedBox(height: 60.0,),
                    Row(
                      children: [
                        SizedBox(width: 40.0, height: 30.0,),
                        SizedBox(width: 70.0, height: 30.0,
                          child: Text(localizations.t('asistencia.nombre'),
                            style: TextStyle(fontWeight: FontWeight.bold),),
                        ),
                        SizedBox(width: 8.0, height: 30.0,),
                        SizedBox(width: 60.0, height: 30.0,
                          child: Text(localizations.t('asistencia.apellidos'),
                              style: TextStyle(fontWeight: FontWeight.bold)),
                        ),
                        SizedBox(width: 10.0, height: 30.0,),
                        SizedBox(width: 120.0, height: 30.0,
                          child: Text(localizations.t('asistencia.fechaentrada'),
                              style: TextStyle(fontWeight: FontWeight.bold)),
                        ),
                      ],
                    ),
                    ListTotalUserEntry(localizations),
                    SizedBox(height: 20.0,)
                  ],
                )
            ),
            Padding(
                padding: const EdgeInsets.fromLTRB(20.0, 0.0, 20.0, 0.0),
                child: ListView(
                  children: <Widget>[
                    SubLabel(localizations.t('asistencia.asistenciasalidas')),
                    SizedBox(height: 70.0,),
                    Row(
                      children: [
                        Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Text(localizations.t('asistencia.centro'), style: TextStyle(fontSize: 15.0,
                                fontWeight: FontWeight.bold),),
                            SizedBox(height: 20.0,),
                            Text(localizations.t('asistencia.inicial'), style: TextStyle(fontSize: 15.0,
                                fontWeight: FontWeight.bold),),
                            SizedBox(height: 20.0,),
                            Text(localizations.t('asistencia.final'), style: TextStyle(fontSize: 15.0,
                                fontWeight: FontWeight.bold),),
                            SizedBox(height: 20.0,),
                            Text(localizations.t('asistencia.salidas'), style: TextStyle(fontSize: 15.0,
                                fontWeight: FontWeight.bold),),
                          ],


                        ),
                        SizedBox(width: 20.0,),
                        Column(

                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Text(arguments.centro,
                              style: TextStyle(fontSize: 15.0),),
                            SizedBox(height: 20.0,),
                            Text(arguments.initialDate,
                              style: TextStyle(fontSize: 15.0),),
                            SizedBox(height: 20.0,),
                            Text(arguments.finalDate,
                              style: TextStyle(fontSize: 15.0),),
                            SizedBox(height: 20.0,),
                            Text(provider.userCentreExits.length.toString(),
                              style: TextStyle(fontSize: 15.0),),
                          ],


                        )
                      ],
                    ),
                    SizedBox(height: 60.0,),
                    Row(
                      children: [
                        SizedBox(width: 40.0, height: 30.0,),
                        SizedBox(width: 70.0, height: 30.0,
                          child: Text(localizations.t('asistencia.nombre'),
                            style: TextStyle(fontWeight: FontWeight.bold),),
                        ),
                        SizedBox(width: 8.0, height: 30.0,),
                        SizedBox(width: 60.0, height: 30.0,
                          child: Text(localizations.t('asistencia.apellidos'),
                              style: TextStyle(fontWeight: FontWeight.bold)),
                        ),
                        SizedBox(width: 10.0, height: 30.0,),
                        SizedBox(width: 120.0, height: 30.0,
                          child: Text(localizations.t('asistencia.fechasalida'),
                              style: TextStyle(fontWeight: FontWeight.bold)),
                        ),
                      ],
                    ),
                    ListTotalUserExit(localizations),
                    SizedBox(height: 20.0,)
                  ],
                )
            ),          ],
        )
      ),
    );
  }
}



class ListTotalUserEntry extends StatelessWidget {

  final ComoGastoLocalizations localizations;

  ListTotalUserEntry(this.localizations, {Key? key}) : super(key: key);


  final List<Widget> users = <Widget>[];

  @override
  Widget build(BuildContext context) {
    final provider = Provider.of<MyProvider>(context);

    entryUser(provider, context);

    return Container(
      child: Column(
        children:
        List.generate(provider.userCentre.length, (index) {
          return users[index];
        }),
      ),
    );
  }

  void entryUser(MyProvider provider, BuildContext context){

    for(int i = 0; i<provider.userCentre.length; i++){
      users.add(TextButton(
          onPressed: () {
            selectUser(context, provider, provider.userCentre[i]['user']['name'],
                provider.userCentre[i]['user']['surname'], provider.userCentre[i]['timestamp'], 0);
          },
          style: TextButton.styleFrom(
            primary: Colors.black,
          ),
          child: GestureDetector(
            child: Padding(
              padding: const EdgeInsets.fromLTRB(0.0, 0.7, 0.0, 0.7),
              child:
              Container(
                decoration: new BoxDecoration(
                  color: Color(0xffd3d3d3),
                ),
                child: Row(

                  children: <Widget>[

                    Icon(Icons.account_circle),
                    SizedBox(width: 2.0,height: 30.0,),
                    SizedBox(width: 75.0,height: 30.0,
                      child: Text(provider.userCentre[i]['user']['name']),
                    ),
                    SizedBox(width: 5.0, height: 30.0,),
                    SizedBox(width: 55.0, height: 30.0,
                      child: Text(provider.userCentre[i]['user']['surname']),
                    ),
                    SizedBox(width: 10.0,height: 30.0,),
                    SizedBox(width: 114.0,height: 30.0,
                      child: Text(formatoFechaApp(provider.userCentre[i]['timestamp'], this.localizations.localeName)),
                    ),
                  ],
                ),
              ),
            ),
          )
      )
      );
    }


  }


}


class ListTotalUserExit extends StatelessWidget {

  final ComoGastoLocalizations localizations;

  ListTotalUserExit(this.localizations, {Key? key}) : super(key: key);


  final List<Widget> users = <Widget>[];

  @override
  Widget build(BuildContext context) {
    final provider = Provider.of<MyProvider>(context);

    exitUser(provider, context);

    return Container(
      child: Column(
        children:
        List.generate(provider.userCentreExits.length, (index) {
          return users[index];
        }),
      ),
    );
  }

  void exitUser(MyProvider provider, BuildContext context) {
    for (int i = 0; i < provider.userCentreExits.length; i++) {
      users.add(TextButton(
          onPressed: () {
            selectUser(
                context, provider, provider.userCentreExits[i]['user']['name'],
                provider.userCentreExits[i]['user']['surname'],
                provider.userCentreExits[i]['timestamp'], 1);
          },
          style: TextButton.styleFrom(
            primary: Colors.black,
          ),
          child: GestureDetector(
            child: Padding(
              padding: const EdgeInsets.fromLTRB(0.0, 0.7, 0.0, 0.7),
              child:
              Container(
                decoration: new BoxDecoration(
                  color: Color(0xffd3d3d3),
                ),
                child: Row(

                  children: <Widget>[

                    Icon(Icons.account_circle),
                    SizedBox(width: 2.0, height: 30.0,),
                    SizedBox(width: 75.0, height: 30.0,
                      child: Text(provider.userCentreExits[i]['user']['name']),
                    ),
                    SizedBox(width: 5.0, height: 30.0,),
                    SizedBox(width: 55.0, height: 30.0,
                      child: Text(
                          provider.userCentreExits[i]['user']['surname']),
                    ),
                    SizedBox(width: 10.0, height: 30.0,),
                    SizedBox(width: 114.0, height: 30.0,
                      child: Text(
                          formatoFechaApp(provider.userCentreExits[i]['timestamp'], this.localizations.localeName)),
                    ),
                  ],
                ),
              ),
            ),
          )
      )
      );
    }
  }


}



selectUser(BuildContext context, MyProvider provider, String name, String surname, String date, int type){

  int selected = 0;

  if (type == 0){
    for (int i = 0; i< provider.userCentre.length; i++){

      if (provider.userCentre[i]['user']['name'] == name &&
          provider.userCentre[i]['user']['surname'] == surname &&
          provider.userCentre[i]['timestamp'] == date){

        selected = i;

        break;
      }
    }

    Navigator.pushNamed(context, "/attendanceuser",
        arguments: AttendanceUserArguments(selected, 0));

  }
  else if (type == 1){
    for (int i = 0; i< provider.userCentreExits.length; i++){

      if (provider.userCentreExits[i]['user']['name'] == name &&
          provider.userCentreExits[i]['user']['surname'] == surname &&
          provider.userCentreExits[i]['timestamp'] == date){

        selected = i;

        break;
      }
    }

    Navigator.pushNamed(context, "/attendanceuser",
        arguments: AttendanceUserArguments(selected, 1));

  }
}

