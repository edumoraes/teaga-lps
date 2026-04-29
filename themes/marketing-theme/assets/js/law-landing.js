document.addEventListener("DOMContentLoaded", function () {
  var form = document.querySelector("[data-law-form]");

  if (!form) {
    return;
  }

  form.addEventListener("submit", function (event) {
    event.preventDefault();

    if (!form.reportValidity()) {
      return;
    }

    var data = new FormData(form);
    var whatsappNumber = form.getAttribute("data-whatsapp-number") || "5592999999999";
    var fieldMap = [
      ["Nome", "full_name"],
      ["E-mail", "email"],
      ["WhatsApp", "phone"],
      ["Escritório", "office"],
      ["Cidade/Estado", "city_state"],
      ["Área de atuação", "practice_area"],
      ["Clientes/mês hoje", "current_clients"],
      ["Meta em 3 meses", "target_clients"],
      ["Já investe em anúncios", "has_ads"]
    ];

    var lines = [
      "Olá, quero minha consultoria estratégica gratuita para advogados.",
      "",
      "Meus dados:"
    ];

    fieldMap.forEach(function (field) {
      var value = String(data.get(field[1]) || "").trim();

      if (value) {
        lines.push(field[0] + ": " + value);
      }
    });

    lines.push("Autorizo contato por WhatsApp e e-mail: Sim");

    window.location.href = "https://wa.me/" + whatsappNumber + "?text=" + encodeURIComponent(lines.join("\n"));
  });
});
