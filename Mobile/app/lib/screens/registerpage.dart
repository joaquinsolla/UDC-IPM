import 'package:entryqr/provider/como_gasto_localizations.dart';
import 'package:entryqr/provider/databasepetition.dart';
import 'package:entryqr/provider/provider.dart';
import 'package:flutter/material.dart';

import 'package:provider/provider.dart';

import '../common.dart';



class RegisterPage extends StatefulWidget {
  RegisterPage({Key? key}) : super(key: key);

  @override
  ResgisterState createState() => ResgisterState();
}

class ResgisterState extends State<RegisterPage> {

  String nameText = "";
  TextEditingController nameController = TextEditingController();

  String surnameText = "";
  TextEditingController surnameController = TextEditingController();

  String dateText = "";
  TextEditingController dateController = TextEditingController();

  String hourText = "";
  TextEditingController hourController = TextEditingController();

  String totalDate = "";

  String temperatureText = "";
  TextEditingController temperatureController = TextEditingController();



  List<String> tipo = ["IN", "OUT"];


  String? _selectedType;
  String? _selectedCentre;

  String? _selectedCentreID;

  late FocusNode typeFocus;
  late FocusNode nameFocus;
  late FocusNode surnameFocus;
  late FocusNode centreFocus;
  late FocusNode dateFocus;
  late FocusNode hourFocus;
  late FocusNode temperatureFocus;
  late FocusNode confirmFocus;


