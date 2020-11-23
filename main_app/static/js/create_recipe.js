const base_url = "http://127.0.0.1:5137"

let added_ingredients = {};

function addButtonToEachIngInFoodGroup(fg_id, classQuery) {
    let childrenOfBody;
    if (parseInt(ingredient_count[fg_id]) > 0) {
        childrenOfBody = document.querySelector(classQuery).firstElementChild.nextElementSibling.children;
    }
    for (let i = 0; i < parseInt(ingredient_count[fg_id]); i++) {
        let td = document.createElement('td');
        let add_btn = document.createElement('input');
        add_btn.type = 'button';
        add_btn.value = 'Add';
        td.appendChild(add_btn);
        childrenOfBody[i].appendChild(td);
    }
}

function getRowElementsForEachFoodGroup_Right(fg_id, tableElement) {
    if (parseInt(ingredient_count[fg_id]) > 0) {
        return tableElement.firstElementChild.nextElementSibling.children;
    }
}

function editEachButton(fg_id, childrenOfBody) {
    for (let i = 0; i < parseInt(ingredient_count[fg_id]); i++) {
        childrenOfBody[i].lastElementChild.firstElementChild.value = 'Select';
    }
}

// Add buttons for each ingredient when the page loads, left and right tables
document.addEventListener('DOMContentLoaded', (event) => {
    let fg_table_ids = ['.fruit_table', '.grain_table', '.vegetable_table', '.protein_table', '.dairy_table'];
    for (let x = 0; x < fg_table_ids.length; x++) {
        addButtonToEachIngInFoodGroup(x, fg_table_ids[x]);
    }
});

// Adding stuff to the recipe
document.querySelector('.accordion').addEventListener('click', (event) => {
    if (event.target.tagName.toLowerCase() === 'input') {
        let ingredient_row = event.target.parentElement.parentElement;
        let ingredient_name = ingredient_row.firstElementChild.innerText;
        
        // // If the ingredient isn't already added to the recipe
        if (!added_ingredients[ingredient_name]) {
            // If this is the first ingredient, display the table head
            if (isEmpty(added_ingredients)) {
                let recipe_head_row = document.querySelector('#recipe_head_row');
                recipe_head_row.style.display = 'table-row';
            }

            // add it to the local data structure
            added_ingredients[ingredient_name] = ingredient_name;

            // Get the table body
            let recipe_table_body = document.querySelector('#recipe_table_body');

            // Get the row, clone it, change button to del, add, alts, append to body
            let row_clone = ingredient_row.cloneNode(true);
            row_clone.lastElementChild.firstElementChild.value = 'Del';
            let td = document.createElement('td');
            let alt_btn = document.createElement('input');
            alt_btn.type = 'button';
            alt_btn.value = 'Alt';
            td.appendChild(alt_btn);
            row_clone.appendChild(td);
            recipe_table_body.appendChild(row_clone);
        }
    }
});

let row_to_be_changed = null;

