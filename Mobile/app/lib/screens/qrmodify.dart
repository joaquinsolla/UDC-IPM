import 'package:entryqr/provider/como_gasto_localizations.dart';
import 'package:entryqr/provider/databasepetition.dart';
import 'package:entryqr/provider/provider.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../common.dart';

class QRModify extends StatefulWidget {
  QRModify({Key? key}) : super(key: key);

  @override
  QRModifyState createState() => QRModifyState();
}

class QRModifyState extends State<QRModify> {

  String temperatureText = "";
  TextEditingController temperatureController = TextEditingController();

  String dateText = "";
  TextEditingController dateController = TextEditingController();

  String hourText = "";
  TextEditingController hourController = TextEditingController();

  String totalDate = "";


  List<String> tipo = ["IN", "OUT"];
  String? _selectedType;
  String? _selectedCentre;

  String? _selectedCentreID;


  late FocusNode typeFocus;
  late FocusNode centreFocus;
  late FocusNode dateFocus;
  late FocusNode hourFocus;
  late FocusNode temperatureFocus;
  late FocusNode confirmFocus;


  @override
  Widget build(BuildContext context) {
    final User arguments = ModalRoute
        .of(context)!
        .settings
        .arguments as User;


    final provider = Provider.of<MyProvider>(context);

    ComoGastoLocalizations? localizations = Localizations.of<
        ComoGastoLocalizations>(context, ComoGastoLocalizations);


    return Scaffold(
      backgroundColor: Colors.white,
      appBar: MainAppBar(),

      body: Padding(
        padding: const EdgeInsets.fromLTRB(20.0, 0.0, 20.0, 0.0),
        child: ListView(
          children: [
            SubLabel(localizations!.t('qr.titulo')),
            SizedBox(height: 70.0,),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Row(
                        children: [
                          Text(localizations.t('qr.nombre') + ":",
                            style: TextStyle(fontSize: 15.0,
                              fontWeight: FontWeight.bold),
                          ),
                          SizedBox(width: 19.0,),
                          Text(arguments.name,
                            style: TextStyle(fontSize: 15.0),
                          ),
                        ]
                    ),
                    SizedBox(height: 20.0,),
                    Row(
                      children: [
                        Text(localizations.t('qr.apellidos') + ":",
                          style: TextStyle(fontSize: 15.0,
                            fontWeight: FontWeight.bold),),
                        SizedBox(width: 10.0,),
                        Text(arguments.surname,
                          style: TextStyle(fontSize: 15.0),),
                      ],
                    ),
                    SizedBox(height: 20.0,),
                    Row(
                      children: [
                        Text(localizations.t('qr.uuid') + ": ",
                          style: TextStyle(fontSize: 15.0,
                            fontWeight: FontWeight.bold),),
                        SizedBox(width: 0.0,),
                        Text(arguments.uuid,
                          style: TextStyle(fontSize: 15.0),),
                      ],
                    ),
                  ],
                ),
              ],
            ),
            SizedBox(height: 30.0,),
            TextFormField(
              cursorColor: Colors.blueGrey,
              keyboardType: TextInputType.datetime,
              textInputAction: TextInputAction.next,
              focusNode: dateFocus,
              onEditingComplete: () => requestFocus(context, hourFocus),
              controller: dateController,
              decoration: InputDecoration(
                labelText: localizations.t('qr.fecha'),
                hintText: localizations.t('qr.hintfecha'),
                fillColor: Color(0xffd3d3d3),
                filled: true,
              ),
            ),
            SizedBox(height: 30.0,),
            TextFormField(
              cursorColor: Colors.blueGrey,
              keyboardType: TextInputType.datetime,
              textInputAction: TextInputAction.next,
              focusNode: hourFocus,
              onEditingComplete: () => requestFocus(context, typeFocus),
              controller: hourController,
              decoration: InputDecoration(
                labelText: localizations.t('qr.hora'),
                hintText: localizations.t('qr.hinthora'),
                fillColor: Color(0xffd3d3d3),
                filled: true,
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
                        localizations.t('qr.tipo'),
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
                        localizations.t('qr.centro'),
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
            SizedBox(
              height: 20.0,),
            TextFormField(
              cursorColor: Colors.blueGrey,
              keyboardType: TextInputType.number,
              textInputAction: TextInputAction.next,
              focusNode: temperatureFocus,
              onEditingComplete: () => requestFocus(context, confirmFocus),
              controller: temperatureController,
              decoration: InputDecoration(
                labelText: localizations.t('qr.temperatura'),
                hintText: localizations.t('qr.hinttemperatura'),
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
                int signal = checkQRModifyValues(localizations);

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

                  Register register = new Register(
                      _selectedType,
                      arguments.name,
                      arguments.surname,
                      arguments.uuid,
                      _selectedCentreID,
                      totalDate,
                      temperatureText);

                  confirmModifiedData(context, provider, register);
                }
              },
              style: TextButton.styleFrom(
                  primary: Colors.black,
                  backgroundColor: Color(0xff009688)
              ),              child: Text(localizations.t('qr.confirmar'),
                  style: TextStyle(fontSize: 16.0, color: Colors.white)),
            ),
            SizedBox(height: 10.0,), //
          ],
        ),
      ),

    );
  }

  void saveFormEntries() {
    dateText = dateController.text;
    hourText = hourController.text;
    totalDate = dateText + " " + hourText;
    temperatureText = temperatureController.text;
  }

  int checkQRModifyValues(ComoGastoLocalizations localizations) {
    /* SIGNALS:
    * 0: OK
    * 1: SOME EMPTY
    * 2: PERSON DOES NOT EXIST
    * 3: BAD DATE FORMAT
    * 4: BAD TEMPERATURE FORMAT
    * 5: INITIAL DATE AFTER FINAL DATE
    */

    if (dateText.isEmpty || hourText.isEmpty || _selectedType == null ||
        _selectedCentre == null || temperatureText.isEmpty)
      return 1;

    if (checkDate(totalDate, localizations.localeName) == false)
      return 3;

    if (checkTemperature(temperatureText, localizations.localeName) == false)
      return 4;

    //If all ok -> signal 0
    return 0;
  }


  @override
  void initState() {
    super.initState();


    typeFocus = FocusNode();
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
    centreFocus.dispose();
    dateFocus.dispose();
    hourFocus.dispose();
    temperatureFocus.dispose();
    confirmFocus.dispose();
  }

}

void confirmModifiedData(BuildContext context, MyProvider provider, Register register){
  confirmar(context, provider, register);
  Navigator.pushNamed(context, "/menucontroller"/*, (route) => false*/);
}