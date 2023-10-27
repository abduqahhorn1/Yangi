document.addEventListener('DOMContentLoaded', function() {
    // Ekrandagi elementlarni tanlash
    var randomDisplay = document.getElementById('random');
    var btn = document.getElementById('btn');
    
    // EEl orqali Python bilan bog'lanish
    eel.expose(setRandomWord); // Python dan JavaScript ga funksiyaning eksport qilinishi
    eel.start('index.html', 'eel.js'); // EEl proyektini boshlash

    // Ok tugmasiga bosilganda tasodifiy so'zni olish va ekranga chiqarish
    btn.addEventListener('click', function() {
        eel.getRandomWord()(setRandomWord);
    });
    
    // Tasodifiy so'zni ekranga chiqarish
    function setRandomWord(word) {
        randomDisplay.textContent = word;
    }
});