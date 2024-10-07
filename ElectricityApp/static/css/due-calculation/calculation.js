function abc(){
    var units, unit;
    units=document.getElementById("units").value;
    unit=units;
   if(unit<=100){
    document.getElementById("acm").innerHTML=(unit*0);
    }
    else if(unit<=200){aa
        document.getElementById("acm").innerHTML=Math.round((100*0)+(unit-100)*2.250);
      
    }
    else if(unit<=400){
        document.getElementById("acm").innerHTML=Math.round((100*0)+(100*2.25)+(unit-200)*4.50);
    }
    else if(unit<=500){
        document.getElementById("acm").innerHTML=Math.round((100*0)+(100*2.25)+(200*4.50)+(unit-400)*6);
    }
    else if(unit<=600){
        document.getElementById("acm").innerHTML=Math.round((100*0)+(300*4.50)+(100*6)+(unit-500)*8);
    }
    else if(unit<=800){
       document.getElementById("acm").innerHTML=Math.round((100*0)+(300*4.50)+(100*6)+(100*8)+(unit-600)*9);
    }
    else if(unit<=1000){
        document.getElementById("acm").innerHTML=Math.round((100*0)+(300*4.50)+(100*6)+(100*8)+(200*9)+(unit-800)*10);
    }
    else if(unit>1000){
        document.getElementById("acm").innerHTML=Math.round((100*0)+(300*4.50)+(100*6)+(100*8)+(200*9)+(200*10)+(unit-1000)*11);
    }
    document.getElementById("hide").style.display="none";
    document.getElementById("con-pay").style.display="block";
    
}
