// // Object to store selected filter values
// let selectedFilters = {
//   marka: [],
//   model: [],
//   city: [],
//   currency: [],
//   ban: [],
// };

// // Function to update selected filters
// function updateSelectedFilters() {
//   // Clear selected values
//   Object.keys(selectedFilters).forEach((key) => {
//     selectedFilters[key] = [];
//   });

//   // Update selected values for marka filter
//   document
//     .querySelectorAll('input[name="selected-marka"]:checked')
//     .forEach((checkbox) => {
//       selectedFilters.marka.push(checkbox.value);
//     });

//   // Update selected values for model filter
//   document
//     .querySelectorAll('input[name="selected-model"]:checked')
//     .forEach((checkbox) => {
//       selectedFilters.model.push(checkbox.value);
//     });

//   // Update selected values for city filter
//   document
//     .querySelectorAll('input[name="selected-city"]:checked')
//     .forEach((checkbox) => {
//       selectedFilters.city.push(checkbox.value);
//     });

//   // Update selected values for currency filter
//   document
//     .querySelectorAll('input[name="selected-currency"]:checked')
//     .forEach((checkbox) => {
//       selectedFilters.currency.push(checkbox.value);
//     });

//   // Update selected values for ban filter
//   document
//     .querySelectorAll('input[name="selected-ban"]:checked')
//     .forEach((checkbox) => {
//       selectedFilters.ban.push(checkbox.value);
//     });

//   console.log(selectedFilters);
// }

// // Event listeners to update selected filters when checkboxes are clicked
// document
//   .querySelectorAll('input[name="selected-marka"]')
//   .forEach((checkbox) => {
//     checkbox.addEventListener("change", updateSelectedFilters);
//   });

// document
//   .querySelectorAll('input[name="selected-model"]')
//   .forEach((checkbox) => {
//     checkbox.addEventListener("change", updateSelectedFilters);
//   });

// document.querySelectorAll('input[name="selected-city"]').forEach((checkbox) => {
//   checkbox.addEventListener("change", updateSelectedFilters);
// });

// document
//   .querySelectorAll('input[name="selected-currency"]')
//   .forEach((checkbox) => {
//     checkbox.addEventListener("change", updateSelectedFilters);
//   });

// document.querySelectorAll('input[name="selected-ban"]').forEach((checkbox) => {
//   checkbox.addEventListener("change", updateSelectedFilters);
// });

// // Event listener for the "Show" button to display selected filters
// let showBtn = document.querySelector(".show-btn");
// showBtn.addEventListener("click", () => {
//   console.log(selectedFilters);
//   // Call a function here to filter the content based on the selected filters
// });
