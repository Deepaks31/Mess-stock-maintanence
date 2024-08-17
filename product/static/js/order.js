
function addItemAndDisplay() {
    var itemName = document.getElementById("items").value;
    var quantity = document.getElementById("quantity").value;
    
    if (itemName && quantity) {
        var newRow = document.createElement("tr");

        var itemNameCol = document.createElement("td");
        itemNameCol.textContent = itemName;
        newRow.appendChild(itemNameCol);

        // Create column for quantity
        var quantityCol = document.createElement("td");
        quantityCol.textContent = quantity;
        newRow.appendChild(quantityCol);

        // Create remove button
        var removeButton = document.createElement("button");
        removeButton.textContent = "Remove";
        removeButton.classList.add("btn", "btn-danger");
        removeButton.onclick = function () {
            newRow.remove();
        };
        var actionCol = document.createElement("td");
        actionCol.appendChild(removeButton);
        newRow.appendChild(actionCol);

        // Append the new row to the saved items table
        document.getElementById("saved_items").appendChild(newRow);
        
        // Add hidden inputs with separate name attributes
        var hiddenInputName = document.createElement("input");
        hiddenInputName.type = "hidden";
        hiddenInputName.name = "item[]"; // Use [] to ensure it's submitted as an array
        hiddenInputName.value = itemName;
        newRow.appendChild(hiddenInputName);
        
        var hiddenInputQuantity = document.createElement("input");
        hiddenInputQuantity.type = "hidden";
        hiddenInputQuantity.name = "quantity[]"; // Use [] to ensure it's submitted as an array
        hiddenInputQuantity.value = quantity;
        newRow.appendChild(hiddenInputQuantity);
    }
}z

function submitForm() {
    var neededDate = document.getElementById("neededDate").value;

    var itemRows = document.querySelectorAll("#itemList tr");
    itemRows.forEach(function(row) {
        var hiddenInput = document.createElement("input");
        hiddenInput.type = "hidden";
        hiddenInput.name = "needed_date";
        hiddenInput.value = neededDate;
        row.appendChild(hiddenInput);
    });

    document.getElementById("orderForm").submit();
}z