// load whatever content the workspace currently has
fetch("/helper/getwkspmods/" + "testspace1") .then(response => response.text()).then((data) => {
  wsmods = data.split(',')
  for (mod in wsmods){
    document.getElementById('loadingload').innerHTML 
    += '<article class=\"message\"><div class=\"message-header section-toggle\" onclick="toggleview(\'' 
    + wsmods[mod] +'-toggle\')\"><p>' 
    + wsmods[mod]+'<p></div><div class=\"message-body\"  style=\"display: none;\" id=\"' 
    + wsmods[mod]+'-toggle\"></div></article>'
}})

function toggleview(target){

  if (!target){
  parent.bulmaToast.toast({ message: "Tried toggling null", position: "bottom-left", type: "is-warning" });
  return
  }
  targetele = document.getElementById(target)
  if (!targetele){
    parent.bulmaToast.toast({ message: "Tried toggling unknown element", position: "bottom-left", type: "is-warning" });
    return
  }

  if (targetele.style.display === "none") {
    targetele.style.display = "block";
  } else {
    targetele.style.display = "none";
  }
}