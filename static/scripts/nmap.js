var socket = io('/nmap');

// prevent nmap from doing funky stuff and sending the controls offscreen
window.onload = function () {
  let nmbar = document.getElementById('nmapbar');
  let nmman = document.getElementById('frameableframe');
  nmman.style.width = ("calc(100vw - " + nmbar.clientWidth + 'px)');
}

var settingsMirror = CodeMirror(document.getElementById("framingframeday1"), {
  mode: "text",
  lineNumbers: true,
  lineWrapping: false,
  readOnly: true,
  theme: 'material-darker'
});
settingsMirror.setSize(null, '100%');

function callnmap() {
  socket.emit('nmapcall')
}

socket.on("message", function(data){
 console.log(data)
})

socket.on("nmapout", function(data){
  var doc = settingsMirror.getDoc();
  console.log(data)
  doc.replaceRange(data.output+ "\n", {line: Infinity})
})