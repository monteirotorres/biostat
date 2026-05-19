/* ============================================================
   Bioestatística — widgets interativos (canvas + estatística)
   ============================================================ */

// --------- Funções estatísticas básicas ---------
function pdfN(x) { return Math.exp(-0.5 * x * x) / Math.sqrt(2 * Math.PI); }

function cdfN(x) {
  const t = 1 / (1 + 0.2316419 * Math.abs(x));
  const poly = t * (0.319381530 + t * (-0.356563782 + t * (1.781477937 + t * (-1.821255978 + t * 1.330274429))));
  const pdf = pdfN(x);
  const cdf = 1 - pdf * poly;
  return x >= 0 ? cdf : 1 - cdf;
}

function invCdfN(p) {
  let lo = -6, hi = 6, mid;
  for (let i = 0; i < 60; i++) { mid = (lo + hi) / 2; cdfN(mid) < p ? lo = mid : hi = mid; }
  return mid;
}

function randN() {
  const u = 1 - Math.random(), v = Math.random();
  return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v);
}

function lgamma(z) {
  // Lanczos approximation
  const g = 7;
  const c = [0.99999999999980993, 676.5203681218851, -1259.1392167224028,
    771.32342877765313, -176.61502916214059, 12.507343278686905,
    -0.13857109526572012, 9.9843695780195716e-6, 1.5056327351493116e-7];
  if (z < 0.5) return Math.log(Math.PI / Math.sin(Math.PI * z)) - lgamma(1 - z);
  z -= 1;
  let x = c[0];
  for (let i = 1; i < g + 2; i++) x += c[i] / (z + i);
  const t = z + g + 0.5;
  return 0.5 * Math.log(2 * Math.PI) + (z + 0.5) * Math.log(t) - t + Math.log(x);
}

function logChoose(n, k) {
  return lgamma(n + 1) - lgamma(k + 1) - lgamma(n - k + 1);
}

function binomPMF(k, n, p) {
  if (k < 0 || k > n) return 0;
  return Math.exp(logChoose(n, k) + k * Math.log(p) + (n - k) * Math.log(1 - p));
}

// --------- Util de canvas ---------
function makeResizer(canvas, aspect, draw) {
  function resize() {
    const W = canvas.parentElement.clientWidth - 2;
    const H = Math.round(W * aspect);
    canvas.width = W;
    canvas.height = H;
    draw();
  }
  resize();
  window.addEventListener('resize', resize);
  return resize;
}

function $(id) { return document.getElementById(id); }