  @override
  Widget build(BuildContext context) {
    final provider = Provider.of<MyProvider>(context);

    ComoGastoLocalizations? localizations = Localizations.of<
        ComoGastoLocalizations>(context, ComoGastoLocalizations);

    totalDate = formatoFechaApp(DateTime.now().toString(), localizations!.localeName);

    dateController.text = totalDate.substring(0, 10);
    hourController.text = totalDate.substring(11);

    return Scaffold(
        backgroundColor: Colors.white,

        appBar: MainAppBar(),

        body: Center(
            child: Padding(
              padding: const EdgeInsets.fromLTRB(20.0, 0.0, 20.0, 0.0),

              child: ListView(
                children: [
                  SubLabel(localizations.t('registerpage.titulo')),
                  SizedBox(height: 20.0,),
                  Container(
                    width: 300,
                    padding: EdgeInsets.symmetric(
                        vertical: 5, horizontal: 15),
                    decoration: BoxDecoration(
                      color: Color(0xffd3d3d3),
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
                              localizations.t('registerpage.centro'),
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
                  Container(
                    width: 300,
                    padding: EdgeInsets.symmetric(
                        vertical: 5, horizontal: 15),
                    decoration: BoxDecoration(
                      color: Color(0xffd3d3d3),
                    ),
                    child: DropdownButton<String>(

                      focusNode: typeFocus,
                      onChanged: (value) {
                        setState(() {
                          _selectedType = value;
                        });
                      },
                      value: _selectedType,

                      // Hide the default underline
                      underline: Container(
                        color: Colors.black,
                      ),
                      hint: Row(
                          mainAxisSize: MainAxisSize.max,
                          children: [
                            Text(
                              localizations.t('registerpage.tipo'),
                              style: TextStyle(color: Colors.black),
                            ),
                          ]),

                      isExpanded: true,

                      // The list of options
                      items: tipo
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
                          tipo
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
                    keyboardType: TextInputType.name,
                    textInputAction: TextInputAction.next,
                    focusNode: nameFocus,
                    onEditingComplete: () =>
                        requestFocus(context, surnameFocus),
                    controller: nameController,
                    decoration: InputDecoration(
                      labelText: localizations.t('registerpage.nombre'),
                      hintText: localizations.t('registerpage.hintnombre'),
                      fillColor: Color(0xffd3d3d3),
                      filled: true,
                    ),
                  ),
                  SizedBox(height: 20.0,),
                  TextFormField(
                    cursorColor: Colors.blueGrey,
                    keyboardType: TextInputType.name,
                    textInputAction: TextInputAction.next,
                    focusNode: surnameFocus,
                    onEditingComplete: () => requestFocus(context, centreFocus),
                    controller: surnameController,
                    decoration: InputDecoration(
                      labelText: localizations.t('registerpage.apellidos'),
                      hintText: localizations.t('registerpage.hintapellidos'),
                      fillColor: Color(0xffd3d3d3),
                      filled: true,
                    ),
                  ),
                  SizedBox(height: 20.0,),
                  TextFormField(
                    cursorColor: Colors.blueGrey,
                    keyboardType: TextInputType.datetime,
                    textInputAction: TextInputAction.next,
                    focusNode: dateFocus,
                    onEditingComplete: () =>
                        requestFocus(context, hourFocus),
                    controller: dateController,
                    decoration: InputDecoration(
                      labelText: localizations.t('registerpage.fecha'),
                      hintText: localizations.t('registerpage.hintfecha'),
                      fillColor: Color(0xffd3d3d3),
                      filled: true,
                    ),
                  ),
                  SizedBox(height: 20.0,),
                  TextFormField(
                    cursorColor: Colors.blueGrey,
                    keyboardType: TextInputType.datetime,
                    textInputAction: TextInputAction.next,
                    focusNode: hourFocus,
                    onEditingComplete: () =>
                        requestFocus(context, temperatureFocus),
                    controller: hourController,
                    decoration: InputDecoration(
                      labelText: localizations.t('registerpage.hora'),
                      hintText: localizations.t('registerpage.hinthora'),
                      fillColor: Color(0xffd3d3d3),
                      filled: true,
                    ),
                  ),
                  SizedBox(height: 20.0,),
                  TextFormField(
                    cursorColor: Colors.blueGrey,
                    keyboardType: TextInputType.number,
                    textInputAction: TextInputAction.next,
                    focusNode: temperatureFocus,
                    onEditingComplete: () =>
                        requestFocus(context, confirmFocus),
                    controller: temperatureController,
                    decoration: InputDecoration(
                      labelText: localizations.t('registerpage.temperatura'),
                      hintText: localizations.t('registerpage.hinttemperatura'),
                      fillColor: Color(0xffd3d3d3),
                      filled: true,
                    ),
                  ),
                  SizedBox(height: 40.0,),
                  TextButton(
                    focusNode: confirmFocus,
                    onPressed: () {
                      //SAVE VARIABLES
                      saveFormEntries();

                      //CHECK VALUES
                      int signal = checkResgisterValues(provider, localizations);

                      //SHOW DIALOG
                      signalControl(context, provider, signal);

                      //DO

                      if (signal == 0) {
                        for (int i = 0; i < provider.centresData.length; i++) {
                          if (provider.centresData[i]['name'].toString() ==
                              _selectedCentre.toString()) {
                            _selectedCentreID =
                                provider.centresData[i]['id'].toString();
                            break;
                          }
                        }

                        registerUser(provider, context, localizations.localeName);
                      }
                    },
                    style: TextButton.styleFrom(
                        primary: Colors.black,
                        backgroundColor: Color(0xff009688)
                    ),                    child: Text(localizations.t('registerpage.confirmar'),
                        style: TextStyle(fontSize: 16.0, color: Colors.white)),
                  ),
                  SizedBox(height: 10.0,),
                ],
              ),
            )
        )

    );
  }

  void saveFormEntries() {
    nameText = nameController.text;
    surnameText = surnameController.text;
    dateText = dateController.text;
    hourText = hourController.text;
    temperatureText = temperatureController.text;
    totalDate = dateText + " " + hourText;
  }

  int checkResgisterValues(MyProvider provider, ComoGastoLocalizations localizations) {
    /* SIGNALS:
    * 0: OK
    * 1: SOME EMPTY
    * 2: PERSON DOES NOT EXIST
    * 3: BAD DATE FORMAT
    * 4: BAD TEMPERATURE FORMAT
    * 5: INITIAL DATE AFTER FINAL DATE
    */

    if (_selectedType == null   || nameText.isEmpty || surnameText.isEmpty ||
        _selectedCentre == null || dateText.isEmpty || hourText.isEmpty    || temperatureText.isEmpty)
      return 1;

    if (checkUserName(provider, nameText, surnameText) == false) {
      return 2;
    }

    if (checkDate(totalDate, localizations.localeName) == false)
      return 3;


    if (checkTemperature(temperatureText, localizations.localeName) == false)
      return 4;

    //If all ok -> signal 0
    return 0;
  }

  void registerUser(MyProvider provider, BuildContext context,String language) {
    Register register = new Register(
        _selectedType,
        nameText,
        surnameText,
        provider.uuid,
        _selectedCentreID,
        totalDate,
        temperatureText);
    confirmar(context, provider, register);
    updateTextFields(language);
  }


  void updateTextFields(String language){

    nameController.clear();
    surnameController.clear();
    temperatureController.clear();

    totalDate = formatoFechaApp(DateTime.now().toString(), language);

    dateController.text = totalDate.substring(0, 10);
    hourController.text = totalDate.substring(11);

  }


  @override
  void initState() {
    super.initState();


    typeFocus = FocusNode();
    nameFocus = FocusNode();
    surnameFocus = FocusNode();
    centreFocus = FocusNode();
    dateFocus = FocusNode();
    hourFocus = FocusNode();
    temperatureFocus = FocusNode();
    confirmFocus = FocusNode();
  }

  @override
  void dispose() {
    super.dispose();

    typeFocus.dispose();
    nameFocus.dispose();
    surnameFocus.dispose();
    centreFocus.dispose();
    dateFocus.dispose();
    hourFocus.dispose();
    temperatureFocus.dispose();
    confirmFocus.dispose();
  }

}

