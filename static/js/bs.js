$(document).on("submit", "#post-form", function (e) {
  e.preventDefault();
  $.ajax({
    type: "POST",
    url: '{% url "create" %}',
    data: {
      Type: $("#Type").val(),
      Note: $("#Note").val(),
      csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
      action: "post",
    },
    success: function (json) {
      document.getElementById("post-form").reset();
      $(".posts").prepend(
        '<div class="col-md-6">' +
          '<div class="row no-gutters border rounded overflow-hidden flex-md-row mb-4 shadow-sm h-md-250 position-relative">' +
          '<div class="col p-4 d-flex flex-column position-static">' +
          '<h3 class="mb-0">' +
          json.Type +
          "</h3>" +
          '<p class="mb-auto">' +
          json.Note +
          "</p>" +
          "</div>" +
          "</div>" +
          "</div>"
      );
    },
    error: function (xhr, errmsg, err) {
      $("#results").html(
        "<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " +
          errmsg +
          " <a href='#' class='close'>&times;</a></div>"
      ); // add the error to the dom
      console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
    },
  });
});