// ============================================================
// WIDGET 1 — Curva Normal
// ============================================================
function wCurvaNormal(id) {
  const cvs = $(id);
  const ctx = cvs.getContext('2d');

  function draw() {
    const W = cvs.width, H = cvs.height;
    const mu = parseFloat($(id+'-mu').value);
    const sigma = parseFloat($(id+'-sg').value);
    $(id+'-mu-v').textContent = mu.toFixed(1);
    $(id+'-sg-v').textContent = sigma.toFixed(1);

    ctx.clearRect(0, 0, W, H);
    const padL = 28, padR = 28, padT = 24, padB = 32;
    const plotW = W - padL - padR, plotH = H - padT - padB;
    const xMin = -12, xMax = 12;
    const baseY = padT + plotH;
    const peak = 1 / (sigma * Math.sqrt(2 * Math.PI));
    const yScale = plotH * 0.9 / Math.max(peak, 0.55);
    const toX = v => padL + (v - xMin) / (xMax - xMin) * plotW;
    const toY = y => baseY - y * yScale;

    // sombras 1σ, 2σ, 3σ
    const shades = [
      { k: 3, color: 'rgba(50,102,173,0.10)' },
      { k: 2, color: 'rgba(50,102,173,0.18)' },
      { k: 1, color: 'rgba(50,102,173,0.30)' },
    ];
    for (const s of shades) {
      ctx.beginPath();
      ctx.moveTo(toX(mu - s.k * sigma), baseY);
      const steps = 200;
      for (let i = 0; i <= steps; i++) {
        const x = mu - s.k * sigma + i / steps * 2 * s.k * sigma;
        const z = (x - mu) / sigma;
        ctx.lineTo(toX(x), toY(pdfN(z) / sigma));
      }
      ctx.lineTo(toX(mu + s.k * sigma), baseY);
      ctx.closePath();
      ctx.fillStyle = s.color;
      ctx.fill();
    }

    // baseline
    ctx.beginPath();
    ctx.moveTo(padL, baseY); ctx.lineTo(W - padR, baseY);
    ctx.strokeStyle = 'rgba(0,0,0,0.12)'; ctx.stroke();

    // curva
    ctx.beginPath();
    for (let i = 0; i <= 400; i++) {
      const x = xMin + i / 400 * (xMax - xMin);
      const z = (x - mu) / sigma;
      const y = pdfN(z) / sigma;
      i === 0 ? ctx.moveTo(toX(x), toY(y)) : ctx.lineTo(toX(x), toY(y));
    }
    ctx.strokeStyle = '#3266ad'; ctx.lineWidth = 2; ctx.stroke();

    // linha da média
    ctx.beginPath();
    ctx.setLineDash([5, 4]);
    ctx.moveTo(toX(mu), padT); ctx.lineTo(toX(mu), baseY);
    ctx.strokeStyle = '#1a1a1a'; ctx.lineWidth = 1.5; ctx.stroke();
    ctx.setLineDash([]);

    // ticks
    const fs = Math.max(10, Math.round(W * 0.018));
    ctx.font = `${fs}px 'Courier New', monospace`;
    ctx.fillStyle = '#666'; ctx.textAlign = 'center';
    for (let v = -12; v <= 12; v += 4) {
      ctx.fillText(v.toFixed(0), toX(v), baseY + 16);
    }

    // labels σ
    ctx.fillStyle = '#3266ad';
    ctx.font = `bold ${fs}px 'Courier New', monospace`;
    ctx.fillText('μ', toX(mu), padT - 6);
    if (sigma > 0.6) {
      for (let k = 1; k <= 3; k++) {
        const xL = mu - k * sigma, xR = mu + k * sigma;
        if (xL >= xMin) ctx.fillText('-'+k+'σ', toX(xL), baseY + 30);
        if (xR <= xMax) ctx.fillText('+'+k+'σ', toX(xR), baseY + 30);
      }
    }

    // estatísticas
    $(id+'-p1').textContent = '68.3%';
    $(id+'-p2').textContent = '95.4%';
    $(id+'-p3').textContent = '99.7%';
  }

  $(id+'-mu').addEventListener('input', draw);
  $(id+'-sg').addEventListener('input', draw);
  makeResizer(cvs, 0.45, draw);
}

// ============================================================
// WIDGET 2 — Teorema do Limite Central
// ============================================================
function wTLC(id) {
  const cvs = $(id);
  const ctx = cvs.getContext('2d');
  let dist = 'uniforme';

  function samplePop(d) {
    if (d === 'uniforme') return Math.random() * 10;
    if (d === 'exponencial') return -Math.log(1 - Math.random()) * 3;
    if (d === 'bimodal') {
      return Math.random() < 0.5 ? randN() * 0.8 + 2 : randN() * 0.8 + 8;
    }
    return randN() * 2 + 5;
  }

  function draw() {
    const W = cvs.width, H = cvs.height;
    const n = parseInt($(id+'-n').value);
    $(id+'-n-v').textContent = n;

    // 2000 médias amostrais
    const k = 2000;
    const means = [];
    for (let i = 0; i < k; i++) {
      let s = 0;
      for (let j = 0; j < n; j++) s += samplePop(dist);
      means.push(s / n);
    }

    ctx.clearRect(0, 0, W, H);
    const padL = 36, padR = 18, padT = 24, padB = 32;
    const plotW = W - padL - padR, plotH = H - padT - padB;
    const xMin = 0, xMax = 12;
    const nBins = 40;
    const bw = (xMax - xMin) / nBins;
    const counts = new Array(nBins).fill(0);
    for (const v of means) {
      const idx = Math.floor((v - xMin) / bw);
      if (idx >= 0 && idx < nBins) counts[idx]++;
    }
    const maxC = Math.max(...counts);
    const toX = v => padL + (v - xMin) / (xMax - xMin) * plotW;
    const toY = c => padT + plotH - c / maxC * plotH;

    // barras
    ctx.fillStyle = 'rgba(50,102,173,0.55)';
    for (let i = 0; i < nBins; i++) {
      const x0 = toX(xMin + i * bw);
      const x1 = toX(xMin + (i + 1) * bw);
      const y = toY(counts[i]);
      ctx.fillRect(x0 + 0.5, y, x1 - x0 - 1, padT + plotH - y);
    }

    // sobreposição normal teórica
    const mean = means.reduce((a, b) => a + b, 0) / k;
    const sd = Math.sqrt(means.reduce((a, b) => a + (b - mean) ** 2, 0) / k);
    ctx.beginPath();
    ctx.strokeStyle = '#c0392b'; ctx.lineWidth = 2;
    for (let px = 0; px <= plotW; px++) {
      const v = xMin + px / plotW * (xMax - xMin);
      const z = (v - mean) / sd;
      const density = pdfN(z) / sd;
      const expected = density * k * bw;
      const y = padT + plotH - expected / maxC * plotH;
      px === 0 ? ctx.moveTo(padL + px, y) : ctx.lineTo(padL + px, y);
    }
    ctx.stroke();

    // baseline
    ctx.beginPath();
    ctx.moveTo(padL, padT + plotH); ctx.lineTo(padL + plotW, padT + plotH);
    ctx.strokeStyle = 'rgba(0,0,0,0.15)'; ctx.lineWidth = 1; ctx.stroke();

    // ticks
    const fs = Math.max(10, Math.round(W * 0.018));
    ctx.font = `${fs}px 'Courier New', monospace`;
    ctx.fillStyle = '#666'; ctx.textAlign = 'center';
    for (let v = 0; v <= 12; v += 2) ctx.fillText(v.toFixed(0), toX(v), padT + plotH + 16);

    // label
    ctx.fillStyle = '#c0392b';
    ctx.font = `bold ${fs}px 'Courier New', monospace`;
    ctx.textAlign = 'right';
    ctx.fillText('Normal teórica', padL + plotW, padT + 14);

    $(id+'-mean').textContent = mean.toFixed(2);
    $(id+'-sd').textContent = sd.toFixed(2);
  }

  $(id+'-n').addEventListener('input', draw);
  document.querySelectorAll('[data-tlc-dist="'+id+'"]').forEach(btn => {
    btn.addEventListener('click', () => {
      dist = btn.dataset.dist;
      document.querySelectorAll('[data-tlc-dist="'+id+'"]').forEach(b => b.classList.toggle('active', b === btn));
      draw();
    });
  });

  makeResizer(cvs, 0.45, draw);
}

