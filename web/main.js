// Main script

// Color object
function Clr(red, green, blue) {
    this.r = red;
    this.g = green;
    this.b = blue;
}

// Distance function
function distance

// Main function
function main() {
    let color = document.getElementById('colorInput').value;
    let rawTrainingText = '';
    fetch('getTraining.php')
        .then((response) => {
            if (!response.ok) {
                throw new Error(`Error. Status: ${response.status}`);
            }
            return response.text();
        })
        .then((data) => {
            rawTrainingText = data;
            let text1 = '';  // Just the rgb
            let text2 = '';  // Just the color names
            text1 = rawTrainingText.replace(new RegExp('([A-Za-z]+)', 'g'), '');
            text2 = rawTrainingText.replace(new RegExp('\\d{1,3}, \\d{1,3}, \\d{1,3}', 'g'), '');
            let rgbValues = text1.split('\n');
            let colors = text2.split('\n');
            let colorArray = [];
            for (let i = 0; i < rgbValues.length; i += 1) {
                let numbers = rgbValues[i].match(new RegExp('(\\d{1-3},)', 'g'));
                colorArray.push(new Clr(numbers[0], numbers[1], numbers[2]));
            }
        })
        .catch((error) => {
            console.error(error);
        });
}