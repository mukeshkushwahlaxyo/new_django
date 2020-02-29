
function Delete(id,models,refreshTable,url,viewname){	
	$.ajaxSetup({ 
           beforeSend: function(xhr, settings) {
               if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                   // Only send the token to relative URLs i.e. locally.
                   xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
                     }
                 } 
            });
	$.ajax({
		type:'POST',
		url:url,
		data:{'id':id,'model':models,'viewname':viewname},
		success:function(data){
			$('#'+refreshTable).html(data)
		}
	})
}

// function getData(modelName,id){
// 	$.ajaxSetup({ 
//            beforeSend: function(xhr, settings) {
//                if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
//                    // Only send the token to relative URLs i.e. locally.
//                    xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
//                      }
//                  } 
//             });
// 	$.ajax({
// 		type:'POST',
// 		url:'employee/get_data',
// 		data:{'id':id,'model':modelName},
// 		success:function(data){
// 			return JSON.parse(data.data)
// 		}
// 	})
// }