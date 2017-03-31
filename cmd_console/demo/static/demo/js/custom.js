$(function() {
  $(this).parent().find(".active").removeClass("active");
  var url = window.location.pathname;
  $('ul.nav a[href="'+ url +'"]').parent().addClass('active');
});
