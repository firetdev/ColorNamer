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
        })
        .catch((error) => {
            console.error(error);
        });
    let trainingTextNoSpaces = rawTrainingText.replace(new RegExp(' [^ \n]', 'g'), '');
    let text1 = '';  // Just the rgb
    let text2 = '';  // Just the color names
    text1 = rawTrainingText.replace(new RegExp('(red|orange|yellow|green|blue|purple|pink)', 'gi'), '');
    text2 = rawTrainingText.replace(new RegExp('rgb\(\d{1,3},\d{1,3},\d{1,3}\)', 'gi'), '');
}

document.getElementById('button').addEventListener('onclick', (e) => {
    main();
});