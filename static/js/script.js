document.addEventListener('DOMContentLoaded', () => {
  const searchInput = document.getElementById('search-input');
  const fileCards = document.querySelectorAll('.file-card');

  if (searchInput) {
    searchInput.addEventListener('input', () => {
      const query = searchInput.value.toLowerCase();
      fileCards.forEach(card => {
        const name = card.querySelector('.file-name').textContent.toLowerCase();
        card.style.display = name.includes(query) ? 'flex' : 'none';
      });
    });
  }

  // Fade-in animasyonu
  fileCards.forEach((card, index) => {
    card.style.opacity = 0;
    card.style.transform = 'translateY(10px)';
    setTimeout(() => {
      card.style.transition = 'all 0.4s ease';
      card.style.opacity = 1;
      card.style.transform = 'translateY(0)';
    }, 100 * index);
  });
});


