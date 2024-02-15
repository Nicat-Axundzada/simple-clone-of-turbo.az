document.addEventListener("DOMContentLoaded", function () {
  const toggleBtnMarka = document.querySelector("#brand-filter");
  const toggleBtnModel = document.querySelector("#model-filter");
  const toggleBtnCity = document.querySelector("#city-filter");
  const toggleBtnCurrency = document.querySelector("#currency-filter");
  const toggleBtnBan = document.querySelector("#ban-filter");
  const modelFilterContentDiv = document.querySelector(
    ".filter-content-for-model"
  );
  const checkboxes = document.querySelectorAll('input[name="brand"]');
  let selectedMarkaBrand = "";
  let models = [];
  function toggleFilterDisplay(element, arrowIcon) {
    if (element.style.display === "none" || element.style.display === "") {
      element.style.display = "block";
      arrowIcon.classList.add("rotate");
    } else {
      element.style.display = "none";
      arrowIcon.classList.remove("rotate");
    }
  }

  checkboxes.forEach((checkbox) => {
    checkbox.addEventListener("click", () => {
      checkboxes.forEach((cb) => {
        if (cb !== checkbox && cb.checked) {
          cb.checked = false;
        }
      });
    });
  });

  toggleBtnMarka.addEventListener("click", (event) => {
    event.preventDefault();
    const element = document.querySelector(".filter-content");
    const arrowIcon = document.querySelector("#brand-filter .btn-arrow");
    toggleFilterDisplay(element, arrowIcon);
  });

  toggleBtnModel.addEventListener("click", (event) => {
    event.preventDefault();
    const element = document.querySelector(".filter-content-for-model");
    const arrowIcon = document.querySelector("#model-filter .btn-arrow");
    toggleFilterDisplay(element, arrowIcon);
  });

  toggleBtnCity.addEventListener("click", (event) => {
    event.preventDefault();
    const element = document.querySelector(".filter-content-for-city");
    const arrowIcon = document.querySelector("#city-filter .btn-arrow");
    toggleFilterDisplay(element, arrowIcon);
  });

  toggleBtnCurrency.addEventListener("click", (event) => {
    event.preventDefault();
    const element = document.querySelector(".filter-content-for-currency");
    const arrowIcon = document.querySelector("#currency-filter .btn-arrow");
    toggleFilterDisplay(element, arrowIcon);
  });

  toggleBtnBan.addEventListener("click", (event) => {
    event.preventDefault();
    const element = document.querySelector(".filter-content-for-ban");
    const arrowIcon = document.querySelector("#ban-filter .btn-arrow");
    toggleFilterDisplay(element, arrowIcon);
  });

  checkboxes.forEach((checkbox) => {
    checkbox.addEventListener("change", () => {
      if (checkbox.checked) {
        selectedMarkaBrand = checkbox.value;
      } else {
        selectedMarkaBrand = null;
      }
      modelFilterContentDiv.innerHTML = "";
      models = [];

      if (selectedMarkaBrand) {
        document.querySelector("#model-filter").disabled = false;
        content.models.forEach((model) => {
          if (
            !models.includes(model.model) &&
            model.brand == selectedMarkaBrand
          ) {
            models.push(model.model);
            modelFilterContentDiv.innerHTML += `
              <label class="custom-checkbox">
                ${model.model}
                <input type="checkbox" name="selected-model" value="${model.model}" />
                <span class="checkmark"></span>
              </label>
            `;
          }
        });
      }
    });
  });
});

//
const creditButton = document.querySelector(".credit-filter-btn");
const barterButton = document.querySelector(".barter-filter-btn");

creditButton.addEventListener("click", (event) => {
  creditButton.classList.toggle("selected");
  event.preventDefault();
});

barterButton.addEventListener("click", (event) => {
  barterButton.classList.toggle("selected");
  event.preventDefault();
});

const filterForm = document.getElementById("filter-form");

filterForm.addEventListener("submit", (event) => {
  event.preventDefault();

  // Get the selected state of the credit and barter buttons
  const isCreditSelected = creditButton.classList.contains("selected");
  const isBarterSelected = barterButton.classList.contains("selected");

  // Set the form input values based on the selected state of the buttons
  filterForm.querySelector('input[name="credit"]').value = isCreditSelected
    ? "true"
    : "false";
  filterForm.querySelector('input[name="barter"]').value = isBarterSelected
    ? "true"
    : "false";

  filterForm.submit();
});

const urlParams = new URLSearchParams(window.location.search);
const selectedMarka = urlParams.getAll("brand");
const markaCheckboxes = document.querySelectorAll('input[name="brand"]');

markaCheckboxes.forEach((checkbox) => {
  if (selectedMarka.includes(checkbox.value)) {
    checkbox.checked = true;
  }
});
let flag = false;
markaCheckboxes.forEach((checkbox) => {
  if (checkbox.checked) flag = true;
});
if (flag) {
  document.querySelector("#model-filter").disabled = false;
  markaCheckboxes.forEach((marka) => {
    if (marka.checked) brand = marka.value;
  });
  content.models.forEach((model) => {
    if (model.brand == brand)
      document.querySelector(".filter-content-for-model").innerHTML += `
  <label class="custom-checkbox">
  ${model.model}
  <input type="checkbox" name="selected-model" value="${model.model}" />
  <span class="checkmark"></span>
  </label>
  `;
  });

  const modelCheckboxes = document.querySelectorAll(
    "input[name='selected-model']"
  );
  const selectedModels = urlParams.getAll("selected-model");
  modelCheckboxes.forEach((checkbox) => {
    if (selectedModels.includes(checkbox.value)) {
      checkbox.checked = true;
    }
  });
}

const selectedCity = urlParams.getAll("selected-city");
const cityCheckboxes = document.querySelectorAll('input[name="selected-city"]');

cityCheckboxes.forEach((checkbox) => {
  if (selectedCity.includes(checkbox.value)) {
    checkbox.checked = true;
  }
});

const minPrice = Number(urlParams.get("min-price"));
if (minPrice)
  document.querySelector("input[name='min-price']").value = minPrice;

const maxPrice = Number(urlParams.get("max-price"));
if (maxPrice)
  document.querySelector("input[name='max-price']").value = maxPrice;

const selectedCurrency = urlParams.getAll("selected-currency");
const currencyCheckboxes = document.querySelectorAll(
  'input[name="selected-currency"]'
);

currencyCheckboxes.forEach((checkbox) => {
  if (selectedCurrency.includes(checkbox.value)) {
    checkbox.checked = true;
  }
});

const selectedBan = urlParams.getAll("selected-ban");
const banCheckboxes = document.querySelectorAll('input[name="selected-ban"]');

banCheckboxes.forEach((checkbox) => {
  if (selectedBan.includes(checkbox.value)) {
    checkbox.checked = true;
  }
});

const selectedCredit = urlParams.get("credit");

if (selectedCredit == "true") {
  creditButton.classList.toggle("selected");
}
const selectedBarter = urlParams.get("barter");
if (selectedBarter == "true") barterButton.classList.toggle("selected");
