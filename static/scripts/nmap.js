var socket = io('/nmap');

var helploaded = false
// prevent nmap from doing funky stuff and sending the controls offscreen
window.onload = function () {
  let nmbar = document.getElementById('nmapbar');
  let nmman = document.getElementById('frameableframe');
  nmman.style.width = ("calc(100vw - " + nmbar.clientWidth + 'px)');
  nmman.style.maxWidth = ("calc(100vw - " + nmbar.clientWidth + 'px)');
}

var settingsMirror = CodeMirror(document.getElementById("framingframeday1"), {
  mode: "text",
  lineNumbers: true,
  lineWrapping: false,
  readOnly: true,
  theme: 'material-darker'
});
settingsMirror.setSize(null, '100%');

function togglehelp(){
  console.log("help requested L:D")
  var element = document.getElementById("helpmodal");
  element.classList.toggle("is-active");
  if (!helploaded) {
    fetch('/static/help/nmap.html')
      .then(response => response.text())
      .then((data) => {
        document.getElementById("helptext").innerHTML= data
      })
    helploaded = true
  }
}

function callnmap() {
  settingsMirror.setValue("")
  settingsMirror.clearHistory();
  var options = {
    host: document.getElementById("nmhost").value,
    args: document.getElementById("nmoptions").value
  }
  socket.emit('nmapcall', options)

}

socket.on("message", function(data){
 console.log(data)
})

socket.on("nmapout", function(data){
  var doc = settingsMirror.getDoc();
  doc.replaceRange(data.output+ "\n", {line: Infinity})
})

