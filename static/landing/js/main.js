const button=document.getElementById('menuBtn');
const menu=document.getElementById('mobileMenu');
if(button&&menu){button.addEventListener('click',()=>menu.classList.toggle('open'));menu.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>menu.classList.remove('open')))}
const observer=new IntersectionObserver(entries=>entries.forEach(entry=>{if(entry.isIntersecting){entry.target.classList.add('visible');observer.unobserve(entry.target)}}),{threshold:.12});
document.querySelectorAll('.reveal').forEach(el=>observer.observe(el));
document.querySelectorAll('.bottom-nav a').forEach(a=>a.addEventListener('click',()=>{document.querySelectorAll('.bottom-nav a').forEach(x=>x.classList.remove('active'));a.classList.add('active')}));
