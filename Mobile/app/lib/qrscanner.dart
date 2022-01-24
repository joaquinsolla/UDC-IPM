import 'package:entryqr/provider/databasepetition.dart';
import 'package:entryqr/provider/provider.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:qr_code_scanner/qr_code_scanner.dart';


class QRScanner extends StatefulWidget {

  @override
  QRScannerState createState() => QRScannerState();
}

class QRScannerState extends State<QRScanner> {

  final GlobalKey qrKey = GlobalKey(debugLabel: 'QR');
  late QRViewController controller;

  late List<String> dataQR;

  late MyProvider provider;

  @override
  Widget build(BuildContext context) {

    provider = Provider.of<MyProvider>(context);

    return Scaffold(
      body: Column(
        children: <Widget>[
          Expanded(
            flex: 5,
            child: Stack(
              children: [
                QRView(key: qrKey, onQRViewCreated: QRViewCreated),
                Center(
                  child: Container(
                    width: 275,
                    height: 275,
                    decoration: BoxDecoration(
                      border: Border.all(
                        color: Color(0xff0c6f59),
                        width: 4,
                      ),
                      borderRadius: BorderRadius.circular(12),
                    ),
                  ),
                )
              ],
            ),
          ),
        ],
      ),
    );
  }

  void QRViewCreated(QRViewController controller) {
    this.controller = controller;
    controller.scannedDataStream.listen((scanData) async {
      controller.pauseCamera();

      checkQRFormat(context, provider, scanData.code.toString());
    }
    );
  }

  @override
  void dispose() {
    controller.dispose();
    super.dispose();
  }

}

void checkQRFormat(BuildContext context, MyProvider provider, String s) {
  //{nombre},{apellidos},{uuid}
  List<String> splited = s.split(",");

  if (splited.length != 3) return;

  if (splited[0].substring(0, 1) != "{") return;
  if (splited[0].substring(splited[0].length - 1) != "}") return;

  if (splited[1].substring(0, 1) != "{") return;
  if (splited[1].substring(splited[1].length - 1) != "}") return;

  if (splited[2].substring(0, 1) != "{") return;
  if (splited[2].substring(splited[2].length - 1) != "}") return;


  buscar(context, provider, splited[2].substring(1, 37));
}

