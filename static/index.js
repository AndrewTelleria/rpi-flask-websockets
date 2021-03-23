$('document').ready(function(){
  var socket = io();
  socket.on('connect', function() {
    socket.emit('newdata');
    socket.emit('test');
  });
  socket.on('environment', function(msg){
    $('#temp_f').text(msg.temperature_f);
    $('#temp_c').text(msg.temperature_c);
    $('#humidity').text(msg.humidity);
    $('#co2').text(msg.co2);
    $('#tvoc').text(msg.tvoc);
  });
  socket.on('power', function(msg){
     $('#relay1').text(msg.relays.relay1);
     $('#relay2').text(msg.relays.relay2);
     $('#relay3').text(msg.relays.relay3);
     $('#relay4').text(msg.relays.relay4);
     $('#relay5').text(msg.relays.relay5);
     $('#relay6').text(msg.relays.relay6);
     $('#relay7').text(msg.relays.relay7);
     $('#relay8').text(msg.relays.relay8);
  });
  socket.on('my response', function(msg){
    $('#log').append('<p>Received: ' + msg.data + '</p>');
  });
  $('#relay1-on').click(function() {
    console.log("Relay 1 power ON")
    socket.emit('power override', {relay1: true})
  });
  $('#relay1-off').click(function() {
    console.log("Relay 1 power OFF")
    socket.emit('power override', {relay1: false})
  });
  $('#relay1-automate').click(function() {
    console.log("Relay 1 power automate")
    socket.emit('power automate', {relay1: 'automate'})
  });
  $('#relay2-on').click(function() {
    console.log("Relay 2 power ON")
    socket.emit('power override', {relay2: true})
  });
  $('#relay2-off').click(function() {
    console.log("Relay 2 power OFF")
    socket.emit('power override', {relay2: false})
  });
  $('#relay2-automate').click(function() {
    console.log("Relay 2 power automate")
    socket.emit('power automate', {relay2: 'automate'})
  });
  $('#relay3-on').click(function() {
    console.log("Relay 3 power ON")
    socket.emit('power override', {relay3: true})
  });
  $('#relay3-off').click(function() {
    console.log("Relay 3 power OFF")
    socket.emit('power override', {relay3: false})
  });
  $('#relay3-automate').click(function() {
    console.log("Relay 3 power automate")
    socket.emit('power automate', {relay3: 'automate'})
  });
  $('#relay4-on').click(function() {
    console.log("Relay 4 power ON")
    socket.emit('power override', {relay4: true})
  });
  $('#relay4-off').click(function() {
    console.log("Relay 4 power OFF")
    socket.emit('power override', {relay4: false})
  });
  $('#relay4-automate').click(function() {
    console.log("Relay 4 power automate")
    socket.emit('power automate', {relay4: 'automate'})
  });
  $('#relay5-on').click(function() {
    console.log("Relay 5 power ON")
    socket.emit('power override', {relay5: true})
  });
  $('#relay5-off').click(function() {
    console.log("Relay 5 power OFF")
    socket.emit('power override', {relay5: false})
  });
  $('#relay5-automate').click(function() {
    console.log("Relay 5 power automate")
    socket.emit('power automate', {relay5: 'automate'})
  });
  $('#relay6-on').click(function() {
    console.log("Relay 6 power ON")
    socket.emit('power override', {relay6: true})
  });
  $('#relay6-off').click(function() {
    console.log("Relay 6 power OFF")
    socket.emit('power override', {relay6: false})
  });
  $('#relay6-automate').click(function() {
    console.log("Relay 6 power automate")
    socket.emit('power automate', {relay6: 'automate'})
  });
  $('#relay7-on').click(function() {
    console.log("Relay 7 power ON")
    socket.emit('power override', {relay7: true})
  });
  $('#relay7-off').click(function() {
    console.log("Relay 7 power OFF")
    socket.emit('power override', {relay7: false})
  });
  $('#relay7-automate').click(function() {
    console.log("Relay 7 power automate")
    socket.emit('power automate', {relay7: 'automate'})
  });
  $('#relay8-on').click(function() {
    console.log("Relay 8 power ON")
    socket.emit('power override', {relay8: true})
  });
  $('#relay8-off').click(function() {
    console.log("Relay 8 power OFF")
    socket.emit('power override', {relay8: false})
  });
  $('#relay8-automate').click(function() {
    console.log("Relay 8 power automate")
    socket.emit('power automate', {relay8: 'automate'})
  });
});