// ============================================================
// WIDGET 3 — Distribuição Binomial
// ============================================================
function wBinomial(id) {
  const cvs = $(id);
  const ctx = cvs.getContext('2d');

  function draw() {
    const W = cvs.width, H = cvs.height;
    const n = parseInt($(id+'-n').value);
    const p = parseFloat($(id+'-p').value);
    $(id+'-n-v').textContent = n;
    $(id+'-p-v').textContent = p.toFixed(2);

    ctx.clearRect(0, 0, W, H);
    const padL = 36, padR = 18, padT = 24, padB = 36;
    const plotW = W - padL - padR, plotH = H - padT - padB;
    const probs = [];
    for (let k = 0; k <= n; k++) probs.push(binomPMF(k, n, p));
    const maxP = Math.max(...probs);
    const toX = k => padL + k / n * plotW;
    const toY = pr => padT + plotH - pr / maxP * plotH;
    const bw = plotW / (n + 1);

    // barras
    for (let k = 0; k <= n; k++) {
      const x = padL + (k / Math.max(n, 1)) * plotW - bw * 0.4;
      const y = toY(probs[k]);
      ctx.fillStyle = 'rgba(50,102,173,0.6)';
      ctx.fillRect(x, y, bw * 0.8, padT + plotH - y);
      ctx.strokeStyle = 'rgba(50,102,173,0.9)';
      ctx.lineWidth = 0.6;
      ctx.strokeRect(x, y, bw * 0.8, padT + plotH - y);
    }

    // baseline
    ctx.beginPath();
    ctx.moveTo(padL, padT + plotH); ctx.lineTo(padL + plotW, padT + plotH);
    ctx.strokeStyle = 'rgba(0,0,0,0.15)'; ctx.stroke();

    // ticks
    const fs = Math.max(9, Math.round(W * 0.016));
    ctx.font = `${fs}px 'Courier New', monospace`;
    ctx.fillStyle = '#666'; ctx.textAlign = 'center';
    const step = Math.max(1, Math.floor(n / 10));
    for (let k = 0; k <= n; k += step) {
      ctx.fillText(k, padL + (k / Math.max(n, 1)) * plotW, padT + plotH + 16);
    }

    const mean = n * p;
    const sd = Math.sqrt(n * p * (1 - p));
    $(id+'-mean').textContent = mean.toFixed(2);
    $(id+'-sd').textContent = sd.toFixed(2);
    $(id+'-modek').textContent = Math.floor((n + 1) * p);
  }

  $(id+'-n').addEventListener('input', draw);
  $(id+'-p').addEventListener('input', draw);
  makeResizer(cvs, 0.45, draw);
}

