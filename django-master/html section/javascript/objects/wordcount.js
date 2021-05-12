var text="hello hello hai how are";
//word count

var words=text.split(" ")
//[hello hello hai how are]====> now its an array of separate words

var obj={}
for(let word of words){
    if(word in obj){
        obj[word]+=1
    }
    else{
        obj[word]=1
    }
}
console.log(obj)