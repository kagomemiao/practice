function addLoadEvent(func){
    var oldload = window.onload;
    if(typeof window.onload != "function"){
        window.onload = func;
    }else{
        window.onload = function(){
            oldload();
            func();
        }
    }
}
function insertAfter(newElement, targetElement){
    var parent = targetElement.parentNode;
    if(parent.lastChild == targetElement){
        parent.appendChild(newElement);
    }else{
        parent.insertBefore(newElement,targetElement.nextSibling);
    }
}

function preparePlaceholder(){
    var img = document.createElement("img");
    img.id = "placeholder";
    img.src = "";
    img.alt = "my miku";

    var p = document.createElement("p");
    p.id = "description";
    
    var text = document.createTextNode("image desc");
    p.appendChild(text);
    
    var gallery = document.getElementById("gallery");
    
    insertAfter(img, gallery);
    insertAfter(p, img);
}
function gallery(){
    if(!document.getElementById||!document.getElementsByTagName) return false;
    var gallery = document.getElementById("gallery");
    var list = gallery.getElementsByTagName("a");
    for(var i = 0; i < list.length; i++){
        list[i].onclick= function(){
            return showPic(this) ? false : true;
        }
    }
}
function showPic(whichpic){
    if(!document.getElementById("placeholder")) return false;
    var source = whichpic.href ? whichpic.href : "";
    var placeholder = document.getElementById("placeholder");
    if(placeholder.nodeName != "IMG") return false;
    placeholder.src = source;

    var desc = document.getElementById("description"); 
    if(desc){
        var title = whichpic.title ? whichpic.title : "";   
        if(desc.firstChild.nodeType == 3){
            desc.firstChild.nodeValue = title;
        }

    }
    return true;
}

addLoadEvent(preparePlaceholder);
addLoadEvent(gallery);