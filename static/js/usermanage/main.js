

function headerstats(){

    $.ajax({
    url: $("#headerapi_url").attr("href"),
    type: 'get',
    dataType: 'json',
    // contentType: 'application/json',
    success: function (data) {
        if (data){

        	$("#totalactive").html(data["total_active"]);
        	$("#totaltried").html(data["total_triedon"]);
        	$("#totalsignup").html(data["total_signup"]);
        }
        },        
	});
}


window.onload=function(){
	headerstats();
}