// Removing stuff from the recipe or get alternatives
document.querySelector('#recipe_table_body').addEventListener('click', (event) => {
    if (event.target.value === 'Del') {
        clearRight();
        let row = event.target.parentElement.parentElement;
        let ingredient_name = row.firstElementChild.innerText;
        // Delete the ingredient from the object
        // Remove the li from the page
        delete added_ingredients[ingredient_name];
        row.remove();
        // Hide the row header if empty
        if (isEmpty(added_ingredients)) {
            let recipe_head_row = document.querySelector('#recipe_head_row');
            recipe_head_row.style.display = 'none';
        }
        console.log(added_ingredients);
    }
    else if (event.target.value === 'Alt') {
        // hide all tables that are currently shown
        clearRight();
        row_to_be_changed = event.target.parentElement.parentElement;
        let fg = row_to_be_changed.firstElementChild.nextElementSibling.innerText;
        // Get right side div
        let right_div = document.querySelector('#right_div');
        // display the one table
        if (fg === 'Fruit') {
            // clone the Fruit table
            let table_clone = document.querySelector('.fruit_table').cloneNode(true);
            // Get the table's, body's, rows
            let table_body_children = getRowElementsForEachFoodGroup_Right(0, table_clone);
            editEachButton(0, table_body_children);
            // Append it to right side div
            right_div.appendChild(table_clone);
        } else if (fg === 'Grain') {
            let table_clone = document.querySelector('.grain_table').cloneNode(true);
            let table_body_children = getRowElementsForEachFoodGroup_Right(1, table_clone);
            editEachButton(1, table_body_children);
            right_div.appendChild(table_clone);
        } else if (fg === 'Vegetable') {
            let table_clone = document.querySelector('.vegetable_table').cloneNode(true);
            let table_body_children = getRowElementsForEachFoodGroup_Right(2, table_clone);
            editEachButton(2, table_body_children);
            right_div.appendChild(table_clone);
        } else if (fg === 'Protein') {
            let table_clone = document.querySelector('.protein_table').cloneNode(true);
            let table_body_children = getRowElementsForEachFoodGroup_Right(3, table_clone);
            editEachButton(3, table_body_children);
            right_div.appendChild(table_clone);
        } else if (fg === 'Dairy') {
            let table_clone = document.querySelector('.dairy_table').cloneNode(true);
            let table_body_children = getRowElementsForEachFoodGroup_Right(4, table_clone);
            editEachButton(4, table_body_children);
            right_div.appendChild(table_clone);
        }
    }
});

document.querySelector('#right_div').addEventListener('click', (event) => {
    if (event.target.value === 'Select') {
        console.log(row_to_be_changed);

        // Get the row
        let selected_ingredient_children = event.target.parentElement.parentElement.children;
        
        // Get the children of the row_to_be_changed
        let children = row_to_be_changed.children

        // Update the added_ingredients
        delete added_ingredients[children[0].innerHTML];
        added_ingredients[selected_ingredient_children[0].innerText] = selected_ingredient_children[0].innerText;
        
        // Set the text in the row to be changed to the alternative ingredients text
        children[0].innerHTML = selected_ingredient_children[0].innerHTML;
        children[1].innerHTML = selected_ingredient_children[1].innerHTML;
        children[2].innerHTML = selected_ingredient_children[2].innerHTML;
        children[3].innerHTML = selected_ingredient_children[3].innerHTML;
        
        clearRight();

        console.log(added_ingredients);
    }
});
    
function clearRight() {
    row_to_be_changed = null;
    let right_div = document.querySelector('#right_div');
    right_div.innerHTML = "";
}

// Pressing the save recipe button
document.querySelector('#save_recipe_button').addEventListener('click', (event) => {
    // Check if the recipe name is valid
    let recipe_name_text = document.querySelector('#recipe_name_textbox').value;
    // If the text is empty, alert the user
    if (recipe_name_text == '') {
        alert('Enter a recipe name');
    }
    else {
        // If the recipe has ingredients, save it
        if (!isEmpty(added_ingredients)) {
            var reqBody = {}
            reqBody.recipe_name = recipe_name_text;
            reqBody.recipe_ingredients = added_ingredients;
            // Save the recipe to the database
            // Pass to the server through a POST request, the added_ingredients object
            var req = new XMLHttpRequest();
            req.open('POST', base_url + '/create');
            req.setRequestHeader('Content-Type', 'application/json');
            req.addEventListener('load', () => {
                var response = JSON.parse(req.responseText);
                if (response['message']) {
                    alert('Please limit recipe name to 16 characters');
                }
                else {
                    alert('Recipe added to database');
                }
            });
            req.send(JSON.stringify(reqBody));
        }
        else {
            // alert them that there's nothing there
            alert('Please add ingredients to your recipe');
        }
    }
});

function isEmpty(obj) {
    return Object.keys(obj).length === 0;
}