/**
 * File: assets/js/main.js
 * Deskripsi: Skrip JavaScript utama untuk fungsionalitas website GKPI Cimahi.
 */

document.addEventListener('DOMContentLoaded', function () {
    // Fungsionalitas untuk menu mobile
    const mobileMenuButton = document.getElementById('mobile-menu-button');
    const mobileMenu = document.getElementById('mobile-menu');

    if (mobileMenuButton && mobileMenu) {
        mobileMenuButton.addEventListener('click', function () {
            mobileMenu.classList.toggle('hidden');
        });
    }
});
