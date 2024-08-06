function abc(){
    var a=document.getElementById("username").value;

    var c=document.getElementById("mail").value;
    var d=document.getElementById("password").value;
    var e=document.getElementById("c_password").value;

    if(a==''||c==''||d==''||e==''){
        alert("please respect all the column");
    }
    else if(d!=e){
        alert("your password is not match")
    }
    else if(d.length<6){
        alert("your password is max 8 character")
    }
   
    else if(d.length>=8){
        alert("please")
    }
   
}
function log(){
    document.getElementById("logins").style.display="block";
    document.getElementById("main").style.display="none";
}
const months=["Jan","Feb","Mar","Apl","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];

function dd(){
    var b=document.getElementById("name").value;
    document.getElementById("consumer-name").innerHTML="Consumer Name <hidden>---</hidden>: "+b;
    var c=document.getElementById("number").value;
    document.getElementById("consumer-number").innerHTML="Consumer Number : "+c;
    var d=document.getElementById("number").value;
    document.getElementById("receipt-number").innerHTML="Receipt Number <hidden>---</hidden>: "+d*4;
    //var e=document.getElementById("payment-date").value;
    let date=new Date();
    var d1=date.getDate();
    var d2=date.getFullYear();
      var dd=months[date.getMonth()];
    document.getElementById("date").innerHTML="Date : "+d1+" "+dd+" "+d2;
    var d=document.getElementById("number").value;
    document.getElementById("payment-date").innerHTML="Type : "+"Online Payment";
    var x=document.getElementById("units").value;
    document.getElementById("e-unit").innerHTML="Unit : "+x;
    var y=document.getElementById("price").value;
    document.getElementById("e-price").innerHTML=y+"/-";
    window.print();
    
}
function response(){
    var c=document.getElementById("price").value;
    document.getElementById("").innerHTML=c;
}
