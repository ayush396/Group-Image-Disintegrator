const srcImg = document.getElementById('src-image');
const fileInput = document.getElementById('input-file');


function changeStyle() {
    var element = document.getElementById("src-image");
    element.style.opacity = "1";
}

fileInput.addEventListener('change', e => {
    srcImg.src = URL.createObjectURL(e.target.files[0]);
    changeStyle()

}, false);
