import 'package:entryqr/provider/como_gasto_localizations.dart';
import 'package:entryqr/provider/databasepetition.dart';
import 'package:entryqr/provider/provider.dart';
import 'package:entryqr/screens/attendancepage.dart';
import 'package:entryqr/screens/qrpage.dart';
import 'package:entryqr/screens/registerpage.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';



class MenuController extends StatefulWidget {

  @override
  MenuControllerState createState() => MenuControllerState();
}

class MenuControllerState extends State<MenuController> {


  int current_page = 1;

  static List<Widget> main_pages = <Widget>[
    RegisterPage(),
    QRPage(),
    AttendancePage(),
  ];

  void bottomTapped(int index) {
    setState(() {
      current_page = index;
    });
  }

  @override
  Widget build(BuildContext context) {
    final provider = Provider.of<MyProvider>(context);

    if (provider.centres.length == 0)
      listCentros(provider, context);

    if (provider.usersTotal.length == 0)
      listUser(provider, context);

    ComoGastoLocalizations? localizations = Localizations.of<
        ComoGastoLocalizations>(context, ComoGastoLocalizations);

    return Scaffold(


      body: Center(
        child: main_pages.elementAt(current_page),
      ),

      bottomNavigationBar: BottomNavigationBar(
        backgroundColor: Color(0xff009688),
        unselectedItemColor: Colors.black45,
        items: [
          BottomNavigationBarItem(
            icon: Icon(Icons.edit_rounded),
            //label: "     Registrar\nManualmente",),
            label: localizations!.t('menucontroller.registrar1') + "\n" +
                localizations.t('menucontroller.registrar2'),
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.qr_code_rounded),
            label: localizations.t('menucontroller.scanner') + "\n",
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.accessibility_rounded),
            label: localizations.t('menucontroller.asistencia') + "\n",
          ),
        ],
        currentIndex: current_page,
        selectedItemColor: Colors.white,
        onTap: bottomTapped,
      ),
    );
  }
}

