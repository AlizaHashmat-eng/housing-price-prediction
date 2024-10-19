// Wait for the DOM to fully load before adding event listeners
document.addEventListener("DOMContentLoaded", function () {

    // Get the form and the output div
    const form = document.getElementById("price-estimation-form");
    const estimatedPriceDiv = document.getElementById("estimated-price");

    // Add an event listener for form submission
    form.addEventListener("submit", function (event) {
        event.preventDefault(); // Prevent default form submission

        // Get the values from the form inputs
        const area = parseFloat(document.getElementById("area").value);
        const bedrooms = parseInt(document.getElementById("bedrooms").value);
        const bathrooms = parseInt(document.getElementById("bathrooms").value);
        const location = document.getElementById("location").value;
        const year = parseInt(document.getElementById("year").value);
        const garage = document.getElementById("garage").value;

        // Simple price estimation logic (this can be improved)
        let basePrice = area * 100; // Base price based on area
        basePrice += bedrooms * 5000; // Add price for bedrooms
        basePrice += bathrooms * 3000; // Add price for bathrooms

        // Modify price based on location
        if (location === "City Center") {
            basePrice *= 1.5;
        } else if (location === "Suburb") {
            basePrice *= 1.2;
        }

        // Add a value for the garage
        if (garage === "yes") {
            basePrice += 10000;
        }

        // Adjust price for the age of the house (newer houses are more expensive)
        const currentYear = new Date().getFullYear();
        const houseAge = currentYear - year;
        if (houseAge < 10) {
            basePrice *= 1.1; // 10% increase for newer houses
        } else if (houseAge > 50) {
            basePrice *= 0.8; // 20% decrease for older houses
        }

        // Display the estimated price
        estimatedPriceDiv.textContent = `Estimated Price: $${basePrice.toFixed(2)}`;
    });

});
