const darkMode = document.querySelector('.dark-mode');

darkMode.addEventListener('click', () => {
    document.body.classList.toggle('dark-mode-variables');
    darkMode.querySelector('span:nth-child(1)').classList.toggle('active');
    darkMode.querySelector('span:nth-child(2)').classList.toggle('active');
})

const baseColorDiv = document.querySelector('#base_color'); // #word_color > input
const baseColorInput = document.querySelector('#base_color > input');
const saveButton = document.querySelector('.save-button');

const wordColorDiv = document.querySelector('#word_color'); // #word_color > input
const wordColorInput = document.querySelector('#word_color > input');

const baseLuminationInput = document.querySelector('#baseLumination');
const wordLuminationInput = document.querySelector('#wordLumination');
const timeInput = document.querySelector('#time');
const ssidInput = document.querySelector('#ssid');
const passwordInput = document.querySelector('#password');



baseColorInput.addEventListener('input', () => {
    baseColorDiv.style.backgroundColor = baseColorInput.value;
});


wordColorInput.addEventListener('input', () => {
    wordColorDiv.style.backgroundColor = wordColorInput.value;
});

saveButton.addEventListener('click', () => {
    
    //also safe it as a cookie here?

    console.log({
        baseColor: baseColorInput.value,
        wordColor: wordColorInput.value,
        baseLumination: baseLuminationInput.value,
        wordLumination: wordLuminationInput.value,
        time: timeInput.value,
        timezone: 'Berlin',
        ssid: ssidInput.value,
        password: passwordInput.value
    })

    var xhr = new XMLHttpRequest();
    xhr.open("POST", '/save', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({
        baseColor: baseColorInput.value,
        wordColor: wordColorInput.value,
        baseLumination: baseLuminationInput.value,
        wordLumination: wordLuminationInput.value,
        time: timeInput.value,
        timezone: 'Berlin',
        ssid: ssidInput.value,
        password: passwordInput.value
    }));
});