// ============================================================
// WIDGET 4 — Sensibilidade / Especificidade / VPP / VPN
// ============================================================
function wSensEsp(id) {
  function draw() {
    const sens = parseFloat($(id+'-sens').value);
    const esp = parseFloat($(id+'-esp').value);
    const prev = parseFloat($(id+'-prev').value);
    $(id+'-sens-v').textContent = sens.toFixed(2);
    $(id+'-esp-v').textContent = esp.toFixed(2);
    $(id+'-prev-v').textContent = (prev*100).toFixed(1)+'%';

    const N = 10000;
    const doentes = Math.round(N * prev);
    const saudaveis = N - doentes;
    const VP = Math.round(doentes * sens);
    const FN = doentes - VP;
    const VN = Math.round(saudaveis * esp);
    const FP = saudaveis - VN;

    $(id+'-vp').textContent = VP.toLocaleString('pt-BR');
    $(id+'-fp').textContent = FP.toLocaleString('pt-BR');
    $(id+'-fn').textContent = FN.toLocaleString('pt-BR');
    $(id+'-vn').textContent = VN.toLocaleString('pt-BR');

    const vpp = VP / Math.max(1, VP + FP);
    const vpn = VN / Math.max(1, VN + FN);
    $(id+'-vpp').textContent = (vpp*100).toFixed(1)+'%';
    $(id+'-vpn').textContent = (vpn*100).toFixed(1)+'%';
  }
  $(id+'-sens').addEventListener('input', draw);
  $(id+'-esp').addEventListener('input', draw);
  $(id+'-prev').addEventListener('input', draw);
  draw();
}

// ============================================================
// WIDGET 5 — Curva ROC
// ============================================================
function wROC(id) {
  const cvs = $(id);
  const ctx = cvs.getContext('2d');

  function draw() {
    const sep = parseFloat($(id+'-sep').value);
    $(id+'-sep-v').textContent = sep.toFixed(1);

    const W = cvs.width, H = cvs.height;
    ctx.clearRect(0, 0, W, H);

    const padL = 50, padR = 18, padT = 18, padB = 36;
    const half = (W - padL - padR);
    const plotS = Math.min(half, H - padT - padB);

    // ---- left: two distributions ----
    const x0 = padL, y0 = padT, sW = half, sH = H - padT - padB;
    const xMin = -4, xMax = sep + 4;
    const toX = v => x0 + (v - xMin) / (xMax - xMin) * sW;
    const baseY = y0 + sH;
    const yScale = sH * 0.85;

    function fillCurve(mu, color) {
      ctx.beginPath();
      const steps = 200;
      ctx.moveTo(toX(xMin), baseY);
      for (let i = 0; i <= steps; i++) {
        const x = xMin + i / steps * (xMax - xMin);
        ctx.lineTo(toX(x), baseY - pdfN(x - mu) * yScale);
      }
      ctx.lineTo(toX(xMax), baseY);
      ctx.closePath();
      ctx.fillStyle = color;
      ctx.fill();
    }

    fillCurve(0, 'rgba(50,102,173,0.35)');
    fillCurve(sep, 'rgba(192,57,43,0.35)');

    // baseline
    ctx.beginPath();
    ctx.moveTo(x0, baseY); ctx.lineTo(x0 + sW, baseY);
    ctx.strokeStyle = 'rgba(0,0,0,0.15)'; ctx.stroke();

    // labels
    const fs = Math.max(10, Math.round(W * 0.016));
    ctx.font = `bold ${fs}px 'Courier New', monospace`;
    ctx.textAlign = 'center';
    ctx.fillStyle = '#3266ad'; ctx.fillText('saudáveis', toX(0), baseY - pdfN(0) * yScale - 6);
    ctx.fillStyle = '#c0392b'; ctx.fillText('doentes', toX(sep), baseY - pdfN(0) * yScale - 6);

    // AUC analítica para duas normais iguais var: AUC = Φ(sep/√2)
    const auc = cdfN(sep / Math.sqrt(2));
    $(id+'-auc').textContent = auc.toFixed(3);

    // simples Youden: corte ótimo = sep/2; sens = 1-Φ(sep/2 - sep), esp = Φ(sep/2)
    const opt = sep / 2;
    const sensAt = 1 - cdfN(opt - sep);
    const espAt = cdfN(opt);
    $(id+'-sens').textContent = sensAt.toFixed(3);
    $(id+'-esp').textContent = espAt.toFixed(3);
  }

  $(id+'-sep').addEventListener('input', draw);
  makeResizer(cvs, 0.42, draw);
}

