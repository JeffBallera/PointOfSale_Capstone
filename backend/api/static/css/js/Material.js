// Selectors
const allSideMenu = document.querySelectorAll('#sidebar .side-menu.top li a');
const addMaterialButton = document.querySelector('#sidebar .side-menu li:nth-child(2) a');
const manageMaterialButton = document.querySelector('#sidebar .side-menu li:nth-child(3) a');
const addMaterialForm = document.getElementById('add-material-form');
const materialTable = document.getElementById('material-table');
const form = document.querySelector('#add-material-form form');
const materialTableBody = document.querySelector('#material-table tbody');
const editButton = document.getElementById('edit-button');
const manualAdjustForm = document.getElementById('manual-adjust-form');
const adjustForm = document.getElementById('adjust-form');
const selectItem = document.getElementById('select-item');
const currentReorderLevel = document.getElementById('current-stock-level');

// Initialize the view
function setInitialView() {
    addMaterialForm.classList.add('hidden');
    materialTable.classList.add('hidden');
    manualAdjustForm.classList.add('hidden');
}

// Handle form submission
form.addEventListener('submit', function (e) {
    e.preventDefault(); // Prevent the form from submitting in the traditional way

    // Get form values
    const itemName = document.getElementById('item-name').value;
    const itemDescription = document.getElementById('item-description').value;
    const itemCategory = document.getElementById('item-category').value;
    const unitOfMeasure = document.getElementById('unit-of-measure').value;
    const purchasePrice = document.getElementById('purchase-price').value;
    const reorderLevel = document.getElementById('reorder-level').value;

    // Create a new table row
    const newRow = document.createElement('tr');
    newRow.innerHTML = `
        <td>${itemName}</td>
        <td>${itemDescription}</td>
        <td>${itemCategory}</td>
        <td>${unitOfMeasure}</td>
        <td>${purchasePrice}</td>
        <td>${reorderLevel}</td>
    `;

    // Add the new row to the table
    materialTableBody.appendChild(newRow);

    // Clear the form fields
    form.reset();
});

// Toggle visibility based on button clicks
function toggleVisibility(buttonClicked) {
    switch (buttonClicked) {
        case 'addMaterial':
            addMaterialForm.classList.remove('hidden');
            materialTable.classList.add('hidden');
            manualAdjustForm.classList.add('hidden');
            break;
        case 'manageMaterial':
            addMaterialForm.classList.add('hidden');
            materialTable.classList.remove('hidden');
            manualAdjustForm.classList.add('hidden');
            break;
        default:
            addMaterialForm.classList.add('hidden');
            materialTable.classList.add('hidden');
            manualAdjustForm.classList.add('hidden');
            break;
    }
}

// Show the form when the "Add Material" button is clicked
addMaterialButton.addEventListener('click', function (e) {
    e.preventDefault(); // Prevent the default action of the anchor tag
    toggleVisibility('addMaterial');
});

// Show the table when the "Manage Material" button is clicked
manageMaterialButton.addEventListener('click', function (e) {
    e.preventDefault(); // Prevent the default action of the anchor tag
    toggleVisibility('manageMaterial');
});

// Hide the form and table when any other sidebar item is clicked
allSideMenu.forEach(item => {
    item.addEventListener('click', function (e) {
        const buttonClicked = e.target.closest('a').textContent.trim();

        // Check if the link should be handled by JavaScript or follow the default action
        if (buttonClicked === 'Add Material') {
            e.preventDefault();
            toggleVisibility('addMaterial');
        } else if (buttonClicked === 'Manage Material') {
            e.preventDefault();
            toggleVisibility('manageMaterial');
        }

        allSideMenu.forEach(i => {
            i.parentElement.classList.remove('active');
        });
        item.parentElement.classList.add('active');
    });
});

// TOGGLE SIDEBAR
const menuBar = document.querySelector('#content nav .bx.bx-menu');
const sidebar = document.getElementById('sidebar');

menuBar.addEventListener('click', function () {
    sidebar.classList.toggle('hide');
});

// SWITCH MODE
const switchMode = document.getElementById('switch-mode');

switchMode.addEventListener('change', function () {
    if (this.checked) {
        document.body.classList.add('dark');
    } else {
        document.body.classList.remove('dark');
    }
});

// Show the manual adjustment form when the "Edit" button is clicked
editButton.addEventListener('click', function () {
    manualAdjustForm.classList.toggle('hidden');

    // Populate the dropdown with items from the table
    populateItemDropdown();
});

// Function to populate the item dropdown with items from the table
function populateItemDropdown() {
    selectItem.innerHTML = ''; // Clear existing options

    const rows = materialTableBody.querySelectorAll('tr');
    rows.forEach(row => {
        const itemName = row.cells[0].textContent;
        const option = document.createElement('option');
        option.value = itemName;
        option.textContent = itemName;
        selectItem.appendChild(option);
    });
}

// Update the current reorder level when an item is selected
selectItem.addEventListener('change', function () {
    const selectedItem = selectItem.value;

    // Find the selected item in the table and update the reorder level display
    const rows = materialTableBody.querySelectorAll('tr');
    rows.forEach(row => {
        const itemName = row.cells[0].textContent;
        if (itemName === selectedItem) {
            currentReorderLevel.textContent = row.cells[5].textContent; // Update the reorder level display
        }
    });
});

// Handle form submission for reorder level adjustment
adjustForm.addEventListener('submit', function (e) {
    e.preventDefault(); // Prevent the form from submitting in the traditional way

    // Get form values
    const item = selectItem.value;
    const adjustedReorderLevel = parseFloat(document.getElementById('adjust-quantity').value);
    const reason = document.getElementById('reason-for-adjustment').value;

    // Update the reorder level in the table
    const rows = materialTableBody.querySelectorAll('tr');
    rows.forEach(row => {
        const itemName = row.cells[0].textContent;
        if (itemName === item) {
            row.cells[5].textContent = (adjustedReorderLevel % 1 === 0) ? adjustedReorderLevel : adjustedReorderLevel.toFixed(2); 
        }
    });

    // Clear the form fields
    adjustForm.reset();
    manualAdjustForm.classList.add('hidden'); // Hide the form after submission
});
