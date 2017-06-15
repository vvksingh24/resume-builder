	$(function() {
		$(".inline .{{ eqformset.prefix }}").formset({
		prefix: "{{ .eqformset.prefix }}",
		})
		$(".{{ skillformset.prefix }}").formset({
		prefix: "{{ skillformset.prefix }}",
		})
		$(".{{ achieveformset.prefix }}").formset({
		prefix: "{{ archieveformset.prefix }}",
		})
	})


// $('#addbutton').click(function(){
// 	$('#addbutton').prefix: "{{ eqformset.prefix }}",
// })