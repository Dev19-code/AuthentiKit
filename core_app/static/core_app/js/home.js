document.getElementById('verify-btn').addEventListener('click', function () {
    const code = document.getElementById('verify-code-input').value;
    const resultBox = document.getElementById('verify-result');

    fetch(`/quick-verify/?code=${encodeURIComponent(code)}`)
        .then(response => response.json())
        .then(data => {
            if (data.status === 'authentic') {
                resultBox.innerHTML = `✅ منتج أصلي: ${data.product_name}`;
                resultBox.className = 'result-success';
            } else {
                resultBox.innerHTML = '⚠️ الكود غير موجود أو غير موثّق';
                resultBox.className = 'result-fail';
            }
        })
        .catch(() => {
            resultBox.innerHTML = 'حدث خطأ، حاول تاني';
        });
});