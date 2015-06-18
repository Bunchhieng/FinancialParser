$(document).ready(function() {
   $.material.init();

   $('#ticker').autocomplete({
      source: function(request, response) {
         $.ajax({
            url: "/finance/api/get_ticker/",
            dataType: 'json',
            data: request,
            success: function(data) {
               response(data.map(function(value) {
                  return {
                     'label': value.name,
                     'symbol': value.symbol
                  };
               }));
            }
         });
      },
      minLength: 2,
      select: function(event, ui) {
         var url = ui.item.symbol;
         if (url != '#') {
            location.href = '/finance/' + url;
         }
      }
   });
});