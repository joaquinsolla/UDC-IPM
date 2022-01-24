import 'dart:async';

import 'package:entryqr/provider/como_gasto_localizations.dart';
import 'package:entryqr/provider/databasepetition.dart';
import 'package:entryqr/provider/provider.dart';
import 'package:flutter/material.dart';
import 'package:charts_flutter/flutter.dart' as charts;
import 'package:provider/provider.dart';
import 'package:intl/intl.dart';

import '../common.dart';


class AttendanceNow extends StatefulWidget {
  AttendanceNow({Key? key}) : super(key: key);

  @override
  AttendanceNowState createState() => AttendanceNowState();
}

class AttendanceNowState extends State<AttendanceNow> {


  String? _selectedCentre;
  late FocusNode centreFocus;
  late String _timeString;
  late Timer t;

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
        child: Column(
          children: <Widget>[
            SubLabel(localizations!.t('asistencia.aforo')),
            SizedBox(height: 20.0,),

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
                  attendance_Now(context, provider);
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

            Text(
              "Última Actualización: " + _timeString.toString(),
              style: TextStyle(
                  color: Colors.black,
                  fontSize: 20.0,
                  fontWeight: FontWeight.bold,
                  fontFamily: 'SourceSansPro'
              ),
            ),

            SizedBox(height: 10.0,),

            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Text(localizations.t('asistencia.porcentajeocupacion') + ": " +
                    provider.actualAttendance[0].numberOfPeople.toString() + " %",
                    style: TextStyle(
                      fontSize: 16.0,
                      color: Colors.black,
                      fontWeight: FontWeight.bold,

                    ),
                ),
              ],
            ),

            SizedBox(height: 5.0,),

            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Text(localizations.t('asistencia.personasdentro') + ": " +
                    provider.peopleInside.toString(),
                  style: TextStyle(
                    fontSize: 16.0,
                    color: Colors.black,
                    fontWeight: FontWeight.bold,

                  ),
                ),
              ],
            ),

            SizedBox(height: 5.0,),

            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Text(localizations.t('asistencia.capacidadmaxima') + ": " +
                    provider.maxCapacity.toString(),
                  style: TextStyle(
                    fontSize: 16.0,
                    color: Colors.black,
                    fontWeight: FontWeight.bold,

                  ),
                ),
              ],
            ),

            Expanded(
              child: charts.PieChart<String>(
                _getData(provider),
                animate: true,
                defaultRenderer: new charts.ArcRendererConfig(
                    arcWidth: 60,
                    arcRendererDecorators: [new charts.ArcLabelDecorator()]
                ),
              ),
            )
          ],
        ),
      ),
    );
  }

  void attendance_Now(BuildContext context, MyProvider provider){

    String? _selectedCentreID;

    for (int i = 0; i < provider.centresData.length; i++) {
      if (provider.centresData[i]['name'].toString() ==
          _selectedCentre.toString()) {
        _selectedCentreID = provider.centresData[i]['id'].toString();
        break;
      }
    }

    asistenciaActual(context, provider, _selectedCentreID!);

  }

  void _getTime(){
    final DateTime now = DateTime.now();
    final String formattedDateTime = _formatDateTime(now);
    setState(() {
      _timeString = formattedDateTime;
    });
  }

  String _formatDateTime(DateTime dateTime){
    return DateFormat.Hm().format(dateTime);
  }

  @override
  void initState() {
    super.initState();

    centreFocus = FocusNode();
    _timeString = _formatDateTime(DateTime.now());
    t = Timer.periodic(Duration(seconds: 60), (Timer t) => _getTime());


  }

  @override
  void dispose() {
    super.dispose();
    t.cancel();
  }
}


_getData(MyProvider provider) {
  List<charts.Series<GradesData, String>> series = [
    charts.Series(
        id: "Grades",
        data: provider.actualAttendance,
        colorFn: (GradesData grade, _) => grade.color,
        labelAccessorFn: (GradesData row, _) => '${row.numberOfPeople} %',
        domainFn: (GradesData grades, _) => grades.gradeSymbol,
        measureFn: (GradesData grades, _) => grades.numberOfPeople,
    )
  ];
  return series;
}
