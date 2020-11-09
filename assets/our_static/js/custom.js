
/*  ==========================================
    SHOW UPLOADED IMAGE
* ========================================== */
function readURL(input) {
    if (input.files && input.files[0]) {
        let reader = new FileReader();

        reader.onload = function (e) {
            $('#imageResult').attr('src', e.target.result);
        };
        reader.readAsDataURL(input.files[0]);
    }
}

// select file input
const input = document.getElementById('upload');

// add event listener
input.addEventListener('change', () => {
    uploadFile(input.files[0]);
});


const uploadFile = (file) => {

    // // check file size (< 2MB)
    // if(file.size > 2 * 1024 * 1024) {
    //     console.log('File must be less than 2MB.');
    // }

    // check file type
    if(!['image/jpeg', 'image/jpg', 'image/png'].includes(file.type)) {
        alert("Allowed image types are PNG, JPG and JPEG. ");
    } else {
        // add file to FormData object
        const fd = new FormData();
        fd.append('image', file);

        // send `POST` request
        fetch('/api/upload/image/', {
            method: 'POST',
            body: fd
        })
        .then(res => res.json())
        .then(json => document.getElementById('controlTextarea').innerHTML = json.message)
        .catch(err => console.error(err));
    }
};

