// Select all the dropdown headers
const dropdownHeaders = document.querySelectorAll("a.dropdown");

dropdownHeaders.forEach(function(header) {
  header.addEventListener("click", function() {
  	// this.preventDefault();
    const menuBody = this.nextElementSibling;
    
    if (menuBody.classList.contains("active")) {
      menuBody.classList.remove("active");
      menuBody.setAttribute("aria-hidden", "true");
      this.setAttribute("aria-expanded", "false");
    } else {
      menuBody.classList.add("active");
      menuBody.setAttribute("aria-hidden", "false");
      this.setAttribute("aria-expanded", "true");
    }
  });
});

const mobileNavDisplay = document.querySelector(".mobile-nav-toggle");

mobileNavDisplay.addEventListener("click", function() {
	const menuBody = this.nextElementSibling;

	if (menuBody.classList.contains("active")) {
	  menuBody.classList.remove("active");
	  menuBody.setAttribute("aria-hidden", "true");
	  this.setAttribute("aria-expanded", "false");
	} else {
	  menuBody.classList.add("active");
	  menuBody.setAttribute("aria-hidden", "false");
	  this.setAttribute("aria-expanded", "true");
	}
});