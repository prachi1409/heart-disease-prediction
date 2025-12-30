document.addEventListener("DOMContentLoaded", () => {
    console.log("JS Loaded (external)");

    const form = document.getElementById("heartForm");
    const output = document.getElementById("output");

    form.addEventListener("submit", async (e) => {
        e.preventDefault();

        output.innerText = "Predicting...";
        output.style.opacity = "0.8";

        try {
            const formData = new FormData(form);

            const res = await fetch("/predict", {
                method: "POST",
                body: formData
            });

            const data = await res.json();
            output.innerText = data.result;
            output.style.opacity = "1";
        } catch (err) {
            output.innerText = "Error: " + err.message;
            output.style.opacity = "1";
        }
    });
});
