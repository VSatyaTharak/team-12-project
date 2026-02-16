async function uploadImage() {
    const fileInput = document.getElementById("imageInput");
    const formData = new FormData();
    formData.append("file", fileInput.files[0]);

    const response = await fetch("http://127.0.0.1:8001/generate/", {
        method: "POST",
        body: formData
    });

    const data = await response.json();

    document.getElementById("result").innerHTML = `
        <h3>English:</h3> ${data.english}
        <h3>Hindi:</h3> ${data.hindi}
        <h3>Maithili:</h3> ${data.maithili}
        <h3>Konkani:</h3> ${data.konkani}
    `;
}



