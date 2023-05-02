// Select all the accordion headers
const accordionHeaders = document.querySelectorAll(".accordion");

accordionHeaders.forEach(function(header) {
  header.addEventListener("click", function() {
    const accordionBody = this.nextElementSibling;
    
    if (accordionBody.classList.contains("active")) {
      accordionBody.classList.remove("active");
      accordionBody.setAttribute("aria-hidden", "true");
      this.setAttribute("aria-expanded", "false");
    } else {
      accordionBody.classList.add("active");
      accordionBody.setAttribute("aria-hidden", "false");
      this.setAttribute("aria-expanded", "true");
    }
  });
});