// ============================================================
// WIDGET 6 — Intervalo de Confiança (simulação)
// ============================================================
function wIC(id) {
  const cvs = $(id);
  const ctx = cvs.getContext('2d');
  let seed = 0;

  function draw() {
    const n = parseInt($(id+'-n').value);
    const conf = parseFloat($(id+'-conf').value);
    $(id+'-n-v').textContent = n;
    $(id+'-conf-v').textContent = (conf*100).toFixed(0)+'%';

    const W = cvs.width, H = cvs.height;
    ctx.clearRect(0, 0, W, H);

    const padL = 28, padR = 28, padT = 18, padB = 28;
    const plotW = W - padL - padR, plotH = H - padT - padB;
    const mu = 100, sd = 15;
    const trials = 60;
    const zcrit = invCdfN(0.5 + conf/2);

    const xMin = mu - 3 * sd / Math.sqrt(n) - 4, xMax = mu + 3 * sd / Math.sqrt(n) + 4;
    const toX = v => padL + (v - xMin) / (xMax - xMin) * plotW;

    // linha verdadeira
    ctx.beginPath();
    ctx.moveTo(toX(mu), padT); ctx.lineTo(toX(mu), padT + plotH);
    ctx.strokeStyle = '#1a1a1a'; ctx.lineWidth = 1.5; ctx.setLineDash([4, 3]); ctx.stroke();
    ctx.setLineDash([]);

    // gerar amostras com seed simples (variando a cada redraw)
    let hits = 0;
    for (let i = 0; i < trials; i++) {
      const s = [];
      for (let j = 0; j < n; j++) s.push(mu + sd * randN());
      const m = s.reduce((a, b) => a + b, 0) / n;
      const sse = Math.sqrt(s.reduce((a, b) => a + (b - m) ** 2, 0) / (n - 1));
      const sem = sse / Math.sqrt(n);
      const lo = m - zcrit * sem, hi = m + zcrit * sem;
      const y = padT + (i + 0.5) / trials * plotH;
      const cobre = lo <= mu && mu <= hi;
      if (cobre) hits++;
      ctx.beginPath();
      ctx.moveTo(toX(lo), y); ctx.lineTo(toX(hi), y);
      ctx.strokeStyle = cobre ? 'rgba(50,102,173,0.7)' : 'rgba(192,57,43,0.85)';
      ctx.lineWidth = 1.5; ctx.stroke();
      ctx.fillStyle = cobre ? '#3266ad' : '#c0392b';
      ctx.beginPath(); ctx.arc(toX(m), y, 2, 0, Math.PI * 2); ctx.fill();
    }

    $(id+'-cov').textContent = ((hits/trials)*100).toFixed(1)+'%';

    // ticks
    const fs = Math.max(10, Math.round(W * 0.016));
    ctx.font = `${fs}px 'Courier New', monospace`;
    ctx.fillStyle = '#666'; ctx.textAlign = 'center';
    for (let v = Math.ceil(xMin/5)*5; v <= xMax; v += 5) {
      ctx.fillText(v.toFixed(0), toX(v), padT + plotH + 16);
    }
    ctx.fillStyle = '#1a1a1a';
    ctx.font = `bold ${fs}px 'Courier New', monospace`;
    ctx.fillText('μ = 100', toX(mu), padT - 4);
  }

  $(id+'-n').addEventListener('input', draw);
  $(id+'-conf').addEventListener('input', draw);
  $(id+'-redraw').addEventListener('click', draw);
  makeResizer(cvs, 0.55, draw);
}

