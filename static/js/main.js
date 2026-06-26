// ML Performance Indicator — small UI polish
(function () {
  // Animate the score meter if present
  const meter = document.querySelector('.score-meter');
  if (meter) {
    const pct = parseFloat(meter.dataset.pct || '0');
    const color =
      pct >= 75 ? '#10b981' :
      pct >= 50 ? '#06b6d4' :
      pct >= 25 ? '#f59e0b' : '#ef4444';
    requestAnimationFrame(() => {
      meter.style.setProperty('--pct', pct + '%');
      meter.style.setProperty('--color', color);
    });
  }

  // Confetti on a successful prediction
  const result = document.querySelector('.result-card');
  if (result) {
    burst();
  }

  function burst() {
    const colors = ['#6366f1', '#ec4899', '#06b6d4', '#10b981', '#f59e0b', '#ef4444'];
    const frag = document.createDocumentFragment();
    for (let i = 0; i < 60; i++) {
      const p = document.createElement('span');
      p.style.cssText = `
        position: fixed;
        top: -10px;
        left: ${Math.random() * 100}vw;
        width: 8px; height: 14px;
        background: ${colors[i % colors.length]};
        transform: rotate(${Math.random() * 360}deg);
        opacity: 0.95;
        z-index: 9999;
        border-radius: 2px;
        pointer-events: none;
        animation: fall ${2 + Math.random() * 2}s linear ${Math.random() * 0.6}s forwards;
      `;
      frag.appendChild(p);
    }
    document.body.appendChild(frag);
    const style = document.createElement('style');
    style.textContent = `@keyframes fall {
      to { transform: translateY(110vh) rotate(720deg); opacity: 0; }
    }`;
    document.head.appendChild(style);
    setTimeout(() => { document.body.removeChild(frag); }, 4500);
  }
})();