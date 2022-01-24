import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:yaml/yaml.dart';

class ComoGastoLocalizations{

  final String localeName;


  ComoGastoLocalizations(this.localeName);

  static const LocalizationsDelegate<ComoGastoLocalizations> delegate = _ComoGastoLocalizationsDelegate();

  YamlMap? translations;

  Future load() async{
    String yamlString = await rootBundle.loadString('languages/${localeName}.yml');
    translations = loadYaml(yamlString);
  }

  dynamic t(String key){
    try{
      var keys = key.split(".");
      dynamic translated = translations;
      keys.forEach((k) => translated = translated[k]);

      if (translated == null){
        return "Key not found: $key";
      }

      return translated;

    } catch (e) {
      return "Key not found: $key";
    }

  }

}

class _ComoGastoLocalizationsDelegate extends LocalizationsDelegate<ComoGastoLocalizations> {

  const _ComoGastoLocalizationsDelegate();

  //Soportados
  @override
  bool isSupported(Locale locale) {
    return ['es', 'en'].contains(locale.languageCode);
  }

  @override
  Future<ComoGastoLocalizations> load(Locale locale) async{
    var t = ComoGastoLocalizations(locale.languageCode);
    await t.load();
    return t;
  }

  @override
  bool shouldReload(covariant LocalizationsDelegate<ComoGastoLocalizations> old) {
    return false;
  }

}