// ============================================================
// WIDGET 7 — Erro Tipo I e II (Poder)
// ============================================================
function wErros(id) {
  const cvs = $(id);
  const ctx = cvs.getContext('2d');

  function draw() {
    const W = cvs.width, H = cvs.height;
    const alpha = parseFloat($(id+'-alpha').value);
    const delta = parseFloat($(id+'-delta').value);
    $(id+'-alpha-v').textContent = alpha.toFixed(2);
    $(id+'-delta-v').textContent = delta.toFixed(1);

    const zcrit = invCdfN(1 - alpha);
    const beta = cdfN(zcrit - delta);
    $(id+'-vAlpha').textContent = alpha.toFixed(3);
    $(id+'-vBeta').textContent = beta.toFixed(3);
    $(id+'-vPower').textContent = (1 - beta).toFixed(3);
    $(id+'-vZ').textContent = zcrit.toFixed(2);

    ctx.clearRect(0, 0, W, H);
    const padL = 28, padR = 28, padT = 24, padB = 36;
    const plotW = W - padL - padR, plotH = H - padT - padB;
    const baseY = padT + plotH, scaleY = plotH * 0.88;
    const xMin = -4, xMax = delta + 4;
    const toX = v => padL + (v - xMin) / (xMax - xMin) * plotW;

    function fill(mu, color, a, b) {
      ctx.beginPath();
      ctx.moveTo(toX(a), baseY);
      for (let i = 0; i <= 300; i++) {
        const x = a + i / 300 * (b - a);
        ctx.lineTo(toX(x), baseY - pdfN(x - mu) * scaleY);
      }
      ctx.lineTo(toX(b), baseY); ctx.closePath();
      ctx.fillStyle = color; ctx.fill();
    }
    function curve(mu, color) {
      ctx.beginPath();
      for (let i = 0; i <= 500; i++) {
        const x = xMin + i / 500 * (xMax - xMin);
        const y = pdfN(x - mu);
        i === 0 ? ctx.moveTo(toX(x), baseY - y * scaleY) : ctx.lineTo(toX(x), baseY - y * scaleY);
      }
      ctx.strokeStyle = color; ctx.lineWidth = 2; ctx.stroke();
    }

    ctx.beginPath(); ctx.moveTo(padL, baseY); ctx.lineTo(W - padR, baseY);
    ctx.strokeStyle = 'rgba(0,0,0,0.12)'; ctx.stroke();

    fill(0, 'rgba(192,57,43,0.32)', zcrit, xMax);
    fill(delta, 'rgba(41,128,185,0.32)', xMin, zcrit);
    curve(0, '#3266ad'); curve(delta, '#c0392b');

    ctx.beginPath();
    ctx.setLineDash([5, 4]);
    ctx.moveTo(toX(zcrit), padT); ctx.lineTo(toX(zcrit), baseY);
    ctx.strokeStyle = '#666'; ctx.lineWidth = 1.5; ctx.stroke();
    ctx.setLineDash([]);

    const fs = Math.max(10, Math.round(W * 0.018));
    ctx.font = `bold ${fs}px 'Courier New', monospace`;
    ctx.textAlign = 'center';
    ctx.fillStyle = '#3266ad'; ctx.fillText('H₀', toX(0), baseY - pdfN(0) * scaleY - 6);
    ctx.fillStyle = '#c0392b'; ctx.fillText('H₁', toX(delta), baseY - pdfN(0) * scaleY - 6);
    ctx.fillStyle = '#444'; ctx.font = `${fs-1}px 'Courier New', monospace`;
    ctx.fillText('z* = ' + zcrit.toFixed(2), toX(zcrit), padT - 4);
  }
  $(id+'-alpha').addEventListener('input', draw);
  $(id+'-delta').addEventListener('input', draw);
  makeResizer(cvs, 0.42, draw);
}

// ============================================================
// WIDGET 8 — Correlação (scatter com r dado)
// ============================================================
function wCorrelacao(id) {
  const cvs = $(id);
  const ctx = cvs.getContext('2d');
  let pts = [];

  function regen() {
    const r = parseFloat($(id+'-r').value);
    pts = [];
    for (let i = 0; i < 80; i++) {
      const x = randN(), z = randN();
      const y = r * x + Math.sqrt(1 - r * r) * z;
      pts.push([x, y]);
    }
  }
  regen();

  function draw() {
    const r = parseFloat($(id+'-r').value);
    $(id+'-r-v').textContent = r.toFixed(2);
    $(id+'-r2').textContent = (r*r).toFixed(3);

    const W = cvs.width, H = cvs.height;
    ctx.clearRect(0, 0, W, H);
    const pad = 30, plotW = W - pad * 2, plotH = H - pad * 2;
    const toX = x => pad + (x + 3) / 6 * plotW;
    const toY = y => pad + plotH - (y + 3) / 6 * plotH;

    // axes
    ctx.strokeStyle = 'rgba(0,0,0,0.12)';
    ctx.lineWidth = 1;
    ctx.beginPath(); ctx.moveTo(pad, toY(0)); ctx.lineTo(pad + plotW, toY(0)); ctx.stroke();
    ctx.beginPath(); ctx.moveTo(toX(0), pad); ctx.lineTo(toX(0), pad + plotH); ctx.stroke();

    // points
    ctx.fillStyle = 'rgba(50,102,173,0.6)';
    for (const [x, y] of pts) {
      ctx.beginPath(); ctx.arc(toX(x), toY(y), 3, 0, Math.PI * 2); ctx.fill();
    }

    // reta de regressão (em z, slope = r)
    ctx.beginPath();
    ctx.moveTo(toX(-3), toY(-3 * r)); ctx.lineTo(toX(3), toY(3 * r));
    ctx.strokeStyle = '#c0392b'; ctx.lineWidth = 1.8; ctx.stroke();
  }

  $(id+'-r').addEventListener('input', draw);
  $(id+'-redraw').addEventListener('click', () => { regen(); draw(); });
  makeResizer(cvs, 0.7, draw);
}

