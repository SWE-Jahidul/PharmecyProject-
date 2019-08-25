$(document).ready(function() {
    $("#addtolist").click(function(){
        
        csrf = $("input[name=csrfmiddlewaretoken]").val();
        console.log(csrf)
        mmid = $("#medicine").val()
        $.ajax({
            url: "../mdetails",
            method: "POST",
            data: { mid : mmid, csrfmiddlewaretoken: csrf },
            dataType: "json",
            success: function(result){
                console.log(result)
            }
        }); 
    })
});