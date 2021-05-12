function displayText(num){
    var input=document.querySelector(".displayBox");
    input.value+=num
}
function calculate(){
    var curval=document.querySelector(".displayBox").value
    var res=eval(curval)
    document.querySelector(".displayBox").value=res
}
function backspace(){
    var back=document.querySelector(".displayBox").value
    var res=back.slice(0,-1)
    document.querySelector(".displayBox").value=res
}