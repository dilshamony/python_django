//ABABC

var pattern="ABABAC"
var obj={}
for(let word of pattern){
    if(word in obj){
        console.log(`${word} is the first recursive character`)
        break;
    }
    else{
        obj[word]=1
    }
}