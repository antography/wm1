var socket = io();
var notify = io('/notify');
var wscommand = io('/wscommand');
var currentView
var workspace
var loadTerm = false

socket.on("update", data => {
  state = data
  document.getElementById('cpumemlabel').innerHTML = data['cpuusage'] + "% cpu<br>" + data['memusage'] + "% mem"
  document.getElementById('revshell_status').innerHTML = "Revshell status: " + data.revshell.status
});

socket.emit("update")
var interval = setInterval(() => socket.emit("update"), 1000);

notify.on("message", function(data){
  bulmaToast.toast({ message: data, position: "bottom-left", type: "is-info" });
})

window.onload = function () {
  window.location.hash = "/dashboard"
  let sidebar = document.getElementById('sidebar');
  let wsman = document.getElementById('wsman');
  wsman.style.width = sidebar.clientWidth + 'px'
}

function setterm() {
  if (!loadTerm) {
    var path = "terminal"
    document.getElementById(path).src = "/module/terminal"
    document.getElementById(path).src = "/gimme-a-momment"
    document.getElementById(path).src = "/module/terminal"
    loadTerm = true
  }
}

window.addEventListener("hashchange", function () {
  var path = (window.location.hash).substring(2)
  fetch("/helper/getext").then(res => res.json()).then(json => {
    if (json[path]) {
      var myEle = document.getElementById(path);
      if (!myEle) {
        prepareFrame(path, "/module/" + path, false)
      }
      var x2 = document.getElementById(currentView);
      x2.style.display = "none";
      var y2 = document.getElementById(path);
      currentView = path
      y2.style.display = "block"
      document.title = "W+M1 | " + json[path]['title']

    } else {
      bulmaToast.toast({ message: "Invalid path: " + path, position: "bottom-left", type: "is-danger" });
    }
  })
});

function prepareFrame(frameID, src, isDefault) {
  var style
  var classes
  if (isDefault) {
    style = "width:100%;height:calc(100vh - 3.25rem);";
    classes = "currentView"
    currentView = frameID
  } else {
    style = "width:100%;height:calc(100vh - 3.25rem); display: none";
  }
  var ifrm = document.createElement("iframe");
  if (frameID == "terminal") {
    ifrm.setAttribute("src", "");
  } else {
    ifrm.setAttribute("src", src);
  }

  ifrm.style = style
  ifrm.id = frameID
  ifrm.classList = classes

  document.getElementById("framingframe").appendChild(ifrm);
}

function togglemanage(){
  var element = document.getElementById("managemodal");
  element.classList.toggle("is-active");
}

fetch("/helper/getext").then(res => res.json()).then(json => {
  for (var i in json) {
    if (json[i].preload == 'true') {
      prepareFrame(i, "/module" + json[i].path, (json[i].startpage == "true"))
    }
  }
})

fetch("/helper/getactwksp").then(response => response.text())
.then((data) => {
  document.getElementById("wsman").innerHTML= data
  document.getElementById("workspacename").value= data
  workspace = data
})

function setactwksp(){
  reqwksp = document.getElementById("workspacename").value
  wscommand.emit("setwksp", reqwksp)
}

function addactwksp(){
  reqwksp = document.getElementById("workspacename").value
  wscommand.emit("addwksp", reqwksp)
}

wscommand.on('reloadws', () => {
  setTimeout(location.reload.bind(location), 1000);
});