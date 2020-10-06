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