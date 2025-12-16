// Smooth scroll effect for navigation
const links = document.querySelectorAll('.nav-links a');

links.forEach(link => {
  link.addEventListener('click', e => {
    e.preventDefault();
    const targetId = link.getAttribute('href');
    document.querySelector(targetId).scrollIntoView({
      behavior: 'smooth'
    });
  });
});

// 3D tilt effect on hero card
const card = document.querySelector('.hero-card');

card.addEventListener('mousemove', (e) => {
  const xAxis = (window.innerWidth / 2 - e.pageX) / 20;
  const yAxis = (window.innerHeight / 2 - e.pageY) / 20;
  card.style.transform = `rotateY(${xAxis}deg) rotateX(${yAxis}deg)`;
});

card.addEventListener('mouseleave', () => {
  card.style.transform = 'rotateY(0deg) rotateX(0deg)';
});
