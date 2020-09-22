var socket = io();
var currentView
var loadTerm = false
// Update cpu and memory usage
socket.on('getusg', data => {
  document.getElementById('cpumemlabel').innerHTML = data['cpuusage'] + "% cpu<br>" + data['memusage'] + "% mem"
});
function test() {
  socket.emit('getusg')
}
var interval = setInterval(test, 2000);
// End cpumem monitor

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
    document.getElementById(path).src = "/module/buffer"
    document.getElementById(path).src = "/module/terminal"
    loadTerm = true
  }
}

window.addEventListener("hashchange", function () {
  var path = (window.location.hash).substring(2)
  fetch("/module/getext").then(res => res.json()).then(json => {
    if (json[path]) {
      var myEle = document.getElementById(path);
      if (myEle) {
        var x = document.getElementById(currentView);
        x.style.display = "none";
        var y = document.getElementById(path);
        currentView = path
        y.style.display = "block"

      } else {
        prepareFrame(path, "/module/" + path, false)
        var x2 = document.getElementById(currentView);
        x2.style.display = "none";
        var y2 = document.getElementById(path);
        currentView = path
        y2.style.display = "block"

      }
    } else {
      console.log(false)
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

fetch("/module/getext").then(res => res.json()).then(json => {
  for (var i in json) {
    if (json[i].preload) {
      prepareFrame(i, "/module" + json[i].path, json[i].startpage)
    }
  }
})