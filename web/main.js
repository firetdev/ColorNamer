// Main script

// Color object
function Clr(red, green, blue) {
    this.r = red;
    this.g = green;
    this.b = blue;
}

// Distance function
function distance(c1, c2) {
    const diff = {
        r: c2.r - c1.r,
        g: c2.g - c1.g,
        b: c2.b - c1.b
    };
    return Math.sqrt(diff.r * diff.r + diff.g * diff.g + diff.b * diff.b);
}

// Main function
function main() {
    const color = document.getElementById('colorInput').value;
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
            const rgbValues = text1.split('\n').map(line => line.trim()).filter(line => line.length > 0);
            const colors = text2.split('\n');
            let colorArray = [];
            for (let i = 0; i < rgbValues.length; i += 1) {
                const numbers = rgbValues[i].match(new RegExp('(\\d+)\\s*,\\s*(\\d+)\\s*,\\s*(\\d+)'));
                if (numbers)
                    colorArray.push(new Clr(numbers[1], numbers[2], numbers[3]));
            }
            const colorNumbers = color.match(new RegExp('(\\d+)\\s*,\\s*(\\d+)\\s*,\\s*(\\d+)'));
            const colorObject = new Clr(colorNumbers[1], colorNumbers[2], colorNumbers[3]);
            // Find closest centroid
            let prevDist = 10000000;
            let index = 0;
            for (let i = 0; i < colorArray.length; i += 1) {
                let dist = distance(colorObject, colorArray[i]);
                if (dist < prevDist) {
                    prevDist = dist;
                    index = i;
                }
            }
            // Output
            document.getElementById('clr').textContent = colors[index];
        })
        .catch((error) => {
            console.error(error);
        });
}