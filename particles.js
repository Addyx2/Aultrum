export function initGooseParticles() {
  const canvas = document.getElementById('gooseCanvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  let width, height;
  let particles = [];
  const numParticles = 150;
  
  // Mouse tracking
  let mouse = { x: -1000, y: -1000, radius: 300 };
  let isHovering = false;

  function resize() {
    width = canvas.width = window.innerWidth;
    height = canvas.height = canvas.parentElement.offsetHeight || window.innerHeight * 0.8;
  }
  window.addEventListener('resize', resize);
  resize();

  window.addEventListener('mousemove', (e) => {
    mouse.x = e.clientX;
    mouse.y = e.clientY;
    isHovering = true;
  });
  window.addEventListener('mouseleave', () => {
    isHovering = false;
  });

  // Generate target points for a V-formation
  // We'll have a leader and wings
  let targetPoints = [];
  function updateTargetPoints() {
    targetPoints = [];
    const leaderX = mouse.x;
    const leaderY = mouse.y - 50;
    
    // We only need as many target points as particles
    const geeseInV = 15; // Number of distinct "geese" in the V
    const pointsPerGoose = numParticles / geeseInV;
    
    for (let i = 0; i < geeseInV; i++) {
      // V-formation math
      let gx, gy;
      if (i === 0) {
        gx = leaderX; gy = leaderY;
      } else {
        const side = i % 2 === 0 ? 1 : -1;
        const row = Math.ceil(i / 2);
        gx = leaderX + (side * row * 60);
        gy = leaderY + (row * 60);
      }
      
      // Each goose is a cluster of points forming a simple chevron
      for(let j=0; j < pointsPerGoose; j++) {
        // Random scatter around the goose center to look like a glowing node
        const ox = (Math.random() - 0.5) * 20;
        const oy = (Math.random() - 0.5) * 20;
        targetPoints.push({ x: gx + ox, y: gy + oy });
      }
    }
  }

  class Particle {
    constructor() {
      this.x = Math.random() * width;
      this.y = Math.random() * height;
      this.baseX = this.x;
      this.baseY = this.y;
      this.vx = (Math.random() - 0.5) * 1;
      this.vy = (Math.random() - 0.5) * 1;
      this.size = Math.random() * 2 + 1;
      this.color = Math.random() > 0.5 ? '#4a9eff' : '#00e676'; // Accent blue and green
    }

    update(target) {
      if (isHovering && target) {
        // Move towards target in V-formation
        const dx = target.x - this.x;
        const dy = target.y - this.y;
        this.x += dx * 0.05;
        this.y += dy * 0.05;
      } else {
        // Idle floating
        this.x += this.vx;
        this.y += this.vy;
        
        // Bounce off edges smoothly
        if (this.x < 0 || this.x > width) this.vx *= -1;
        if (this.y < 0 || this.y > height) this.vy *= -1;
      }
    }

    draw() {
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
      ctx.fillStyle = this.color;
      ctx.fill();
    }
  }

  for (let i = 0; i < numParticles; i++) {
    particles.push(new Particle());
  }

  function animate() {
    ctx.clearRect(0, 0, width, height);
    
    if (isHovering) {
      updateTargetPoints();
    }

    // Draw lines between close particles
    ctx.lineWidth = 0.5;
    for (let i = 0; i < particles.length; i++) {
      for (let j = i + 1; j < particles.length; j++) {
        const dx = particles[i].x - particles[j].x;
        const dy = particles[i].y - particles[j].y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        
        if (dist < 60) {
          ctx.beginPath();
          ctx.strokeStyle = `rgba(74, 158, 255, ${1 - dist/60})`;
          ctx.moveTo(particles[i].x, particles[i].y);
          ctx.lineTo(particles[j].x, particles[j].y);
          ctx.stroke();
        }
      }
    }

    for (let i = 0; i < particles.length; i++) {
      const target = targetPoints[i];
      particles[i].update(target);
      particles[i].draw();
    }

    requestAnimationFrame(animate);
  }

  animate();
}
