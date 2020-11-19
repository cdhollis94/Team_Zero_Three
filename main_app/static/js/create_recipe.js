const base_url = "http://127.0.0.1:5137/"

const added_ingredients = {};

// Adding stuff to the recipe
document.querySelector('.accordion').addEventListener('click', (event) => {
    if (event.target.tagName.toLowerCase() === 'span') {
        let ingredient_id = event.target.parentElement.querySelector('.ingredient_id_span').innerHTML;
        let ingredient_name = event.target.innerHTML;
        
        // If the ingredient isn't already added to the recipe, add it
        // to the added_ingredients object to keep track of the ingredient
        // and render it to the recipe_div
        if (!added_ingredients[ingredient_name]) {
            added_ingredients[ingredient_name] = ingredient_id;
            let recipe_div = document.querySelector('.recipe_div');
            // Create an li and put the ingredient in the recipe_div
            ingredient_li = document.createElement('li');
            ingredient_li.innerHTML = ingredient_name;
            recipe_div.appendChild(ingredient_li);
            console.log(added_ingredients);
        }
    }
});

// Removing stuff from the recipe
document.querySelector('.recipe_div').addEventListener('click', (event) => {
    if (event.target.tagName.toLowerCase() === 'li') {
        let ingredient_name = event.target.innerHTML;

        // Delete the ingredient from the object
        // Remove the li from the page
        delete added_ingredients[ingredient_name];
        event.target.remove();
        console.log(added_ingredients);
    }
});

// Pressing the save recipe button
document.querySelector('#save_recipe_button').addEventListener('click', (event) => {
    // Check if the recipe name is valid
    let recipe_name_text = document.querySelector('#recipe_name_textbox').value;
    // If the text is empty, alert the user
    if (recipe_name_text == '') {
        console.log('Put something fool');
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
            req.open('POST', base_url + 'create');
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
            console.log('You have nothing');
        }
    }
});

function isEmpty(obj) {
    return Object.keys(obj).length === 0;
}