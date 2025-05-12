const buttons = document.querySelectorAll("button.like")
const spans=document.querySelectorAll("span.like-counter")
buttons.forEach((item,i)=>{
    item.addEventListener("click",function(){
        let likesCount = parseInt(spans[i].innerText)
        likesCount++
        spans[i].innerText=likesCount + " like(s)"
    })
})