#!/usr/bin/env node
// Blinks various LEDs
const Blynk = require('/usr/lib/node_modules/blynk-library');
const b = require('bonescript');
const util = require('util');

const LED1 = 'P9_14';
b.pinMode(LED1, b.OUTPUT);

const AUTH = 'ab16c0bd9123409abc4b55e5e70fb2cd';


var blynk = new Blynk.Blynk(AUTH);

var v11 = new blynk.VirtualPin(11);

v11.on('write', function(param) {
    console.log('V11:', param[0]);
    b.analogWrite(LED1, parseFloat(param));
});
