import 'package:entryqr/provider/databasepetition.dart';
import 'package:flutter/material.dart';

import '../common.dart';
import '../qrscanner.dart';


class QRPage extends StatefulWidget {
  QRPage({Key? key}) : super(key: key);

  @override
  QRState createState() => QRState();
}

class QRState extends State<QRPage> {

  String uuidText = "";
  TextEditingController uuidController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: MainAppBar(),
      body: Center(
        child: QRScanner(),
        /*child: Column(
          children: [TextFormField(
            cursorColor: Colors.blueGrey,
            keyboardType: TextInputType.text,
            controller: uuidController,
            decoration: InputDecoration(
              labelText: "UUID",
              hintText: "Ex. ",
              fillColor: Color(0xffd3d3d3),
              filled: true,
            ),
          ),
            RaisedButton(
              onPressed: () {
                Navigator.pushNamed(context, "/qrform",
                    arguments: User(
                        "6bd49b45-d916-414d-a1e4-2f0ca04553a0",
                        "beatriz.marquez",
                        "Beatriz",
                        "Marquez",
                        "beatriz.marquez@example.com",
                        "971-779-685",
                        "false",
                        DateTime.now()));
              },
              color: Color(0xff009688),
              child: Text("Confirmar",
                  style: TextStyle(fontSize: 16.0, color: Colors.white)),
            ),
          ],
        ),*/
      ),
    );
  }
}


