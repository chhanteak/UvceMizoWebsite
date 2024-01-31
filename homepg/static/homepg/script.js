$(document).ready(function () {
    // Add a click event listener to all "Read More" links
    $(".read-more-link").click(function (event) {
        // Prevent the default behavior of the link
        event.preventDefault();

        // Find the closest .thuziak element
        var thuziak = $(this).closest(".thuziak");

        // Toggle the visibility of .hidden-content within the .thuziak element
        thuziak.find(".hidden-content").toggle();

        // Toggle the link text between "Read More" and "Read Less"
        var link = $(this);
        if (link.text() === "Read More") {
            link.text("Read Less");
        } else {
            link.text("Read More");
        }
    });
});
$(document).ready(function(){
            $('.image1').slick({
                // Slick Carousel options and settings
            });
        });