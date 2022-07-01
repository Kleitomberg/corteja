let checkboxs = document.querySelectorAll('.checado')
const inputs = [...checkboxs]
for (let i of inputs){
    console.log(i.checked)
    i.addEventListener('change', function(){
        if(i.checked){
            console.log('checado')
            i.parentElement.classList.add('marcado')

            const notchecked = inputs.filter(input => input !== i)
            for(let i of notchecked){
                i.checked=false
                i.parentElement.classList.remove('marcado')
            }
        }
    })     
}

//abrir e fechar profile
$('#user-menu-button').click(function(){

    if( $('#showprofile').hasClass('d-none') ){
        $('#showprofile').removeClass('d-none')
        $('#showprofile').addClass('d-block')
}else{
    $('#showprofile').removeClass('d-block')
    $('#showprofile').addClass('d-none')
    
}

});

//fechar com clique esterno

$('#main').click(function(){

    if( $('#showprofile').hasClass('d-block') ){
        $('#showprofile').removeClass('d-block')
        $('#showprofile').addClass('d-none')
}else{
    $('#showprofile').removeClass('d-block')
    $('#showprofile').addClass('d-none')
    
}

});

$('#main').on('click', function (){
    $('#showprofile').removeClass('d-block')
    $('#showprofile').addClass('d-none')  
     
});

$(window).on('keyup',function(event){
    console.log('press')
    var code = event.keyCode;
    console.log(code)
    if(event.keyCode==27){
        
        //se clicou em esq fechar menu de perfil
        if( $('#showprofile').hasClass('d-block') ){
                $('#showprofile').removeClass('d-block')
                $('#showprofile').addClass('d-none')
        }else{
            $('#showprofile').removeClass('d-block')
            $('#showprofile').addClass('d-none')
            
        }
         //se clicou em esq fechar menu 
         if( $('#mobile-menu').hasClass('d-block') ){
            $('#mobile-menu').removeClass('d-block')
            $('#mobile-menu').addClass('d-none')
    }
}
});



//se clicou

$(document).on('click',function(event){

 //se clicou em esq fechar menu de perfil

    console.log("main")


});


//mobile

$('#openmobile').click(function(){

    if( $('#mobile-menu').hasClass('d-none') ){
        $('#mobile-menu').removeClass('d-none')
        $('#mobile-menu').addClass('d-block')
}else{
    $('#mobile-menu').removeClass('d-block')
    $('#mobile-menu').addClass('d-none')
    
}

});
