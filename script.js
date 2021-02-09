const { exists } = require('fs');

function in_array(element, list_elements) {
    var exist = false;
    for (var i = 0; i < list_elements.length; i++) {
        if (element == list_elements[i]) {
            exist = true
        }
    }
    return exist;
}

in_array(5, [1, 2, 3]);