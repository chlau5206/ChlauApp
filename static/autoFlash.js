function reflash(){
    var seconds =6; 
    // countdown timer. took 6 because page takes approx 1 sec to load 
    
    var url="{{url_for('home')}}"; 
    // variable for index.html url 
    
    if (seconds <=0){ 
    // redirect to new url after counter  down. 
        window.location = url; 
    } else { 
        seconds--; 
        document.getElementById("pageInfo").innerHTML="Redirecting to Home Page after " 
        +seconds+" seconds." 
        setTimeout("redirect()", 1000) 
    } 
} 