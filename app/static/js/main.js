// Float label headings in the contact form
$(document).ready(function() {
  $("body")
    .on("input propertychange", ".form-element", function(e) {
    $(this).toggleClass("form-element-filled", !!$(e.target).val());
  })
  .on("focus",".form-element",function(){
    $(this).addClass("form-element-focused");
  })
  .on("blur",".form-element",function(){
    $(this).removeClass("form-element-focused");
  });
});
