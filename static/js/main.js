$(document).ready(function () {
    // USE STRICT
    "use strict";

    $(".form-radio .radio-item").click(function(){
        //Spot switcher:
        $(this).parent().find(".radio-item input").prop("checked", false);
        $(this).find("input").prop("checked", true);
        //$(this).parent().find(".radio-item input").removeClass("checked");
        //$(this).addClass("checked");
    });

    // $('#time').parent().append('<ul class="list-item" id="newtime" name="time"></ul>');
    // $('#time option').each(function(){
    //     $('#newtime').append('<li value="' + $(this).val() + '">'+$(this).text()+'</li>');
    // });
    // $('#time').remove();
    // $('#newtime').attr('id', 'time');
    // $('#time li').first().addClass('init');
    // $("#time").on("click", ".init", function() {
    //     $(this).closest("#time").children('li:not(.init)').toggle();
    // });

    // $('#food').parent().append('<ul class="list-item" id="newfood" name="food"></ul>');
    // $('#food option').each(function(){
    //     $('#newfood').append('<li value="' + $(this).val() + '">'+$(this).text()+'</li>');
    // });
    // $('#food').remove();
    // $('#newfood').attr('id', 'food');
    // $('#food li').first().addClass('init');
    // $("#food").on("click", ".init", function() {
    //     $(this).closest("#food").children('li:not(.init)').toggle();
    // });
    
    // var allOptions = $("#time").children('li:not(.init)');
    // $("#time").on("click", "li:not(.init)", function() {
    //     allOptions.removeClass('selected');
    //     $(this).addClass('selected');
    //     $("#time").children('.init').html($(this).html());
    //     allOptions.toggle();
    // });

    // var FoodOptions = $("#food").children('li:not(.init)');
    // $("#food").on("click", "li:not(.init)", function() {
    //     FoodOptions.removeClass('selected');
    //     $(this).addClass('selected');
    //     $("#food").children('.init').html($(this).html());
    //     FoodOptions.toggle();
    // });
});

// Code goes here

// $(document).ready(function() {
//     var map = null;
//     var myMarker;
//     var myLatlng;
  
//     function initializeGMap(lat, lng) {
//       myLatlng = new google.maps.LatLng(lat, lng);
  
//       var myOptions = {
//         zoom: 12,
//         zoomControl: true,
//         center: myLatlng,
//         mapTypeId: google.maps.MapTypeId.ROADMAP
//       };
  
//       map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);
  
//       myMarker = new google.maps.Marker({
//         position: myLatlng
//       });
//       myMarker.setMap(map);
//     }
  
//     // Re-init map before show modal
//     $('#myModal').on('show.bs.modal', function(event) {
//       var button = $(event.relatedTarget);
//       initializeGMap(button.data('lat'), button.data('lng'));
//       $("#location-map").css("width", "100%");
//       $("#map_canvas").css("width", "100%");
//     });
  
//     // Trigger map resize event after modal shown
//     $('#myModal').on('shown.bs.modal', function() {
//       google.maps.event.trigger(map, "resize");
//       map.setCenter(myLatlng);
//     });
//   });





// var map;

// function initAutocomplete() {
//     map = new google.maps.Map(document.getElementById('map'), {
//         center: {lat: -33.8688, lng: 151.2195},
//         zoom: 13,
//         mapTypeId: google.maps.MapTypeId.ROADMAP
//     });

//     // ....
// }
// $(function() {
//     $('#myModal').on('shown', function () {
//         google.maps.event.trigger(map, "resize");
//     });
// });
