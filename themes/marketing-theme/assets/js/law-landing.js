document.addEventListener("DOMContentLoaded", function () {
  document.body.classList.add("is-js");

  var faqItems = document.querySelectorAll(".law-lp-faq-item");
  var revealItems = document.querySelectorAll("[data-reveal]");

  faqItems.forEach(function (item) {
    var button = item.querySelector(".law-lp-faq-question");

    if (!button) {
      return;
    }

    button.addEventListener("click", function () {
      var isOpen = item.classList.contains("is-open");

      faqItems.forEach(function (currentItem) {
        var currentButton = currentItem.querySelector(".law-lp-faq-question");

        currentItem.classList.remove("is-open");

        if (currentButton) {
          currentButton.setAttribute("aria-expanded", "false");
        }
      });

      if (!isOpen) {
        item.classList.add("is-open");
        button.setAttribute("aria-expanded", "true");
      }
    });
  });

  if (!("IntersectionObserver" in window)) {
    revealItems.forEach(function (item) {
      item.classList.add("is-visible");
    });

    return;
  }

  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12 });

  revealItems.forEach(function (item) {
    observer.observe(item);
  });
});
