import 'package:flutter/material.dart';
import 'package:flutter/foundation.dart';

import 'databasepetition.dart';
import 'package:charts_flutter/flutter.dart' as charts;


class MyProvider extends ChangeNotifier {


  // Language

  String _language = "";

  String get language => _language;

  set language(String lang) {
    _language = lang;
    notifyListeners();
  }


  // List of names of the centres in the data base

  List<String> _centres = [];

  List<String> get centres => _centres;

  set centres(List<String> centros) {
    _centres = centros;
    notifyListeners();
  }

  // List of the centres in the data base

  List _centresData = [];

  List get centresData => _centresData;

  set centresData(List centres) {
    _centresData = centres;
    notifyListeners();
  }

  // List of the users in the data base

  List _usersTotal = [];

  List get usersTotal => _usersTotal;

  set usersTotal(List userList) {
    _usersTotal = userList;
    notifyListeners();
  }


  // UUID of the person which is manually registered

  String _uuid = "";

  String get uuid => _uuid;

  set uuid(String id) {
    _uuid = id;
    notifyListeners();
  }


  //Graphics of actual attendance

  List<GradesData> _actualAttendance = [GradesData('IN', 0, charts.MaterialPalette.red.shadeDefault),
    GradesData('OUT', 100, charts.MaterialPalette.green.shadeDefault)];

  List<GradesData> get actualAttendance => _actualAttendance;

  set actualAttendance(List<GradesData> actual) {
    _actualAttendance = actual;
    notifyListeners();
  }

  //People Inside

  int _peopleInside = 0;

  int get peopleInside => _peopleInside;

  set peopleInside(int people){
    _peopleInside = people;
    notifyListeners();
  }

  //MaxCapacity Centre
  int _maxCapacity = 0;

  int get maxCapacity => _maxCapacity;

  set maxCapacity(int capacity){
    _maxCapacity = capacity;
    notifyListeners();
  }


  // List of the different entries in a centre

  List _userCentre = [];

  List get userCentre => _userCentre;

  set userCentre(List users) {
    _userCentre = users;
    notifyListeners();
  }


  // List of the different exits in a centre

  List _userCentreExits = [];

  List get userCentreExits => _userCentreExits;

  set userCentreExits(List usersExits) {
    _userCentreExits = usersExits;
    notifyListeners();
  }


  // Show error dialog if there is not already one being showed

  int _dialogShow = 0;

  int get dialogShow => _dialogShow;

  set dialogShow(int dialog) {
    _dialogShow = dialog;
    notifyListeners();
  }

}