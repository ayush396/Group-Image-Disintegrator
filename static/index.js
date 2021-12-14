const srcImg = document.getElementById('src-image');
const fileInput = document.getElementById('input-file');

fileInput.addEventListener('change', e => {
    srcImg.src = URL.createObjectURL(e.target.files[0]);

}, false);
