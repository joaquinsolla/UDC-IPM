import 'package:entryqr/provider/como_gasto_localizations.dart';
import 'package:entryqr/provider/databasepetition.dart';
import 'package:entryqr/provider/provider.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../common.dart';



class AttendancePage extends StatefulWidget {
  AttendancePage({Key? key}) : super(key: key);

  @override
  AttendanceState createState() => AttendanceState();
}

class AttendanceState extends State<AttendancePage> {

  String initialDate = "";
  String initialHour = "";
  String finalDate = "";
  String finalHour = "";

  TextEditingController initialDateController = TextEditingController();
  TextEditingController finalDateController = TextEditingController();
  TextEditingController initialHourController = TextEditingController();
  TextEditingController finalHourController = TextEditingController();

  String totalInitialDate = "";
  String totalFinalDate = "";



  String? _selectedCentre;

  List asistence = [];


  late FocusNode centreFocus;
  late FocusNode initialDateFocus;
  late FocusNode initialHourFocus;
  late FocusNode finalDateFocus;
  late FocusNode finalHourFocus;
  late FocusNode searchFocus;


  @override
  Widget build(BuildContext context) {
    final provider = Provider.of<MyProvider>(context);

    ComoGastoLocalizations? localizations = Localizations.of<
        ComoGastoLocalizations>(context, ComoGastoLocalizations);

    return Scaffold(
        backgroundColor: Colors.white,

        appBar: MainAppBar(),

        body: Padding(
            padding: const EdgeInsets.fromLTRB(20.0, 0.0, 20.0, 0.0),
            child: ListView(
                children: <Widget>[
                  SubLabel(localizations!.t('asistencia.titulo')),
                  SizedBox(height: 30.0,),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.end,
                    children: [
                      SizedBox(
                        width: 200,
                        child: TextButton(
                          onPressed: () {
                            Navigator.pushNamed(context, "/attendancenow",);
                          },
                          style: TextButton.styleFrom(
                            backgroundColor: Color(0xff009688),
                          ),

                          child: Text(localizations.t('asistencia.aforo'),
                              style: TextStyle(fontSize: 16.0, color: Colors.white)),
                        ),
                      )
                    ],
                  ),

                  SizedBox(height: 30.0,),


                  Container(
                    width: 300,
                    padding: EdgeInsets.symmetric(
                        vertical: 5, horizontal: 15),
                    decoration: BoxDecoration(
                        color: Color(0xffd3d3d3)
                    ),
                    child: DropdownButton<String>(
                      focusNode: centreFocus,
                      onChanged: (value) {
                        setState(() {
                          _selectedCentre = value;
                        });
                      },
                      value: _selectedCentre,

                      // Hide the default underline
                      underline: Container(
                        color: Colors.black,
                      ),
                      hint: Row(
                          mainAxisSize: MainAxisSize.max,
                          children: [
                            Text(
                              localizations.t('asistencia.centro'),
                              style: TextStyle(color: Colors.black),
                            ),
                          ]),

                      isExpanded: true,

                      // The list of options
                      items: provider.centres
                          .map((e) =>
                          DropdownMenuItem(
                            child: Container(
                              alignment: Alignment.centerLeft,
                              child: Text(
                                e,
                                style: TextStyle(fontSize: 18),
                              ),
                            ),
                            value: e,
                          ))
                          .toList(),

                      // Customize the selected item
                      selectedItemBuilder: (BuildContext context) =>
                          provider.centres
                              .map((e) =>
                              Center(
                                child: Text(
                                  e,
                                  style: TextStyle(
                                      fontSize: 18,
                                      color: Colors.black,
                                      fontWeight: FontWeight.normal),
                                ),
                              ))
                              .toList(),
                    ),
                  ),

                  SizedBox(height: 20.0,),
                  TextFormField(
                    cursorColor: Colors.blueGrey,
                    keyboardType: TextInputType.datetime,
                    textInputAction: TextInputAction.next,
                    focusNode: initialDateFocus,
                    onEditingComplete: () => requestFocus(context, initialHourFocus),
                    controller: initialDateController,
                    decoration: InputDecoration(
                      labelText: localizations.t('asistencia.fechainicial'),
                      hintText: localizations.t('asistencia.hintfecha'),
                      fillColor: Color(0xffd3d3d3),
                      filled: true,
                    ),
                  ),
                  SizedBox(height: 20.0,),
                  TextFormField(
                    cursorColor: Colors.blueGrey,
                    keyboardType: TextInputType.datetime,
                    textInputAction: TextInputAction.next,
                    focusNode: initialHourFocus,
                    onEditingComplete: () => requestFocus(context, finalDateFocus),
                    controller: initialHourController,
                    decoration: InputDecoration(
                      labelText: localizations.t('asistencia.horainicial'),
                      hintText: localizations.t('asistencia.hinthora'),
                      fillColor: Color(0xffd3d3d3),
                      filled: true,
                    ),
                  ),
                  SizedBox(height: 20.0,),
                  TextFormField(
                    cursorColor: Colors.blueGrey,
                    keyboardType: TextInputType.datetime,
                    textInputAction: TextInputAction.next,
                    focusNode: finalDateFocus,
                    onEditingComplete: () => requestFocus(context, finalHourFocus),
                    controller: finalDateController,
                    decoration: InputDecoration(
                      labelText: localizations.t('asistencia.fechafinal'),
                      hintText: localizations.t('asistencia.hintfecha'),
                      fillColor: Color(0xffd3d3d3),
                      filled: true,
                    ),
                  ),

                  SizedBox(height: 20.0,),
                  TextFormField(
                    cursorColor: Colors.blueGrey,
                    keyboardType: TextInputType.datetime,
                    textInputAction: TextInputAction.next,
                    focusNode: finalHourFocus,
                    onEditingComplete: () => requestFocus(context, finalHourFocus),
                    controller: finalHourController,
                    decoration: InputDecoration(
                      labelText: localizations.t('asistencia.horafinal'),
                      hintText: localizations.t('asistencia.hinthora'),
                      fillColor: Color(0xffd3d3d3),
                      filled: true,
                    ),
                  ),

                  SizedBox(height: 20.0,),
                  TextButton(
                    focusNode: searchFocus,
                    onPressed: () {
                      //SAVE VARIABLES
                      saveFormEntries();

                      //CHECK VALUES
                      int signal = checkAttendanceValues(localizations);

                      //SHOW DIALOG
                      signalControl(context, provider, signal);

                      //DO
                      if (signal == 0) {
                        attendance_Search(context, provider);
                      }
                    },
                    style: TextButton.styleFrom(
                      primary: Colors.black,
                      backgroundColor: Color(0xff009688)
                    ),
                    child: Text(localizations.t('asistencia.buscar'),
                        style: TextStyle(fontSize: 16.0, color: Colors.white)),
                  ),
                  SizedBox(height: 20.0,),
                ],
            ),
        ),
    );
  }

  void saveFormEntries() {
    initialDate = initialDateController.text;
    initialHour = initialHourController.text;
    totalInitialDate = initialDate + " " + initialHour;
    finalDate = finalDateController.text;
    finalHour = finalHourController.text;
    totalFinalDate = finalDate + " " + finalHour;
  }

  int checkAttendanceValues(ComoGastoLocalizations localizations) {
    /* SIGNALS:
    * 0: OK
    * 1: SOME EMPTY
    * 2: PERSON DOES NOT EXIST
    * 3: BAD DATE FORMAT
    * 4: BAD TEMPERATURE FORMAT
    * 5: INITIAL DATE AFTER FINAL DATE
    */

    if (_selectedCentre == null || initialDate.isEmpty || initialHour.isEmpty ||
        finalDate.isEmpty || finalHour.isEmpty)
      return 1;

    if (checkDate(totalInitialDate, localizations.localeName) == false)
      return 3;

    if (checkDate(totalFinalDate, localizations.localeName) == false)
      return 3;

    DateTime init = DateTime.parse(formatoFechaBaseDatos(totalInitialDate, localizations.localeName));
    DateTime fin = DateTime.parse(formatoFechaBaseDatos(totalFinalDate, localizations.localeName));
    if (init.isAfter(fin) || init == fin)
      return 5;

    //If all ok -> signal 0
    return 0;
  }


  void attendance_Search(BuildContext context, MyProvider provider) {
    String? _selectedCentreID;

    for (int i = 0; i < provider.centresData.length; i++) {
      if (provider.centresData[i]['name'].toString() ==
          _selectedCentre.toString()) {
        _selectedCentreID = provider.centresData[i]['id'].toString();
        break;
      }
    }

    asistenciaEntrada(context, provider, _selectedCentreID!, totalInitialDate, totalFinalDate);
    asistenciaSalida(context, provider, _selectedCentreID, totalInitialDate, totalFinalDate);

    Navigator.pushNamed(context, "/attendancesearch",
        arguments: AttendanceSearchArguments(
            _selectedCentre!, totalInitialDate, totalFinalDate));
  }


  @override
  void initState() {
    super.initState();


    centreFocus = FocusNode();
    initialDateFocus = FocusNode();
    initialHourFocus = FocusNode();
    finalDateFocus = FocusNode();
    finalHourFocus = FocusNode();
    searchFocus = FocusNode();
  }

  @override
  void dispose() {
    super.dispose();

    centreFocus.dispose();
    initialDateFocus.dispose();
    initialHourFocus.dispose();
    finalDateFocus.dispose();
    finalHourFocus.dispose();
    searchFocus.dispose();
  }
}