// ============================================================
// WIDGET 9 — Valor-p (visualização)
// ============================================================
function wValorP(id) {
  const cvs = $(id);
  const ctx = cvs.getContext('2d');

  function draw() {
    const z = parseFloat($(id+'-z').value);
    const bil = $(id+'-bil').checked;
    $(id+'-z-v').textContent = z.toFixed(2);

    const pUni = 1 - cdfN(Math.abs(z));
    const p = bil ? 2 * pUni : pUni;
    $(id+'-p').textContent = p < 0.0001 ? '< 0.0001' : p.toFixed(4);

    const W = cvs.width, H = cvs.height;
    ctx.clearRect(0, 0, W, H);
    const padL = 28, padR = 28, padT = 24, padB = 32;
    const plotW = W - padL - padR, plotH = H - padT - padB;
    const xMin = -4, xMax = 4, baseY = padT + plotH, scaleY = plotH * 0.88;
    const toX = v => padL + (v - xMin) / (xMax - xMin) * plotW;

    // shade
    function shade(a, b, c) {
      ctx.beginPath();
      ctx.moveTo(toX(a), baseY);
      for (let i = 0; i <= 200; i++) {
        const x = a + i / 200 * (b - a);
        ctx.lineTo(toX(x), baseY - pdfN(x) * scaleY);
      }
      ctx.lineTo(toX(b), baseY); ctx.closePath();
      ctx.fillStyle = c; ctx.fill();
    }
    const az = Math.abs(z);
    shade(az, xMax, 'rgba(192,57,43,0.35)');
    if (bil) shade(xMin, -az, 'rgba(192,57,43,0.35)');

    // curve
    ctx.beginPath();
    for (let i = 0; i <= 500; i++) {
      const x = xMin + i / 500 * (xMax - xMin);
      const y = pdfN(x);
      i === 0 ? ctx.moveTo(toX(x), baseY - y * scaleY) : ctx.lineTo(toX(x), baseY - y * scaleY);
    }
    ctx.strokeStyle = '#3266ad'; ctx.lineWidth = 2; ctx.stroke();

    ctx.beginPath(); ctx.moveTo(padL, baseY); ctx.lineTo(W - padR, baseY);
    ctx.strokeStyle = 'rgba(0,0,0,0.12)'; ctx.stroke();

    // z line
    ctx.beginPath();
    ctx.setLineDash([5, 4]);
    ctx.moveTo(toX(z), padT); ctx.lineTo(toX(z), baseY);
    ctx.strokeStyle = '#666'; ctx.lineWidth = 1.5; ctx.stroke();
    ctx.setLineDash([]);

    const fs = Math.max(10, Math.round(W * 0.018));
    ctx.font = `${fs}px 'Courier New', monospace`;
    ctx.fillStyle = '#666'; ctx.textAlign = 'center';
    for (let v = -4; v <= 4; v++) ctx.fillText(v.toFixed(0), toX(v), baseY + 16);
    ctx.fillStyle = '#1a1a1a';
    ctx.font = `bold ${fs}px 'Courier New', monospace`;
    ctx.fillText('z = ' + z.toFixed(2), toX(z), padT - 4);
  }

  $(id+'-z').addEventListener('input', draw);
  $(id+'-bil').addEventListener('change', draw);
  makeResizer(cvs, 0.42, draw);
}

