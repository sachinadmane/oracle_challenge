jQuery(document).ready(function($){

    var table_body=($("#recipe-table > tbody > tr").length);

    if(table_body>0){

        $("#search").show();
    } else {
         $("#search").hide();
    }

    var $rows = $('#recipe-table tbody tr');

$('#search').keyup(function() {
    var val = $.trim($(this).val()).replace(/ +/g, ' ').toLowerCase();

    $rows.show().filter(function() {
        var text = $(this).text().replace(/\s+/g, ' ').toLowerCase();
        return !~text.indexOf(val);
    }).hide();
});


});
