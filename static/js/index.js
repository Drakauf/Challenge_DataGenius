var pannier = {}

function add_product(e)
{
	$.ajax({
		type : "POST",
		url : "/add_product/",
		data: JSON.stringify(e.id, null, '\t'),
		contentType: 'application/json;charset=UTF-8',
		success: function(result) {
			if (result == "Error : 1")
				alert("Ce produit n'existe pas");
			else if (result == "Error : 2")
				alert("Ce produit n'est plus en stock");
			else
			{
				res = result.split(" ");
				$(".s_"+e.id)[0].innerHTML = res[1] + " en stock";
				if (e.id in pannier)
					pannier[e.id] += 1;
				else
					pannier[e.id] = 1;
			}
		}
	});
}

function validate_pannier()
{
	console.log($("#form_text").val()) 
	$("#form_text").val(JSON.stringify(pannier))
	console.log($("#form_text").val()) 
	$("#form").submit()
}
