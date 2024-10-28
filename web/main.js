// Main script

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
            // Next: isolate RGBs and color names
            text1 = rawTrainingText.replace(new RegExp('\(([A-Za-z]+)\)', 'g'), '');
            text2 = rawTrainingText.replace(new RegExp('rgb\(\d{1,3},\s*\d{1,3},\s*\d{1,3}\)\s+\(([^)]+)\)', 'g'), '');
            console.log(`${text1}:${text2}`);
        })
        .catch((error) => {
            console.error(error);
        });
}