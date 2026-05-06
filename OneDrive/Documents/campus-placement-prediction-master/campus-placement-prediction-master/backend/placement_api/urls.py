"""
URL configuration for placement_api project.
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse


def home(request):
    """Landing page for the Campus Placement Prediction API"""
    html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Campus Placement Prediction API</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap" rel="stylesheet" />
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: 'Inter', sans-serif;
      background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #fff;
      overflow: hidden;
    }
    .stars {
      position: fixed; top: 0; left: 0; width: 100%; height: 100%;
      pointer-events: none; z-index: 0;
    }
    .star {
      position: absolute; background: #fff; border-radius: 50%;
      animation: twinkle 3s infinite alternate;
    }
    @keyframes twinkle { from { opacity: 0.2; } to { opacity: 1; } }
    .container {
      position: relative; z-index: 1;
      text-align: center;
      padding: 3rem 2rem;
      max-width: 860px;
      width: 100%;
    }
    .badge {
      display: inline-block;
      background: rgba(99,102,241,0.25);
      border: 1px solid rgba(99,102,241,0.5);
      color: #a5b4fc;
      padding: 0.4rem 1.2rem;
      border-radius: 999px;
      font-size: 0.8rem;
      font-weight: 600;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      margin-bottom: 1.5rem;
    }
    h1 {
      font-size: clamp(2.2rem, 5vw, 3.5rem);
      font-weight: 800;
      line-height: 1.15;
      background: linear-gradient(90deg, #a78bfa, #60a5fa, #34d399);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      margin-bottom: 1rem;
    }
    .subtitle {
      font-size: 1.1rem;
      color: rgba(255,255,255,0.65);
      max-width: 540px;
      margin: 0 auto 2.5rem;
      line-height: 1.6;
    }
    .status-pill {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      background: rgba(52,211,153,0.15);
      border: 1px solid rgba(52,211,153,0.4);
      color: #6ee7b7;
      padding: 0.5rem 1.4rem;
      border-radius: 999px;
      font-size: 0.9rem;
      font-weight: 600;
      margin-bottom: 3rem;
    }
    .dot {
      width: 8px; height: 8px; background: #34d399;
      border-radius: 50%;
      animation: pulse 1.5s ease-in-out infinite;
    }
    @keyframes pulse {
      0%, 100% { opacity: 1; transform: scale(1); }
      50%  { opacity: 0.4; transform: scale(0.85); }
    }
    .cards {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 1.2rem;
      margin-bottom: 3rem;
    }
    .card {
      background: rgba(255,255,255,0.05);
      border: 1px solid rgba(255,255,255,0.1);
      border-radius: 16px;
      padding: 1.5rem 1.2rem;
      backdrop-filter: blur(10px);
      transition: transform 0.2s, background 0.2s;
      text-decoration: none;
      color: inherit;
      display: block;
    }
    .card:hover {
      transform: translateY(-4px);
      background: rgba(255,255,255,0.09);
    }
    .card .icon { font-size: 1.8rem; margin-bottom: 0.6rem; }
    .card .label {
      font-size: 0.75rem;
      font-weight: 600;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: rgba(255,255,255,0.45);
      margin-bottom: 0.3rem;
    }
    .card .endpoint {
      font-size: 0.95rem;
      font-weight: 600;
      color: #c4b5fd;
      word-break: break-all;
    }
    .cta-row { display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; }
    .btn {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.85rem 2rem;
      border-radius: 12px;
      font-size: 0.95rem;
      font-weight: 700;
      text-decoration: none;
      transition: all 0.25s;
      cursor: pointer;
      border: none;
    }
    .btn-primary {
      background: linear-gradient(135deg, #6366f1, #8b5cf6);
      color: #fff;
      box-shadow: 0 4px 20px rgba(99,102,241,0.4);
    }
    .btn-primary:hover {
      transform: translateY(-2px);
      box-shadow: 0 8px 28px rgba(99,102,241,0.55);
    }
    .btn-secondary {
      background: rgba(255,255,255,0.07);
      border: 1px solid rgba(255,255,255,0.2);
      color: rgba(255,255,255,0.85);
    }
    .btn-secondary:hover {
      background: rgba(255,255,255,0.13);
      transform: translateY(-2px);
    }
    footer { margin-top: 3rem; font-size: 0.8rem; color: rgba(255,255,255,0.3); }
  </style>
</head>
<body>
  <div class="stars" id="stars"></div>
  <div class="container">
    <div class="badge">&#x1F916; ML-Powered API</div>
    <h1>Campus Placement<br/>Prediction System</h1>
    <p class="subtitle">
      A machine learning API that predicts student campus placements
      based on academic performance and profile data.
    </p>
    <div class="status-pill"><div class="dot"></div> API is Live &amp; Running</div>

    <div class="cards">
      <a class="card" href="/api/">
        <div class="icon">&#x1F4E1;</div>
        <div class="label">API Explorer</div>
        <div class="endpoint">/api/</div>
      </a>
      <a class="card" href="/api/predictions/predict/">
        <div class="icon">&#x1F52E;</div>
        <div class="label">Predict Endpoint</div>
        <div class="endpoint">/api/predictions/predict/</div>
      </a>
      <a class="card" href="/api/health/">
        <div class="icon">&#x2764;&#xFE0F;</div>
        <div class="label">Health Check</div>
        <div class="endpoint">/api/health/</div>
      </a>
      <a class="card" href="/admin/">
        <div class="icon">&#x1F6E1;&#xFE0F;</div>
        <div class="label">Admin Panel</div>
        <div class="endpoint">/admin/</div>
      </a>
    </div>

    <div class="cta-row">
      <a class="btn btn-primary" href="/api/predictions/">&#x26A1; View All Predictions</a>
      <a class="btn btn-secondary" href="/api/health/">&#x1F4CA; Check Health</a>
    </div>

    <footer>Campus Placement Prediction API &bull; Built with Django REST Framework &bull; Deployed on Render</footer>
  </div>

  <script>
    // Generate random stars
    const starsEl = document.getElementById('stars');
    for (let i = 0; i < 80; i++) {
      const s = document.createElement('div');
      s.className = 'star';
      const size = Math.random() * 2.5 + 0.5;
      s.style.cssText = `width:${size}px;height:${size}px;top:${Math.random()*100}%;left:${Math.random()*100}%;animation-delay:${Math.random()*3}s;animation-duration:${2+Math.random()*3}s`;
      starsEl.appendChild(s);
    }
  </script>
</body>
</html>
"""
    return HttpResponse(html)


urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
