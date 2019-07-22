$(function() {
  $( ".chore-block" ).click(function() {
    var form = $(this).data('form-id');
    var user = $(this).data('username');
    var id = '#' + form;

    $(id).submit();

  });
});