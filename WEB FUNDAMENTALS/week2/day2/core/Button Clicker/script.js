function change(e){
    e.innerHTML="log out"

}
function remove(e){
    e.remove()
}
function increase(el){
    var span = document.getElementById(el)
    span.innerHTML++
    alert("the post was liked")
}
 