import 'package:entryqr/provider/como_gasto_localizations.dart';
import 'package:entryqr/provider/provider.dart';
import 'package:entryqr/screens/attendancenow.dart';
import 'package:entryqr/screens/attendancesearch.dart';
import 'package:entryqr/screens/attendanceuser.dart';
import 'package:entryqr/screens/qrform.dart';
import 'package:entryqr/screens/qrmodify.dart';
import 'package:flutter/material.dart';
import 'package:flutter_localizations/flutter_localizations.dart';
import 'package:provider/provider.dart';

import 'menucontroller.dart';



class mainScreen extends StatelessWidget {
  const mainScreen({Key? key}) : super(key: key);


  @override
  Widget build(BuildContext context) {
    return ChangeNotifierProvider(
      create: (context) => MyProvider(),
      child: MaterialApp(
        debugShowCheckedModeBanner: false,
        title: "mainScreen",
        initialRoute: "/menucontroller",
        routes: {
          "/menucontroller": (BuildContext context) => MenuController(),
          "/qrform": (BuildContext context) => QRForm(),
          "/qrmodify": (BuildContext context) => QRModify(),
          "/attendancenow": (BuildContext context) => AttendanceNow(),
          "/attendancesearch": (BuildContext context) => AttendanceSearch(),
          "/attendanceuser": (BuildContext context) => AttendanceUser()
        },
        supportedLocales: [
          Locale('en'),
          Locale('es'),
        ],
        localizationsDelegates: [
          ComoGastoLocalizations.delegate,
          GlobalMaterialLocalizations.delegate,
          GlobalWidgetsLocalizations.delegate,
          GlobalCupertinoLocalizations.delegate,
        ]
      ),
    );
  }
}





