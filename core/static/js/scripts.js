

$("#div_f1").click(function(){
   
    elem = document.querySelector('.check1')
    div = document.querySelector('#div_f1') 

   if ( $( elem ).prop( "checked" ) ){
  
    situacao = 'marcado'
    $(".check1").prop("checked", false)

    }else{
       
        situacao = 'desmarcado'
        $(".check1").prop("checked", true)
        $(".check3").prop("checked", false)
        $(".check2").prop("checked", false)
        $(".check4").prop("checked", false)
       
    }
    
    if (situacao =="marcado"){
        $("#div_f1").removeClass('marcado')
    }else if(situacao =="desmarcado"){
       
        $("#div_f1").addClass('marcado')
    }

    
 });

 //funcionario2

 

$("#div_f2").click(function(){
 
    elem = document.querySelector('.check2')
    div = document.querySelector('#div_f2') 

   if ( $( elem ).prop( "checked" ) ){
  
    situacao = 'marcado'
    $(".check2").prop("checked", false)

    }else{
       
        situacao = 'desmarcado'
        $(".check2").prop("checked", true)
        $(".check1").prop("checked", false)
        $(".check3").prop("checked", false)
        $(".check4").prop("checked", false)
       
    }
    
    if (situacao =="marcado"){
       
        $("#div_f2").removeClass('marcado')
    }else if(situacao =="desmarcado"){
        $("#div_f2").addClass('marcado')
    }

    
 });

  //funcionario2

 

$("#div_f3").click(function(){
 
    elem = document.querySelector('.check3')
    div = document.querySelector('#div_f3') 

   if ( $( elem ).prop( "checked" ) ){
  
    situacao = 'marcado'
    $(".check3").prop("checked", false)

    }else{
       
        situacao = 'desmarcado'
        $(".check3").prop("checked", true)
        $(".check2").prop("checked", false)
        $(".check1").prop("checked", false)
        $(".check4").prop("checked", false)
       
    }
    
    if (situacao =="marcado"){
        $("#div_f3").removeClass('marcado')
      
    }else if(situacao =="desmarcado"){
        $("#div_f3").addClass('marcado')
    }

});

 

$("#div_f4").click(function(){
 
    elem = document.querySelector('.check4')
    div = document.querySelector('#div_f4') 

   if ( $( elem ).prop( "checked" ) ){
  
    situacao = 'marcado'
    $(".check4").prop("checked", false)

    }else{
       
        situacao = 'desmarcado'
        $(".check4").prop("checked", true)
        $(".check3").prop("checked", false)
        $(".check2").prop("checked", false)
        $(".check1").prop("checked", false)
       
    }
    
    if (situacao =="marcado"){
        $("#div_f4").removeClass('marcado')
    }else if(situacao =="desmarcado"){
       
        $("#div_f4").addClass('marcado')
    }

});



$('#user-menu-button').click(function(){

    if( $('#showprofile').hasClass('d-none') ){
        $('#showprofile').removeClass('d-none')
        $('#showprofile').addClass('d-block')
}else{
    $('#showprofile').removeClass('d-block')
    $('#showprofile').addClass('d-none')
    
}

});



$('#openmobile').click(function(){

    if( $('#mobile-menu').hasClass('d-none') ){
        $('#mobile-menu').removeClass('d-none')
        $('#mobile-menu').addClass('d-block')
}else{
    $('#mobile-menu').removeClass('d-block')
    $('#mobile-menu').addClass('d-none')
    
}

});