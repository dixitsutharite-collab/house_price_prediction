async function predict(){

const data={

MedInc:parseFloat(document.getElementById("income").value),

HouseAge:parseFloat(document.getElementById("age").value),

AveRooms:parseFloat(document.getElementById("rooms").value),

Population:parseFloat(document.getElementById("population").value),

Latitude:parseFloat(document.getElementById("lat").value),

Longitude:parseFloat(document.getElementById("long").value)

};

const response=await fetch("/predict",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify(data)

});

const result=await response.json();

document.getElementById("result").innerHTML=
"Predicted Price : $" + result.predicted_price.toFixed(2)+" Lakhs";

}