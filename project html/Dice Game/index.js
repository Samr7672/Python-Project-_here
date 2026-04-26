var randomNumber1=Math.floor(Math.random()*6)+1;

var randomDice="dice"+randomNumber1+".png";

var randomImage1="images/"+randomDice

document.querySelectorAll("img")[0].setAttribute("src",randomImage1)

var randomNumber2=Math.floor(Math.random()*6)+1;

var randomDice="dice"+randomNumber2+".png";

var randomImage2="images/"+randomDice

document.querySelectorAll("img")[1].setAttribute("src",randomImage2)

if(randomNumber1>randomNumber2){
    document.querySelector("h1").innerHTML="first Dice win"

}
else if(randomNumber1<randomNumber2){
    document.querySelector("h1").innerHTML="Second DIce WIn"
}
else{
    document.querySelector("h1").innerHTML="DRAW"
}