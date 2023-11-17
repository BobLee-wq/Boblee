
const developers = document.querySelectorAll('.developer');

developers.forEach((developer) => {
    developer.addEventListener('mouseenter', () => {
        developer.querySelector('.info').style.display = 'block';
    });

    developer.addEventListener('mouseleave', () => {
        developer.querySelector('.info').style.display = 'none';
    });
});