// ============================================================
// WIDGET 10 — Histograma + amostragem
// ============================================================
function wHistograma(id) {
  const cvs = $(id);
  const ctx = cvs.getContext('2d');
  let dist = 'uniforme';
  let data = [];

  const sizes = [10, 30, 100, 200, 500, 1000, 2000, 5000];

  function resample() {
    const N = sizes[parseInt($(id+'-n').value) - 1];
    data = [];
    for (let i = 0; i < N; i++) {
      data.push(dist === 'normal' ? randN() : (Math.random() * 2 - 1));
    }
  }

  function draw() {
    const W = cvs.width, H = cvs.height;
    const N = sizes[parseInt($(id+'-n').value) - 1];
    const bins = parseInt($(id+'-bins').value);
    $(id+'-n-v').textContent = N.toLocaleString('pt-BR');
    $(id+'-bins-v').textContent = bins;
    if (data.length !== N) resample();

    ctx.clearRect(0, 0, W, H);
    const padL = 44, padR = 22, padT = 24, padB = 36;
    const plotW = W - padL - padR, plotH = H - padT - padB;
    const xMin = dist === 'normal' ? -4 : -1.05;
    const xMax = dist === 'normal' ?  4 :  1.05;
    const counts = new Array(bins).fill(0);
    const bw = (xMax - xMin) / bins;
    for (const v of data) {
      const idx = Math.min(bins - 1, Math.floor((v - xMin) / bw));
      if (idx >= 0 && idx < bins) counts[idx]++;
    }
    const maxC = Math.max(...counts);
    const toX = v => padL + (v - xMin) / (xMax - xMin) * plotW;
    const toY = c => padT + plotH - c / maxC * plotH;

    const barCol = dist === 'normal' ? 'rgba(50,102,173,0.55)' : 'rgba(192,57,43,0.50)';
    const lineCol = dist === 'normal' ? '#3266ad' : '#c0392b';
    for (let i = 0; i < bins; i++) {
      const x0 = toX(xMin + i * bw), x1 = toX(xMin + (i+1) * bw);
      const y = toY(counts[i]);
      ctx.fillStyle = barCol;
      ctx.fillRect(x0 + 0.5, y, x1 - x0 - 1, padT + plotH - y);
    }

    // overlay teórica
    ctx.beginPath();
    ctx.strokeStyle = lineCol; ctx.lineWidth = 2;
    for (let px = 0; px <= plotW; px++) {
      const v = xMin + px / plotW * (xMax - xMin);
      let dens;
      if (dist === 'normal') dens = pdfN(v);
      else dens = (v >= -1 && v <= 1) ? 0.5 : 0;
      const expected = dens * N * bw;
      const y = padT + plotH - expected / maxC * plotH;
      px === 0 ? ctx.moveTo(padL + px, y) : ctx.lineTo(padL + px, y);
    }
    ctx.stroke();

    // ticks
    const fs = Math.max(10, Math.round(W * 0.016));
    ctx.font = `${fs}px 'Courier New', monospace`;
    ctx.fillStyle = '#666'; ctx.textAlign = 'center';
    for (let i = 0; i <= 6; i++) {
      const v = xMin + i / 6 * (xMax - xMin);
      ctx.fillText(v.toFixed(1), toX(v), padT + plotH + 16);
    }

    const mean = data.reduce((a, b) => a + b, 0) / N;
    const sd = Math.sqrt(data.reduce((a, b) => a + (b - mean) ** 2, 0) / (N - 1));
    $(id+'-mean').textContent = mean.toFixed(3);
    $(id+'-sd').textContent = sd.toFixed(3);

    // dist label
    ctx.fillStyle = lineCol;
    ctx.textAlign = 'right';
    ctx.font = `bold ${fs}px 'Courier New', monospace`;
    ctx.fillText(dist === 'normal' ? 'Normal(0,1)' : 'Uniforme(−1,1)', padL + plotW, padT + 12);
  }

  $(id+'-n').addEventListener('input', () => { resample(); draw(); });
  $(id+'-bins').addEventListener('input', draw);
  document.querySelectorAll('[data-hist-dist="'+id+'"]').forEach(btn => {
    btn.addEventListener('click', () => {
      dist = btn.dataset.dist;
      document.querySelectorAll('[data-hist-dist="'+id+'"]').forEach(b => b.classList.toggle('active', b === btn));
      resample(); draw();
    });
  });
  $(id+'-redraw').addEventListener('click', () => { resample(); draw(); });
  resample();
  makeResizer(cvs, 0.45, draw);
}

// ============================================================
// Tabs runtime
// ============================================================
function initTabs() {
  document.querySelectorAll('.tabs').forEach(group => {
    const tabs = group.querySelectorAll('.tab');
    tabs.forEach(tab => {
      tab.addEventListener('click', () => {
        const target = tab.dataset.target;
        tabs.forEach(t => t.classList.toggle('active', t === tab));
        document.querySelectorAll('.topic').forEach(t => {
          t.classList.toggle('active', t.id === target);
        });
        // chama widgets se houver
        window.dispatchEvent(new Event('resize'));
        // scroll suave para o topo do conteúdo
        const el = document.getElementById(target);
        if (el) {
          const top = el.getBoundingClientRect().top + window.pageYOffset - 80;
          window.scrollTo({ top, behavior: 'smooth' });
        }
        // persiste em hash
        if (history && history.replaceState) {
          history.replaceState(null, '', '#' + target);
        }
      });
    });
  });
}

window.addEventListener('DOMContentLoaded', () => {
  initTabs();

  // ativa tab via hash
  if (window.location.hash) {
    const target = window.location.hash.slice(1);
    const tab = document.querySelector('.tab[data-target="' + target + '"]');
    if (tab) tab.click();
  }
});
