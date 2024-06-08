function addItemAndDisplay() {
    var itemName = document.getElementById("item").value;
    var quantity = document.getElementById("quantity").value;
    
    if (itemName && quantity) {
        // Create a new row for the saved items table
        var newRow = document.createElement("tr");

        // Create columns for item name and quantity
        var itemNameCol = document.createElement("td");
        itemNameCol.textContent = itemName;
        newRow.appendChild(itemNameCol);

        var quantityCol = document.createElement("td");
        quantityCol.textContent = quantity;
        newRow.appendChild(quantityCol);

        // Create a remove button
        var removeButton = document.createElement("button");
        removeButton.textContent = "Remove";
        removeButton.classList.add("btn", "btn-danger");
        removeButton.onclick = function () {
            // Remove the corresponding row when the remove button is clicked
            newRow.remove();
        };
        var actionCol = document.createElement("td");
        actionCol.appendChild(removeButton);
        newRow.appendChild(actionCol);

        // Append the new row to the saved items table
        document.getElementById("savedItemList").appendChild(newRow);
    }
}
