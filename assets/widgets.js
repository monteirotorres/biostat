/* ============================================================
   Bioestatística — widgets interativos
   Princípio: mover um slider NUNCA sorteia novos valores.
   Só o botão "nova simulação/amostra" gera dados novos.
   ============================================================ */

// ---------- PRNG determinístico (mulberry32) ----------
function makeRng(seed) {
  let s = seed >>> 0;
  return function () {
    s |= 0; s = (s + 0x6D2B79F5) | 0;
    let t = Math.imul(s ^ (s >>> 15), 1 | s);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}
function rngNormal(rng) {
  const u = 1 - rng(), v = rng();
  return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v);
}

// ---------- estatística ----------
function pdfN(x) { return Math.exp(-0.5 * x * x) / Math.sqrt(2 * Math.PI); }
function cdfN(x) {
  const t = 1 / (1 + 0.2316419 * Math.abs(x));
  const poly = t * (0.319381530 + t * (-0.356563782 + t * (1.781477937 + t * (-1.821255978 + t * 1.330274429))));
  const cdf = 1 - pdfN(x) * poly;
  return x >= 0 ? cdf : 1 - cdf;
}
function invCdfN(p) {
  let lo = -6, hi = 6, mid;
  for (let i = 0; i < 60; i++) { mid = (lo + hi) / 2; cdfN(mid) < p ? lo = mid : hi = mid; }
  return mid;
}
function lgamma(z) {
  const g = 7, c = [0.99999999999980993, 676.5203681218851, -1259.1392167224028,
    771.32342877765313, -176.61502916214059, 12.507343278686905,
    -0.13857109526572012, 9.9843695780195716e-6, 1.5056327351493116e-7];
  if (z < 0.5) return Math.log(Math.PI / Math.sin(Math.PI * z)) - lgamma(1 - z);
  z -= 1; let x = c[0];
  for (let i = 1; i < g + 2; i++) x += c[i] / (z + i);
  const t = z + g + 0.5;
  return 0.5 * Math.log(2 * Math.PI) + (z + 0.5) * Math.log(t) - t + Math.log(x);
}
function binomPMF(k, n, p) {
  if (k < 0 || k > n) return 0;
  return Math.exp(lgamma(n + 1) - lgamma(k + 1) - lgamma(n - k + 1) + k * Math.log(p) + (n - k) * Math.log(1 - p));
}
function mean(a) { return a.reduce((x, y) => x + y, 0) / a.length; }
function sd(a, ddof = 1) { const m = mean(a); return Math.sqrt(a.reduce((s, x) => s + (x - m) ** 2, 0) / (a.length - ddof)); }
function quantile(sorted, q) {
  const pos = (sorted.length - 1) * q, b = Math.floor(pos), r = pos - b;
  return sorted[b + 1] !== undefined ? sorted[b] + r * (sorted[b + 1] - sorted[b]) : sorted[b];
}
// gama incompleta regularizada P(a,x) (Numerical Recipes)
function gammap(a, x) {
  if (x <= 0 || a <= 0) return 0;
  if (x < a + 1) {
    let ap = a, sum = 1 / a, del = sum;
    for (let i = 0; i < 300; i++) { ap++; del *= x / ap; sum += del; if (Math.abs(del) < Math.abs(sum) * 1e-13) break; }
    return sum * Math.exp(-x + a * Math.log(x) - lgamma(a));
  }
  let b = x + 1 - a, c = 1e30, d = 1 / b, h = d;
  for (let i = 1; i <= 300; i++) {
    const an = -i * (i - a); b += 2; d = an * d + b; if (Math.abs(d) < 1e-30) d = 1e-30;
    c = b + an / c; if (Math.abs(c) < 1e-30) c = 1e-30; d = 1 / d; const del = d * c; h *= del;
    if (Math.abs(del - 1) < 1e-13) break;
  }
  return 1 - Math.exp(-x + a * Math.log(x) - lgamma(a)) * h;
}
function chi2cdf(x, v) { return gammap(v / 2, x / 2); }
function chi2sf(x, v) { return 1 - chi2cdf(x, v); }
function chi2inv(pp, v) { let lo = 0, hi = 1000, mid; for (let i = 0; i < 80; i++) { mid = (lo + hi) / 2; chi2cdf(mid, v) < pp ? lo = mid : hi = mid; } return mid; }
// qui-quadrado não-central: P(X > x) com gl v e parâmetro de não-centralidade lam
function ncChi2sf(x, v, lam) {
  const half = lam / 2; let s = 0, logw = -half;
  for (let j = 0; j < 300; j++) {
    s += Math.exp(logw) * chi2sf(x, v + 2 * j);
    if (j > half && Math.exp(logw) < 1e-9) break;
    logw += Math.log(half) - Math.log(j + 1);
  }
  return s;
}

// ---------- canvas ----------
function $(id) { return document.getElementById(id); }

// cores sensíveis ao tema (lidas em cada draw)
function _dark() { return document.documentElement.dataset.theme === 'dark'; }
function INK() { return _dark() ? '#ece6d8' : '#1a1a1a'; }
function MUTED() { return _dark() ? '#a59a85' : '#666'; }
function GRID() { return _dark() ? 'rgba(255,255,255,0.16)' : 'rgba(0,0,0,0.15)'; }
function GRIDSOFT() { return _dark() ? 'rgba(255,255,255,0.07)' : 'rgba(0,0,0,0.08)'; }

function makeResizer(canvas, aspect, draw) {
  function resize() {
    const W = Math.max(280, canvas.parentElement.clientWidth - 2);
    canvas.width = W; canvas.height = Math.round(W * aspect);
    draw();
  }
  resize();
  window.addEventListener('resize', resize);
  return resize;
}

// ============================================================
// 1 — Curva Normal (sem aleatoriedade)
// ============================================================
function wCurvaNormal(id) {
  const cvs = $(id), ctx = cvs.getContext('2d');
  function draw() {
    const W = cvs.width, H = cvs.height;
    const mu = +$(id + '-mu').value, sigma = +$(id + '-sg').value;
    $(id + '-mu-v').textContent = mu.toFixed(1);
    $(id + '-sg-v').textContent = sigma.toFixed(1);
    ctx.clearRect(0, 0, W, H);
    const padL = 28, padR = 28, padT = 24, padB = 32;
    const plotW = W - padL - padR, plotH = H - padT - padB;
    const xMin = -12, xMax = 12, baseY = padT + plotH;
    const peak = 1 / (sigma * Math.sqrt(2 * Math.PI));
    const yScale = plotH * 0.9 / Math.max(peak, 0.55);
    const toX = v => padL + (v - xMin) / (xMax - xMin) * plotW;
    const toY = y => baseY - y * yScale;
    for (const s of [{ k: 3, c: 'rgba(50,102,173,0.10)' }, { k: 2, c: 'rgba(50,102,173,0.18)' }, { k: 1, c: 'rgba(50,102,173,0.30)' }]) {
      ctx.beginPath(); ctx.moveTo(toX(mu - s.k * sigma), baseY);
      for (let i = 0; i <= 200; i++) { const x = mu - s.k * sigma + i / 200 * 2 * s.k * sigma; ctx.lineTo(toX(x), toY(pdfN((x - mu) / sigma) / sigma)); }
      ctx.lineTo(toX(mu + s.k * sigma), baseY); ctx.closePath(); ctx.fillStyle = s.c; ctx.fill();
    }
    ctx.beginPath(); ctx.moveTo(padL, baseY); ctx.lineTo(W - padR, baseY); ctx.strokeStyle = GRID(); ctx.stroke();
    ctx.beginPath();
    for (let i = 0; i <= 400; i++) { const x = xMin + i / 400 * (xMax - xMin); const y = pdfN((x - mu) / sigma) / sigma; i ? ctx.lineTo(toX(x), toY(y)) : ctx.moveTo(toX(x), toY(y)); }
    ctx.strokeStyle = '#3266ad'; ctx.lineWidth = 2; ctx.stroke();
    ctx.beginPath(); ctx.setLineDash([5, 4]); ctx.moveTo(toX(mu), padT); ctx.lineTo(toX(mu), baseY); ctx.strokeStyle = INK(); ctx.lineWidth = 1.5; ctx.stroke(); ctx.setLineDash([]);
    const fs = Math.max(10, Math.round(W * 0.018));
    ctx.font = `${fs}px 'Courier New', monospace`; ctx.fillStyle = MUTED(); ctx.textAlign = 'center';
    for (let v = -12; v <= 12; v += 4) ctx.fillText(v.toFixed(0), toX(v), baseY + 16);
    ctx.fillStyle = '#3266ad'; ctx.font = `bold ${fs}px 'Courier New', monospace`; ctx.fillText('μ', toX(mu), padT - 6);
    $(id + '-p1').textContent = '68.3%'; $(id + '-p2').textContent = '95.4%'; $(id + '-p3').textContent = '99.7%';
  }
  $(id + '-mu').addEventListener('input', draw);
  $(id + '-sg').addEventListener('input', draw);
  makeResizer(cvs, 0.45, draw);
}

// ============================================================
// 2 — TLC (seed fixo; só botão gera nova simulação)
// ============================================================
function wTLC(id) {
  const cvs = $(id), ctx = cvs.getContext('2d');
  let dist = 'uniforme', seed = 12345, means = [];
  function samplePop(rng) {
    if (dist === 'uniforme') return rng() * 10;
    if (dist === 'exponencial') return -Math.log(1 - rng()) * 3;
    if (dist === 'bimodal') return rng() < 0.5 ? rngNormal(rng) * 0.8 + 2 : rngNormal(rng) * 0.8 + 8;
    return rngNormal(rng) * 2 + 5;
  }
  function generate() {
    const n = +$(id + '-n').value, rng = makeRng(seed);
    means = [];
    for (let i = 0; i < 2000; i++) { let s = 0; for (let j = 0; j < n; j++) s += samplePop(rng); means.push(s / n); }
  }
  function draw() {
    $(id + '-n-v').textContent = $(id + '-n').value;
    const W = cvs.width, H = cvs.height; ctx.clearRect(0, 0, W, H);
    const padL = 36, padR = 18, padT = 24, padB = 32, plotW = W - padL - padR, plotH = H - padT - padB;
    const xMin = 0, xMax = 12, nB = 40, bw = (xMax - xMin) / nB, counts = new Array(nB).fill(0);
    for (const v of means) { const i = Math.floor((v - xMin) / bw); if (i >= 0 && i < nB) counts[i]++; }
    const maxC = Math.max(...counts, 1);
    const toX = v => padL + (v - xMin) / (xMax - xMin) * plotW, toY = c => padT + plotH - c / maxC * plotH;
    ctx.fillStyle = 'rgba(50,102,173,0.55)';
    for (let i = 0; i < nB; i++) { const x0 = toX(xMin + i * bw), x1 = toX(xMin + (i + 1) * bw); ctx.fillRect(x0 + 0.5, toY(counts[i]), x1 - x0 - 1, padT + plotH - toY(counts[i])); }
    const m = mean(means), s = sd(means, 0);
    ctx.beginPath(); ctx.strokeStyle = '#c0392b'; ctx.lineWidth = 2;
    for (let px = 0; px <= plotW; px++) { const v = xMin + px / plotW * (xMax - xMin); const e = pdfN((v - m) / s) / s * 2000 * bw; const y = padT + plotH - e / maxC * plotH; px ? ctx.lineTo(padL + px, y) : ctx.moveTo(padL + px, y); }
    ctx.stroke();
    ctx.beginPath(); ctx.moveTo(padL, padT + plotH); ctx.lineTo(padL + plotW, padT + plotH); ctx.strokeStyle = GRID(); ctx.stroke();
    const fs = Math.max(10, Math.round(W * 0.018)); ctx.font = `${fs}px 'Courier New', monospace`; ctx.fillStyle = MUTED(); ctx.textAlign = 'center';
    for (let v = 0; v <= 12; v += 2) ctx.fillText(v.toFixed(0), toX(v), padT + plotH + 16);
    ctx.fillStyle = '#c0392b'; ctx.font = `bold ${fs}px 'Courier New', monospace`; ctx.textAlign = 'right'; ctx.fillText('Normal teórica', padL + plotW, padT + 14);
    $(id + '-mean').textContent = m.toFixed(2); $(id + '-sd').textContent = s.toFixed(2);
  }
  $(id + '-n').addEventListener('input', () => { generate(); draw(); });
  document.querySelectorAll('[data-tlc-dist="' + id + '"]').forEach(b => b.addEventListener('click', () => {
    dist = b.dataset.dist; document.querySelectorAll('[data-tlc-dist="' + id + '"]').forEach(x => x.classList.toggle('active', x === b)); generate(); draw();
  }));
  $(id + '-redraw').addEventListener('click', () => { seed = (seed * 1103515245 + 12345) & 0x7fffffff; generate(); draw(); });
  generate(); makeResizer(cvs, 0.45, draw);
}

// ============================================================
// 3 — Binomial (analítico, sem aleatoriedade)
// ============================================================
function wBinomial(id) {
  const cvs = $(id), ctx = cvs.getContext('2d');
  function draw() {
    const n = +$(id + '-n').value, p = +$(id + '-p').value;
    $(id + '-n-v').textContent = n; $(id + '-p-v').textContent = p.toFixed(2);
    const W = cvs.width, H = cvs.height; ctx.clearRect(0, 0, W, H);
    const padL = 36, padR = 18, padT = 24, padB = 36, plotW = W - padL - padR, plotH = H - padT - padB;
    const probs = []; for (let k = 0; k <= n; k++) probs.push(binomPMF(k, n, p));
    const maxP = Math.max(...probs), toY = pr => padT + plotH - pr / maxP * plotH, bw = plotW / (n + 1);
    for (let k = 0; k <= n; k++) { const x = padL + k / Math.max(n, 1) * plotW - bw * 0.4, y = toY(probs[k]); ctx.fillStyle = 'rgba(50,102,173,0.6)'; ctx.fillRect(x, y, bw * 0.8, padT + plotH - y); }
    ctx.beginPath(); ctx.moveTo(padL, padT + plotH); ctx.lineTo(padL + plotW, padT + plotH); ctx.strokeStyle = GRID(); ctx.stroke();
    const fs = Math.max(9, Math.round(W * 0.016)); ctx.font = `${fs}px 'Courier New', monospace`; ctx.fillStyle = MUTED(); ctx.textAlign = 'center';
    const step = Math.max(1, Math.floor(n / 10));
    for (let k = 0; k <= n; k += step) ctx.fillText(k, padL + k / Math.max(n, 1) * plotW, padT + plotH + 16);
    $(id + '-mean').textContent = (n * p).toFixed(2); $(id + '-sd').textContent = Math.sqrt(n * p * (1 - p)).toFixed(2); $(id + '-modek').textContent = Math.floor((n + 1) * p);
  }
  $(id + '-n').addEventListener('input', draw); $(id + '-p').addEventListener('input', draw);
  makeResizer(cvs, 0.45, draw);
}

// ============================================================
// 4 — Sensibilidade/Especificidade/VPP (determinístico)
// ============================================================
function wSensEsp(id) {
  function draw() {
    const sens = +$(id + '-sens').value, esp = +$(id + '-esp').value, prev = +$(id + '-prev').value;
    $(id + '-sens-v').textContent = sens.toFixed(2); $(id + '-esp-v').textContent = esp.toFixed(2); $(id + '-prev-v').textContent = (prev * 100).toFixed(1) + '%';
    const N = 10000, doentes = Math.round(N * prev), saud = N - doentes;
    const VP = Math.round(doentes * sens), FN = doentes - VP, VN = Math.round(saud * esp), FP = saud - VN;
    $(id + '-vp').textContent = VP.toLocaleString('pt-BR'); $(id + '-fp').textContent = FP.toLocaleString('pt-BR');
    $(id + '-fn').textContent = FN.toLocaleString('pt-BR'); $(id + '-vn').textContent = VN.toLocaleString('pt-BR');
    $(id + '-vpp').textContent = (VP / Math.max(1, VP + FP) * 100).toFixed(1) + '%';
    $(id + '-vpn').textContent = (VN / Math.max(1, VN + FN) * 100).toFixed(1) + '%';
  }
  $(id + '-sens').addEventListener('input', draw); $(id + '-esp').addEventListener('input', draw); $(id + '-prev').addEventListener('input', draw);
  draw();
}

// ============================================================
// 5 — ROC completa: distribuições + corte + matriz de confusão + curva
// ============================================================
function wROC(id) {
  const cvs = $(id), ctx = cvs.getContext('2d');
  function metrics() {
    const sep = +$(id + '-sep').value, prev = +$(id + '-prev').value, thr = +$(id + '-thr').value, N = 10000;
    const nD = Math.round(N * prev), nS = N - nD;
    const TP = Math.round(nD * (1 - cdfN(thr - sep)));
    const FN = nD - TP;
    const FP = Math.round(nS * (1 - cdfN(thr)));
    const TN = nS - FP;
    return { sep, prev, thr, TP, FN, FP, TN, nD, nS };
  }
  function draw() {
    const m = metrics();
    $(id + '-sep-v').textContent = m.sep.toFixed(1);
    $(id + '-prev-v').textContent = (m.prev * 100).toFixed(0) + '%';
    $(id + '-thr-v').textContent = m.thr.toFixed(2);
    // matriz + métricas
    $(id + '-tp').textContent = m.TP; $(id + '-fp').textContent = m.FP;
    $(id + '-fn').textContent = m.FN; $(id + '-tn').textContent = m.TN;
    const sens = m.TP / Math.max(1, m.TP + m.FN), spec = m.TN / Math.max(1, m.TN + m.FP);
    const ppv = m.TP / Math.max(1, m.TP + m.FP), npv = m.TN / Math.max(1, m.TN + m.FN);
    const acc = (m.TP + m.TN) / 10000;
    $(id + '-sens').textContent = (sens * 100).toFixed(1) + '%';
    $(id + '-spec').textContent = (spec * 100).toFixed(1) + '%';
    $(id + '-ppv').textContent = (ppv * 100).toFixed(1) + '%';
    $(id + '-npv').textContent = (npv * 100).toFixed(1) + '%';
    $(id + '-acc').textContent = (acc * 100).toFixed(1) + '%';
    $(id + '-auc').textContent = cdfN(m.sep / Math.sqrt(2)).toFixed(3);

    const W = cvs.width, H = cvs.height; ctx.clearRect(0, 0, W, H);
    const gap = 24, half = (W - gap) / 2;
    // --- esquerda: distribuições ---
    const x0 = 0, y0 = 18, sW = half, sH = H - 50, baseY = y0 + sH;
    const xMin = -4, xMax = m.sep + 4, toX = v => x0 + (v - xMin) / (xMax - xMin) * sW, yS = sH * 0.8;
    function fill(mu, color) {
      ctx.beginPath(); ctx.moveTo(toX(xMin), baseY);
      for (let i = 0; i <= 200; i++) { const x = xMin + i / 200 * (xMax - xMin); ctx.lineTo(toX(x), baseY - pdfN(x - mu) * yS); }
      ctx.lineTo(toX(xMax), baseY); ctx.closePath(); ctx.fillStyle = color; ctx.fill();
    }
    fill(0, 'rgba(50,102,173,0.35)'); fill(m.sep, 'rgba(192,57,43,0.35)');
    ctx.beginPath(); ctx.moveTo(x0, baseY); ctx.lineTo(x0 + sW, baseY); ctx.strokeStyle = GRID(); ctx.stroke();
    // linha de corte
    ctx.beginPath(); ctx.setLineDash([5, 4]); ctx.moveTo(toX(m.thr), y0); ctx.lineTo(toX(m.thr), baseY); ctx.strokeStyle = INK(); ctx.lineWidth = 1.5; ctx.stroke(); ctx.setLineDash([]);
    const fs = Math.max(9, Math.round(W * 0.014)); ctx.font = `bold ${fs}px 'Courier New', monospace`; ctx.textAlign = 'center';
    ctx.fillStyle = '#3266ad'; ctx.fillText('saudáveis', toX(0), baseY - pdfN(0) * yS - 4);
    ctx.fillStyle = '#c0392b'; ctx.fillText('doentes', toX(m.sep), baseY - pdfN(0) * yS - 4);
    ctx.fillStyle = INK(); ctx.font = `${fs}px 'Courier New', monospace`; ctx.fillText('corte', toX(m.thr), y0 - 4);
    // --- direita: curva ROC ---
    const rx = half + gap, ry = 18, rW = half - 18, rH = H - 50;
    ctx.strokeStyle = GRID(); ctx.strokeRect(rx, ry, rW, rH);
    ctx.beginPath(); ctx.setLineDash([3, 3]); ctx.moveTo(rx, ry + rH); ctx.lineTo(rx + rW, ry); ctx.strokeStyle = '#bbb'; ctx.stroke(); ctx.setLineDash([]);
    ctx.beginPath(); ctx.strokeStyle = '#3266ad'; ctx.lineWidth = 2;
    for (let i = 0; i <= 100; i++) {
      const t = -4 + i / 100 * (m.sep + 8);
      const tpr = 1 - cdfN(t - m.sep), fpr = 1 - cdfN(t);
      const px = rx + fpr * rW, py = ry + rH - tpr * rH;
      i ? ctx.lineTo(px, py) : ctx.moveTo(px, py);
    }
    ctx.stroke();
    // ponto de operação atual
    const tpr = 1 - cdfN(m.thr - m.sep), fpr = 1 - cdfN(m.thr);
    ctx.fillStyle = '#c0392b'; ctx.beginPath(); ctx.arc(rx + fpr * rW, ry + rH - tpr * rH, 4, 0, 7); ctx.fill();
    ctx.fillStyle = MUTED(); ctx.font = `${fs}px 'Courier New', monospace`; ctx.textAlign = 'center';
    ctx.fillText('curva ROC', rx + rW / 2, ry + 12);
    ctx.fillText('1 - especificidade', rx + rW / 2, ry + rH + 16);
  }
  ['sep', 'prev', 'thr'].forEach(k => $(id + '-' + k).addEventListener('input', draw));
  makeResizer(cvs, 0.5, draw);
}

// ============================================================
// 6 — Intervalo de Confiança (seed fixo; EIXO FIXO)
// ============================================================
function wIC(id) {
  const cvs = $(id), ctx = cvs.getContext('2d');
  let seed = 777, samples = [];
  const MU = 100, SD = 15, TRIALS = 60;
  function generate() {
    const n = +$(id + '-n').value, rng = makeRng(seed);
    samples = [];
    for (let i = 0; i < TRIALS; i++) { const s = []; for (let j = 0; j < n; j++) s.push(MU + SD * rngNormal(rng)); samples.push(s); }
  }
  function draw() {
    const n = +$(id + '-n').value, conf = +$(id + '-conf').value;
    $(id + '-n-v').textContent = n; $(id + '-conf-v').textContent = (conf * 100).toFixed(0) + '%';
    const W = cvs.width, H = cvs.height; ctx.clearRect(0, 0, W, H);
    const padL = 28, padR = 28, padT = 18, padB = 28, plotW = W - padL - padR, plotH = H - padT - padB;
    const zc = invCdfN(0.5 + conf / 2);
    const xMin = MU - 22, xMax = MU + 22;            // EIXO FIXO (não muda com n)
    const toX = v => padL + (v - xMin) / (xMax - xMin) * plotW;
    ctx.beginPath(); ctx.setLineDash([4, 3]); ctx.moveTo(toX(MU), padT); ctx.lineTo(toX(MU), padT + plotH); ctx.strokeStyle = INK(); ctx.lineWidth = 1.5; ctx.stroke(); ctx.setLineDash([]);
    let hits = 0;
    for (let i = 0; i < TRIALS; i++) {
      const s = samples[i], m = mean(s), sem = sd(s) / Math.sqrt(n), lo = m - zc * sem, hi = m + zc * sem;
      const y = padT + (i + 0.5) / TRIALS * plotH, cobre = lo <= MU && MU <= hi; if (cobre) hits++;
      ctx.beginPath(); ctx.moveTo(toX(Math.max(lo, xMin)), y); ctx.lineTo(toX(Math.min(hi, xMax)), y);
      ctx.strokeStyle = cobre ? 'rgba(50,102,173,0.7)' : 'rgba(192,57,43,0.9)'; ctx.lineWidth = 1.5; ctx.stroke();
      ctx.fillStyle = cobre ? '#3266ad' : '#c0392b'; ctx.beginPath(); ctx.arc(toX(m), y, 2, 0, 7); ctx.fill();
    }
    $(id + '-cov').textContent = (hits / TRIALS * 100).toFixed(1) + '%';
    const fs = Math.max(10, Math.round(W * 0.016)); ctx.font = `${fs}px 'Courier New', monospace`; ctx.fillStyle = MUTED(); ctx.textAlign = 'center';
    for (let v = 85; v <= 115; v += 5) ctx.fillText(v, toX(v), padT + plotH + 16);
    ctx.fillStyle = INK(); ctx.font = `bold ${fs}px 'Courier New', monospace`; ctx.fillText('μ = 100', toX(MU), padT - 4);
  }
  $(id + '-n').addEventListener('input', () => { generate(); draw(); });
  $(id + '-conf').addEventListener('input', draw);
  $(id + '-redraw').addEventListener('click', () => { seed = (seed * 1103515245 + 12345) & 0x7fffffff; generate(); draw(); });
  generate(); makeResizer(cvs, 0.55, draw);
}

// ============================================================
// 7 — Erros tipo I e II (determinístico; eixo fixo)
// ============================================================
function wErros(id) {
  const cvs = $(id), ctx = cvs.getContext('2d');
  function draw() {
    const W = cvs.width, H = cvs.height;
    const alpha = +$(id + '-alpha').value, delta = +$(id + '-delta').value;
    $(id + '-alpha-v').textContent = alpha.toFixed(2); $(id + '-delta-v').textContent = delta.toFixed(1);
    const zc = invCdfN(1 - alpha), beta = cdfN(zc - delta);
    $(id + '-vAlpha').textContent = alpha.toFixed(3); $(id + '-vBeta').textContent = beta.toFixed(3);
    $(id + '-vPower').textContent = (1 - beta).toFixed(3); $(id + '-vZ').textContent = zc.toFixed(2);
    ctx.clearRect(0, 0, W, H);
    const padL = 28, padR = 28, padT = 24, padB = 36, plotW = W - padL - padR, plotH = H - padT - padB;
    const baseY = padT + plotH, sY = plotH * 0.88, xMin = -4, xMax = 7;   // eixo fixo
    const toX = v => padL + (v - xMin) / (xMax - xMin) * plotW;
    function fill(mu, color, a, b) { ctx.beginPath(); ctx.moveTo(toX(a), baseY); for (let i = 0; i <= 300; i++) { const x = a + i / 300 * (b - a); ctx.lineTo(toX(x), baseY - pdfN(x - mu) * sY); } ctx.lineTo(toX(b), baseY); ctx.closePath(); ctx.fillStyle = color; ctx.fill(); }
    function curve(mu, color) { ctx.beginPath(); for (let i = 0; i <= 500; i++) { const x = xMin + i / 500 * (xMax - xMin); const y = pdfN(x - mu); i ? ctx.lineTo(toX(x), baseY - y * sY) : ctx.moveTo(toX(x), baseY - y * sY); } ctx.strokeStyle = color; ctx.lineWidth = 2; ctx.stroke(); }
    ctx.beginPath(); ctx.moveTo(padL, baseY); ctx.lineTo(W - padR, baseY); ctx.strokeStyle = GRID(); ctx.stroke();
    fill(0, 'rgba(192,57,43,0.32)', zc, xMax); fill(delta, 'rgba(41,128,185,0.32)', xMin, zc);
    curve(0, '#3266ad'); curve(delta, '#c0392b');
    ctx.beginPath(); ctx.setLineDash([5, 4]); ctx.moveTo(toX(zc), padT); ctx.lineTo(toX(zc), baseY); ctx.strokeStyle = MUTED(); ctx.lineWidth = 1.5; ctx.stroke(); ctx.setLineDash([]);
    const fs = Math.max(10, Math.round(W * 0.018)); ctx.font = `bold ${fs}px 'Courier New', monospace`; ctx.textAlign = 'center';
    ctx.fillStyle = '#3266ad'; ctx.fillText('H₀', toX(0), baseY - pdfN(0) * sY - 6);
    ctx.fillStyle = '#c0392b'; ctx.fillText('H₁', toX(delta), baseY - pdfN(0) * sY - 6);
    ctx.fillStyle = MUTED(); ctx.font = `${fs - 1}px 'Courier New', monospace`; ctx.fillText('z* = ' + zc.toFixed(2), toX(zc), padT - 4);
  }
  $(id + '-alpha').addEventListener('input', draw); $(id + '-delta').addEventListener('input', draw);
  makeResizer(cvs, 0.42, draw);
}

// ============================================================
// 8 — Correlação com resíduos (seed fixo; slider r não re-sorteia)
// ============================================================
function wCorrelacao(id) {
  const cvs = $(id), ctx = cvs.getContext('2d');
  let seed = 99, xs = [], zs = [];
  function generate() { const rng = makeRng(seed); xs = []; zs = []; for (let i = 0; i < 60; i++) { xs.push(rngNormal(rng)); zs.push(rngNormal(rng)); } }
  function draw() {
    const r = +$(id + '-r').value; $(id + '-r-v').textContent = r.toFixed(2); $(id + '-r2').textContent = (r * r).toFixed(3);
    const W = cvs.width, H = cvs.height; ctx.clearRect(0, 0, W, H);
    const pad = 30, plotW = W - pad * 2, plotH = H - pad * 2;
    const toX = x => pad + (x + 3) / 6 * plotW, toY = y => pad + plotH - (y + 3) / 6 * plotH;
    // y a partir dos MESMOS x,z (sem nova aleatoriedade)
    const ys = xs.map((x, i) => r * x + Math.sqrt(Math.max(0, 1 - r * r)) * zs[i]);
    ctx.strokeStyle = GRID(); ctx.beginPath(); ctx.moveTo(pad, toY(0)); ctx.lineTo(pad + plotW, toY(0)); ctx.stroke(); ctx.beginPath(); ctx.moveTo(toX(0), pad); ctx.lineTo(toX(0), pad + plotH); ctx.stroke();
    // resíduos (linha vertical do ponto até a reta y = r*x)
    ctx.strokeStyle = 'rgba(192,57,43,0.35)'; ctx.lineWidth = 1;
    for (let i = 0; i < xs.length; i++) { const yhat = r * xs[i]; ctx.beginPath(); ctx.moveTo(toX(xs[i]), toY(ys[i])); ctx.lineTo(toX(xs[i]), toY(yhat)); ctx.stroke(); }
    // reta
    ctx.beginPath(); ctx.moveTo(toX(-3), toY(-3 * r)); ctx.lineTo(toX(3), toY(3 * r)); ctx.strokeStyle = '#c0392b'; ctx.lineWidth = 1.8; ctx.stroke();
    // pontos
    ctx.fillStyle = 'rgba(50,102,173,0.7)';
    for (let i = 0; i < xs.length; i++) { ctx.beginPath(); ctx.arc(toX(xs[i]), toY(ys[i]), 3, 0, 7); ctx.fill(); }
    const fs = Math.max(9, Math.round(W * 0.015)); ctx.fillStyle = MUTED(); ctx.font = `${fs}px 'Courier New', monospace`; ctx.textAlign = 'left';
    ctx.fillText('linhas vermelhas = resíduos', pad + 4, pad + 12);
  }
  $(id + '-r').addEventListener('input', draw);
  $(id + '-redraw').addEventListener('click', () => { seed = (seed * 1103515245 + 12345) & 0x7fffffff; generate(); draw(); });
  generate(); makeResizer(cvs, 0.7, draw);
}

// ============================================================
// 9 — Valor-p (determinístico)
// ============================================================
function wValorP(id) {
  const cvs = $(id), ctx = cvs.getContext('2d');
  function draw() {
    const z = +$(id + '-z').value, bil = $(id + '-bil').checked;
    $(id + '-z-v').textContent = z.toFixed(2);
    const pUni = 1 - cdfN(Math.abs(z)), p = bil ? 2 * pUni : pUni;
    $(id + '-p').textContent = p < 0.0001 ? '< 0.0001' : p.toFixed(4);
    const W = cvs.width, H = cvs.height; ctx.clearRect(0, 0, W, H);
    const padL = 28, padR = 28, padT = 24, padB = 32, plotW = W - padL - padR, plotH = H - padT - padB;
    const xMin = -4, xMax = 4, baseY = padT + plotH, sY = plotH * 0.88, toX = v => padL + (v - xMin) / (xMax - xMin) * plotW;
    function shade(a, b, c) { ctx.beginPath(); ctx.moveTo(toX(a), baseY); for (let i = 0; i <= 200; i++) { const x = a + i / 200 * (b - a); ctx.lineTo(toX(x), baseY - pdfN(x) * sY); } ctx.lineTo(toX(b), baseY); ctx.closePath(); ctx.fillStyle = c; ctx.fill(); }
    const az = Math.abs(z); shade(az, xMax, 'rgba(192,57,43,0.35)'); if (bil) shade(xMin, -az, 'rgba(192,57,43,0.35)');
    ctx.beginPath(); for (let i = 0; i <= 500; i++) { const x = xMin + i / 500 * (xMax - xMin); const y = pdfN(x); i ? ctx.lineTo(toX(x), baseY - y * sY) : ctx.moveTo(toX(x), baseY - y * sY); } ctx.strokeStyle = '#3266ad'; ctx.lineWidth = 2; ctx.stroke();
    ctx.beginPath(); ctx.moveTo(padL, baseY); ctx.lineTo(W - padR, baseY); ctx.strokeStyle = GRID(); ctx.stroke();
    ctx.beginPath(); ctx.setLineDash([5, 4]); ctx.moveTo(toX(z), padT); ctx.lineTo(toX(z), baseY); ctx.strokeStyle = MUTED(); ctx.lineWidth = 1.5; ctx.stroke(); ctx.setLineDash([]);
    const fs = Math.max(10, Math.round(W * 0.018)); ctx.font = `${fs}px 'Courier New', monospace`; ctx.fillStyle = MUTED(); ctx.textAlign = 'center';
    for (let v = -4; v <= 4; v++) ctx.fillText(v.toFixed(0), toX(v), baseY + 16);
    ctx.fillStyle = INK(); ctx.font = `bold ${fs}px 'Courier New', monospace`; ctx.fillText('z = ' + z.toFixed(2), toX(z), padT - 4);
  }
  $(id + '-z').addEventListener('input', draw); $(id + '-bil').addEventListener('change', draw);
  makeResizer(cvs, 0.42, draw);
}

// ============================================================
// 10 — Histograma (seed fixo; só botão re-sorteia)
// ============================================================
function wHistograma(id) {
  const cvs = $(id), ctx = cvs.getContext('2d');
  let dist = 'uniforme', seed = 2024, data = [];
  const sizes = [10, 30, 100, 200, 500, 1000, 2000, 5000];
  function generate() {
    const N = sizes[+$(id + '-n').value - 1], rng = makeRng(seed); data = [];
    for (let i = 0; i < N; i++) data.push(dist === 'normal' ? rngNormal(rng) : rng() * 2 - 1);
  }
  function draw() {
    const N = sizes[+$(id + '-n').value - 1], bins = +$(id + '-bins').value;
    $(id + '-n-v').textContent = N.toLocaleString('pt-BR'); $(id + '-bins-v').textContent = bins;
    const W = cvs.width, H = cvs.height; ctx.clearRect(0, 0, W, H);
    const padL = 44, padR = 22, padT = 24, padB = 36, plotW = W - padL - padR, plotH = H - padT - padB;
    const xMin = dist === 'normal' ? -4 : -1.05, xMax = dist === 'normal' ? 4 : 1.05;
    const counts = new Array(bins).fill(0), bw = (xMax - xMin) / bins;
    for (const v of data) { const i = Math.min(bins - 1, Math.floor((v - xMin) / bw)); if (i >= 0 && i < bins) counts[i]++; }
    const maxC = Math.max(...counts, 1), toX = v => padL + (v - xMin) / (xMax - xMin) * plotW, toY = c => padT + plotH - c / maxC * plotH;
    const barCol = dist === 'normal' ? 'rgba(50,102,173,0.55)' : 'rgba(192,57,43,0.5)', lineCol = dist === 'normal' ? '#3266ad' : '#c0392b';
    for (let i = 0; i < bins; i++) { const x0 = toX(xMin + i * bw), x1 = toX(xMin + (i + 1) * bw); ctx.fillStyle = barCol; ctx.fillRect(x0 + 0.5, toY(counts[i]), x1 - x0 - 1, padT + plotH - toY(counts[i])); }
    ctx.beginPath(); ctx.strokeStyle = lineCol; ctx.lineWidth = 2;
    for (let px = 0; px <= plotW; px++) { const v = xMin + px / plotW * (xMax - xMin); let d = dist === 'normal' ? pdfN(v) : (v >= -1 && v <= 1 ? 0.5 : 0); const e = d * N * bw, y = padT + plotH - e / maxC * plotH; px ? ctx.lineTo(padL + px, y) : ctx.moveTo(padL + px, y); }
    ctx.stroke();
    const fs = Math.max(10, Math.round(W * 0.016)); ctx.font = `${fs}px 'Courier New', monospace`; ctx.fillStyle = MUTED(); ctx.textAlign = 'center';
    for (let i = 0; i <= 6; i++) { const v = xMin + i / 6 * (xMax - xMin); ctx.fillText(v.toFixed(1), toX(v), padT + plotH + 16); }
    $(id + '-mean').textContent = mean(data).toFixed(3); $(id + '-sd').textContent = sd(data).toFixed(3);
    ctx.fillStyle = lineCol; ctx.textAlign = 'right'; ctx.font = `bold ${fs}px 'Courier New', monospace`;
    ctx.fillText(dist === 'normal' ? 'Normal(0,1)' : 'Uniforme(−1,1)', padL + plotW, padT + 12);
  }
  $(id + '-n').addEventListener('input', () => { generate(); draw(); });
  $(id + '-bins').addEventListener('input', draw);
  document.querySelectorAll('[data-hist-dist="' + id + '"]').forEach(b => b.addEventListener('click', () => { dist = b.dataset.dist; document.querySelectorAll('[data-hist-dist="' + id + '"]').forEach(x => x.classList.toggle('active', x === b)); generate(); draw(); }));
  $(id + '-redraw').addEventListener('click', () => { seed = (seed * 1103515245 + 12345) & 0x7fffffff; generate(); draw(); });
  generate(); makeResizer(cvs, 0.45, draw);
}

// ============================================================
// 11 — Precisão e acurácia (4 cenários; seed fixo)
// ============================================================
function wPrecisao(id) {
  const cvs = $(id), ctx = cvs.getContext('2d');
  let seed = 11;
  function draw() {
    const vies = +$(id + '-bias').value, ruido = +$(id + '-noise').value;
    $(id + '-bias-v').textContent = vies.toFixed(1); $(id + '-noise-v').textContent = ruido.toFixed(1);
    const rng = makeRng(seed), W = cvs.width, H = cvs.height; ctx.clearRect(0, 0, W, H);
    const cx = W / 2, cy = H / 2, R = Math.min(W, H) * 0.42;
    // alvo
    for (let k = 4; k >= 1; k--) { ctx.beginPath(); ctx.arc(cx, cy, R * k / 4, 0, 7); ctx.fillStyle = k % 2 ? '#fff' : '#efe9dc'; ctx.fill(); ctx.strokeStyle = '#d4cdbd'; ctx.stroke(); }
    ctx.beginPath(); ctx.arc(cx, cy, 3, 0, 7); ctx.fillStyle = '#c0392b'; ctx.fill();
    // tiros: viés desloca centro, ruído espalha (mesma semente → slider não re-sorteia)
    const ang = -0.6, dx = Math.cos(ang) * vies * R / 6, dy = Math.sin(ang) * vies * R / 6;
    ctx.fillStyle = 'rgba(50,102,173,0.75)';
    for (let i = 0; i < 40; i++) {
      const px = cx + dx + rngNormal(rng) * ruido * R / 12;
      const py = cy + dy + rngNormal(rng) * ruido * R / 12;
      ctx.beginPath(); ctx.arc(px, py, 3.2, 0, 7); ctx.fill();
    }
    $(id + '-acc').textContent = vies < 0.7 ? 'Alta' : (vies < 2 ? 'Média' : 'Baixa');
    $(id + '-prec').textContent = ruido < 0.7 ? 'Alta' : (ruido < 2 ? 'Média' : 'Baixa');
  }
  $(id + '-bias').addEventListener('input', draw); $(id + '-noise').addEventListener('input', draw);
  $(id + '-redraw').addEventListener('click', () => { seed = (seed * 1103515245 + 12345) & 0x7fffffff; draw(); });
  makeResizer(cvs, 0.7, draw);
}

// ============================================================
// 12 — Tendência central: outlier move média/mediana/moda
// ============================================================
function wTendencia(id) {
  const cvs = $(id), ctx = cvs.getContext('2d');
  const base = [3, 4, 4, 5, 5, 5, 6, 6, 7]; // dados fixos
  function draw() {
    const out = +$(id + '-out').value; $(id + '-out-v').textContent = out.toFixed(0);
    const data = base.concat([out]).sort((a, b) => a - b);
    const m = mean(data), md = quantile(data, 0.5);
    // moda
    const freq = {}; let mode = data[0], best = 0;
    data.forEach(v => { freq[v] = (freq[v] || 0) + 1; if (freq[v] > best) { best = freq[v]; mode = v; } });
    $(id + '-mean').textContent = m.toFixed(2); $(id + '-median').textContent = md.toFixed(2); $(id + '-mode').textContent = mode.toFixed(0);
    const W = cvs.width, H = cvs.height; ctx.clearRect(0, 0, W, H);
    const padL = 30, padR = 30, padB = 40, padT = 20, plotW = W - padL - padR, baseY = H - padB;
    const xMin = 0, xMax = 25, toX = v => padL + (v - xMin) / (xMax - xMin) * plotW;
    ctx.beginPath(); ctx.moveTo(padL, baseY); ctx.lineTo(padL + plotW, baseY); ctx.strokeStyle = GRID(); ctx.stroke();
    // empilhar pontos
    const stack = {};
    ctx.fillStyle = 'rgba(50,102,173,0.8)';
    data.forEach(v => { stack[v] = (stack[v] || 0) + 1; const x = toX(v), y = baseY - 10 - (stack[v] - 1) * 14; ctx.beginPath(); ctx.arc(x, y, 5, 0, 7); ctx.fill(); });
    const fs = Math.max(10, Math.round(W * 0.016)); ctx.font = `${fs}px 'Courier New', monospace`; ctx.textAlign = 'center'; ctx.fillStyle = MUTED();
    for (let v = 0; v <= 25; v += 5) ctx.fillText(v, toX(v), baseY + 16);
    // linhas média / mediana
    function vline(v, color, label, off) { ctx.beginPath(); ctx.setLineDash([4, 3]); ctx.moveTo(toX(v), padT); ctx.lineTo(toX(v), baseY); ctx.strokeStyle = color; ctx.lineWidth = 2; ctx.stroke(); ctx.setLineDash([]); ctx.fillStyle = color; ctx.font = `bold ${fs}px 'Courier New', monospace`; ctx.fillText(label, toX(v), padT + off); }
    vline(m, '#c0392b', 'média', 0);
    vline(md, '#1a7a4a', 'mediana', 14);
  }
  $(id + '-out').addEventListener('input', draw);
  makeResizer(cvs, 0.5, draw);
}

// ============================================================
// 13 — Boxplot + histograma (seed fixo)
// ============================================================
function wBoxplot(id) {
  const cvs = $(id), ctx = cvs.getContext('2d');
  let seed = 55, data = [];
  function generate() {
    const skew = +$(id + '-skew').value, rng = makeRng(seed); data = [];
    for (let i = 0; i < 200; i++) { let v = rngNormal(rng); if (skew > 0) v = Math.exp(v * skew * 0.5) * 4 + 6; else v = v * 3 + 15; data.push(v); }
  }
  function draw() {
    const skew = +$(id + '-skew').value; $(id + '-skew-v').textContent = skew.toFixed(1);
    const sorted = [...data].sort((a, b) => a - b);
    const q1 = quantile(sorted, 0.25), md = quantile(sorted, 0.5), q3 = quantile(sorted, 0.75), iqr = q3 - q1;
    const lo = q1 - 1.5 * iqr, hi = q3 + 1.5 * iqr;
    const wLo = sorted.find(v => v >= lo), wHi = [...sorted].reverse().find(v => v <= hi);
    $(id + '-q1').textContent = q1.toFixed(1); $(id + '-med').textContent = md.toFixed(1); $(id + '-q3').textContent = q3.toFixed(1); $(id + '-iqr').textContent = iqr.toFixed(1);
    const W = cvs.width, H = cvs.height; ctx.clearRect(0, 0, W, H);
    const padL = 20, padR = 20, plotW = W - padL - padR;
    const xMin = Math.min(...sorted) - 1, xMax = Math.max(...sorted) + 1, toX = v => padL + (v - xMin) / (xMax - xMin) * plotW;
    // histograma em cima
    const histY0 = 20, histH = H * 0.42, bins = 30, bw = (xMax - xMin) / bins, counts = new Array(bins).fill(0);
    for (const v of sorted) { const i = Math.min(bins - 1, Math.floor((v - xMin) / bw)); counts[i]++; }
    const maxC = Math.max(...counts, 1);
    ctx.fillStyle = 'rgba(50,102,173,0.5)';
    for (let i = 0; i < bins; i++) { const x0 = toX(xMin + i * bw), x1 = toX(xMin + (i + 1) * bw), h = counts[i] / maxC * histH; ctx.fillRect(x0 + 0.5, histY0 + histH - h, x1 - x0 - 1, h); }
    // boxplot embaixo
    const by = H * 0.72, bh = H * 0.16;
    ctx.strokeStyle = INK(); ctx.lineWidth = 1.5;
    ctx.beginPath(); ctx.moveTo(toX(wLo), by); ctx.lineTo(toX(q1), by); ctx.moveTo(toX(q3), by); ctx.lineTo(toX(wHi), by); ctx.stroke();
    ctx.beginPath(); ctx.moveTo(toX(wLo), by - bh / 3); ctx.lineTo(toX(wLo), by + bh / 3); ctx.moveTo(toX(wHi), by - bh / 3); ctx.lineTo(toX(wHi), by + bh / 3); ctx.stroke();
    ctx.fillStyle = 'rgba(50,102,173,0.35)'; ctx.fillRect(toX(q1), by - bh / 2, toX(q3) - toX(q1), bh);
    ctx.strokeRect(toX(q1), by - bh / 2, toX(q3) - toX(q1), bh);
    ctx.beginPath(); ctx.moveTo(toX(md), by - bh / 2); ctx.lineTo(toX(md), by + bh / 2); ctx.strokeStyle = '#c0392b'; ctx.lineWidth = 2.5; ctx.stroke();
    // outliers
    ctx.fillStyle = '#c0392b';
    sorted.filter(v => v < lo || v > hi).forEach(v => { ctx.beginPath(); ctx.arc(toX(v), by, 3, 0, 7); ctx.fill(); });
    const fs = Math.max(9, Math.round(W * 0.015)); ctx.font = `${fs}px 'Courier New', monospace`; ctx.fillStyle = MUTED(); ctx.textAlign = 'center';
    ctx.fillText('Q1', toX(q1), by + bh); ctx.fillText('mediana', toX(md), by - bh); ctx.fillText('Q3', toX(q3), by + bh);
  }
  $(id + '-skew').addEventListener('input', () => { generate(); draw(); });
  $(id + '-redraw').addEventListener('click', () => { seed = (seed * 1103515245 + 12345) & 0x7fffffff; generate(); draw(); });
  generate(); makeResizer(cvs, 0.55, draw);
}

// ============================================================
// 14 — Hipóteses: distribuição sob H0 + estatística observada
// ============================================================
function wHipoteses(id) {
  const cvs = $(id), ctx = cvs.getContext('2d');
  function draw() {
    const obs = +$(id + '-obs').value, alpha = +$(id + '-alpha').value, bil = $(id + '-bil').checked;
    $(id + '-obs-v').textContent = obs.toFixed(2); $(id + '-alpha-v').textContent = alpha.toFixed(2);
    const zc = bil ? invCdfN(1 - alpha / 2) : invCdfN(1 - alpha);
    const pUni = 1 - cdfN(Math.abs(obs)), p = bil ? 2 * pUni : 1 - cdfN(obs);
    const rejeita = bil ? Math.abs(obs) > zc : obs > zc;
    $(id + '-p').textContent = p < 0.0001 ? '< 0.0001' : p.toFixed(4);
    $(id + '-dec').textContent = rejeita ? 'Rejeita H₀' : 'Não rejeita H₀';
    $(id + '-dec').style.color = rejeita ? '#c0392b' : '#1a7a4a';
    const W = cvs.width, H = cvs.height; ctx.clearRect(0, 0, W, H);
    const padL = 28, padR = 28, padT = 26, padB = 32, plotW = W - padL - padR, plotH = H - padT - padB;
    const xMin = -4, xMax = 4, baseY = padT + plotH, sY = plotH * 0.88, toX = v => padL + (v - xMin) / (xMax - xMin) * plotW;
    function shade(a, b, c) { ctx.beginPath(); ctx.moveTo(toX(a), baseY); for (let i = 0; i <= 150; i++) { const x = a + i / 150 * (b - a); ctx.lineTo(toX(x), baseY - pdfN(x) * sY); } ctx.lineTo(toX(b), baseY); ctx.closePath(); ctx.fillStyle = c; ctx.fill(); }
    // regiões de rejeição (alfa)
    shade(zc, xMax, 'rgba(192,57,43,0.25)'); if (bil) shade(xMin, -zc, 'rgba(192,57,43,0.25)');
    // curva H0
    ctx.beginPath(); for (let i = 0; i <= 500; i++) { const x = xMin + i / 500 * (xMax - xMin); const y = pdfN(x); i ? ctx.lineTo(toX(x), baseY - y * sY) : ctx.moveTo(toX(x), baseY - y * sY); } ctx.strokeStyle = '#3266ad'; ctx.lineWidth = 2; ctx.stroke();
    ctx.beginPath(); ctx.moveTo(padL, baseY); ctx.lineTo(W - padR, baseY); ctx.strokeStyle = GRID(); ctx.stroke();
    // estatística observada
    ctx.beginPath(); ctx.moveTo(toX(obs), padT - 6); ctx.lineTo(toX(obs), baseY); ctx.strokeStyle = rejeita ? '#c0392b' : '#1a7a4a'; ctx.lineWidth = 2.5; ctx.stroke();
    const fs = Math.max(10, Math.round(W * 0.018)); ctx.font = `bold ${fs}px 'Courier New', monospace`; ctx.textAlign = 'center';
    ctx.fillStyle = '#3266ad'; ctx.fillText('distribuição sob H₀', toX(0), padT + 4);
    ctx.fillStyle = rejeita ? '#c0392b' : '#1a7a4a'; ctx.fillText('obs', toX(obs), padT - 10);
    ctx.fillStyle = MUTED(); ctx.font = `${fs}px 'Courier New', monospace`;
    for (let v = -4; v <= 4; v += 2) ctx.fillText(v.toFixed(0), toX(v), baseY + 16);
  }
  $(id + '-obs').addEventListener('input', draw); $(id + '-alpha').addEventListener('input', draw); $(id + '-bil').addEventListener('change', draw);
  makeResizer(cvs, 0.45, draw);
}

// ============================================================
// 15 — ANOVA: 3 grupos (seed fixo; sliders movem sem re-sortear)
// ============================================================
function wANOVA(id) {
  const cvs = $(id), ctx = cvs.getContext('2d');
  let seed = 321, raw = [];
  function generate() { const rng = makeRng(seed); raw = []; for (let g = 0; g < 3; g++) { const arr = []; for (let i = 0; i < 12; i++) arr.push(rngNormal(rng)); raw.push(arr); } }
  function ibeta(x, a, b) {
    if (x <= 0) return 0; if (x >= 1) return 1;
    const lbeta = lgamma(a) + lgamma(b) - lgamma(a + b);
    const front = Math.exp(a * Math.log(x) + b * Math.log(1 - x) - lbeta) / a;
    let f = 1, c = 1, d = 0;
    for (let i = 0; i <= 200; i++) {
      const m = Math.floor(i / 2);
      let num;
      if (i === 0) num = 1;
      else if (i % 2 === 0) num = (m * (b - m) * x) / ((a + 2 * m - 1) * (a + 2 * m));
      else num = -((a + m) * (a + b + m) * x) / ((a + 2 * m) * (a + 2 * m + 1));
      d = 1 + num * d; if (Math.abs(d) < 1e-30) d = 1e-30; d = 1 / d;
      c = 1 + num / c; if (Math.abs(c) < 1e-30) c = 1e-30;
      f *= d * c; if (Math.abs(1 - d * c) < 1e-8) break;
    }
    return front * (f - 1);
  }
  function fSf(F, d1, d2) { if (F <= 0) return 1; return 1 - ibeta(d1 * F / (d1 * F + d2), d1 / 2, d2 / 2); }
  function fPdf(x, d1, d2) { if (x <= 0) return 0; const a = d1 / 2, b = d2 / 2; const lb = lgamma(a) + lgamma(b) - lgamma(a + b); return Math.exp(a * Math.log(d1 / d2) + (a - 1) * Math.log(x) - (a + b) * Math.log(1 + d1 / d2 * x) - lb); }
  function fInv(pp, d1, d2) { let lo = 0, hi = 200, mid; for (let i = 0; i < 60; i++) { mid = (lo + hi) / 2; fSf(mid, d1, d2) > pp ? lo = mid : hi = mid; } return mid; }
  function hexA(hex, a) { const n = parseInt(hex.slice(1), 16); return `rgba(${(n >> 16) & 255},${(n >> 8) & 255},${n & 255},${a})`; }
  function draw() {
    const sep = +$(id + '-sep').value, spread = +$(id + '-spread').value;
    $(id + '-sep-v').textContent = sep.toFixed(1); $(id + '-spread-v').textContent = spread.toFixed(1);
    const centros = [10 - sep, 10, 10 + sep];
    const groups = raw.map((arr, g) => arr.map(z => centros[g] + z * spread));
    const all = groups.flat(), grand = mean(all), k = 3, N = all.length, d1 = k - 1, d2 = N - k;
    let ssb = 0, ssw = 0;
    groups.forEach(g => { const m = mean(g); ssb += g.length * (m - grand) ** 2; g.forEach(v => ssw += (v - m) ** 2); });
    const F = (ssb / d1) / (ssw / d2), p = fSf(F, d1, d2);
    $(id + '-F').textContent = F.toFixed(2);
    $(id + '-p').textContent = p < 0.0001 ? '< 0.0001' : p.toFixed(4);
    $(id + '-sig').textContent = p < 0.05 ? 'Significativo' : 'Não signif.';
    $(id + '-sig').style.color = p < 0.05 ? '#c0392b' : '#1a7a4a';

    const W = cvs.width, H = cvs.height; ctx.clearRect(0, 0, W, H);
    const gap = 26, leftW = (W - gap) * 0.52, rightW = (W - gap) * 0.48, rx0 = leftW + gap;

    // ----- painel esquerdo: dotplots -----
    const padL = 30, padT = 18, padB = 30, plotH = H - padT - padB, plotW = leftW - padL - 8;
    const yMin = 2, yMax = 18, toY = v => padT + plotH - (v - yMin) / (yMax - yMin) * plotH;
    ctx.beginPath(); ctx.moveTo(padL, padT); ctx.lineTo(padL, padT + plotH); ctx.lineTo(padL + plotW, padT + plotH); ctx.strokeStyle = GRID(); ctx.stroke();
    const cols = ['#3266ad', '#c0392b', '#1a7a4a'], names = ['A', 'B', 'C'];
    const fs = Math.max(9, Math.round(W * 0.014));
    groups.forEach((g, gi) => {
      const cx = padL + plotW * (gi + 0.5) / 3;
      g.forEach((v, i) => { const jx = cx + ((i % 5) - 2) * 6; ctx.fillStyle = hexA(cols[gi], 0.6); ctx.beginPath(); ctx.arc(jx, toY(v), 3, 0, 7); ctx.fill(); });
      const m = mean(g); ctx.strokeStyle = cols[gi]; ctx.lineWidth = 2.5; ctx.beginPath(); ctx.moveTo(cx - 26, toY(m)); ctx.lineTo(cx + 26, toY(m)); ctx.stroke();
      ctx.fillStyle = cols[gi]; ctx.font = `bold ${fs}px 'Courier New', monospace`; ctx.textAlign = 'center'; ctx.fillText(names[gi], cx, padT + plotH + 16);
    });
    ctx.fillStyle = MUTED(); ctx.font = `${fs}px 'Courier New', monospace`; ctx.textAlign = 'center';
    ctx.fillText('os 3 grupos', padL + plotW / 2, padT - 4);

    // ----- painel direito: distribuição F -----
    const rPadT = 18, rPadB = 30, rPlotH = H - rPadT - rPadB, rPlotW = rightW - 12, baseY = rPadT + rPlotH;
    const xMax = Math.max(6, F * 1.2);
    const toRX = x => rx0 + x / xMax * rPlotW;
    let maxY = 0; for (let i = 1; i <= 200; i++) { maxY = Math.max(maxY, fPdf(i / 200 * xMax, d1, d2)); }
    const toRY = y => baseY - y / maxY * rPlotH * 0.9;
    // área-p (cauda à direita de F)
    ctx.beginPath(); ctx.moveTo(toRX(F), baseY);
    for (let i = 0; i <= 120; i++) { const x = F + i / 120 * (xMax - F); ctx.lineTo(toRX(x), toRY(fPdf(x, d1, d2))); }
    ctx.lineTo(toRX(xMax), baseY); ctx.closePath(); ctx.fillStyle = 'rgba(192,57,43,0.30)'; ctx.fill();
    // curva F
    ctx.beginPath();
    for (let i = 1; i <= 300; i++) { const x = i / 300 * xMax; const y = fPdf(x, d1, d2); i === 1 ? ctx.moveTo(toRX(x), toRY(y)) : ctx.lineTo(toRX(x), toRY(y)); }
    ctx.strokeStyle = '#3266ad'; ctx.lineWidth = 2; ctx.stroke();
    ctx.beginPath(); ctx.moveTo(rx0, baseY); ctx.lineTo(rx0 + rPlotW, baseY); ctx.strokeStyle = GRID(); ctx.stroke();
    // F crítico (5%) tracejado
    const fc = fInv(0.05, d1, d2);
    if (fc < xMax) { ctx.beginPath(); ctx.setLineDash([4, 3]); ctx.moveTo(toRX(fc), rPadT); ctx.lineTo(toRX(fc), baseY); ctx.strokeStyle = MUTED(); ctx.lineWidth = 1.2; ctx.stroke(); ctx.setLineDash([]); }
    // F observado
    ctx.beginPath(); ctx.moveTo(toRX(F), rPadT); ctx.lineTo(toRX(F), baseY); ctx.strokeStyle = '#c0392b'; ctx.lineWidth = 2; ctx.stroke();
    ctx.fillStyle = '#c0392b'; ctx.font = `bold ${fs}px 'Courier New', monospace`; ctx.textAlign = 'center';
    ctx.fillText('F = ' + F.toFixed(2), toRX(F), rPadT - 4 < 12 ? 26 : rPadT + 8);
    ctx.fillStyle = MUTED(); ctx.font = `${fs}px 'Courier New', monospace`;
    ctx.fillText('distribuição F sob H₀', rx0 + rPlotW / 2, baseY + 16);
    if (fc < xMax) { ctx.fillText('F* (5%)', toRX(fc), baseY + 16); }
  }
  $(id + '-sep').addEventListener('input', draw); $(id + '-spread').addEventListener('input', draw);
  $(id + '-redraw').addEventListener('click', () => { seed = (seed * 1103515245 + 12345) & 0x7fffffff; generate(); draw(); });
  generate(); makeResizer(cvs, 0.42, draw);
}

// ============================================================
// Distribuições t / χ² / F (interativas, determinísticas)
// ============================================================
function wDistAmostral(id) {
  const cvs = $(id), ctx = cvs.getContext('2d');
  let tipo = 't';
  function pdf(x, df, df2) {
    if (tipo === 't') { const c = Math.exp(lgamma((df + 1) / 2) - lgamma(df / 2)) / Math.sqrt(df * Math.PI); return c * Math.pow(1 + x * x / df, -(df + 1) / 2); }
    if (tipo === 'chi2') { if (x <= 0) return 0; return Math.exp((df / 2 - 1) * Math.log(x) - x / 2 - (df / 2) * Math.log(2) - lgamma(df / 2)); }
    if (tipo === 'f') { if (x <= 0) return 0; const a = df / 2, b = df2 / 2; const lb = lgamma(a) + lgamma(b) - lgamma(a + b); return Math.exp(a * Math.log(df / df2) + (a - 1) * Math.log(x) - (a + b) * Math.log(1 + df / df2 * x) - lb); }
    return 0;
  }
  function draw() {
    const df = +$(id + '-df').value, df2 = +$(id + '-df2').value;
    $(id + '-df-v').textContent = df; $(id + '-df2-v').textContent = df2;
    const W = cvs.width, H = cvs.height; ctx.clearRect(0, 0, W, H);
    const padL = 30, padR = 20, padT = 20, padB = 30, plotW = W - padL - padR, plotH = H - padT - padB, baseY = padT + plotH;
    const xMin = tipo === 't' ? -5 : 0, xMax = tipo === 't' ? 5 : (tipo === 'chi2' ? 30 : 6);
    const toX = v => padL + (v - xMin) / (xMax - xMin) * plotW;
    let maxY = 0; for (let i = 0; i <= 200; i++) { const x = xMin + i / 200 * (xMax - xMin); maxY = Math.max(maxY, pdf(x, df, df2)); }
    const toY = y => baseY - y / maxY * plotH * 0.92;
    // normal de referência (para t)
    if (tipo === 't') { ctx.beginPath(); for (let i = 0; i <= 300; i++) { const x = xMin + i / 300 * (xMax - xMin); i ? ctx.lineTo(toX(x), toY(pdfN(x))) : ctx.moveTo(toX(x), toY(pdfN(x))); } ctx.strokeStyle = '#1a7a4a'; ctx.setLineDash([4, 3]); ctx.lineWidth = 1.5; ctx.stroke(); ctx.setLineDash([]); }
    ctx.beginPath(); for (let i = 0; i <= 300; i++) { const x = xMin + i / 300 * (xMax - xMin); const y = pdf(x, df, df2); i ? ctx.lineTo(toX(x), toY(y)) : ctx.moveTo(toX(x), toY(y)); } ctx.strokeStyle = '#c0392b'; ctx.lineWidth = 2; ctx.stroke();
    ctx.beginPath(); ctx.moveTo(padL, baseY); ctx.lineTo(padL + plotW, baseY); ctx.strokeStyle = GRID(); ctx.stroke();
    const fs = Math.max(10, Math.round(W * 0.016)); ctx.font = `${fs}px 'Courier New', monospace`; ctx.fillStyle = MUTED(); ctx.textAlign = 'center';
    for (let i = 0; i <= 6; i++) { const v = xMin + i / 6 * (xMax - xMin); ctx.fillText(v.toFixed(0), toX(v), baseY + 16); }
    if (tipo === 't') { ctx.fillStyle = '#1a7a4a'; ctx.textAlign = 'right'; ctx.font = `bold ${fs}px 'Courier New', monospace`; ctx.fillText('normal', padL + plotW, padT + 12); }
  }
  document.querySelectorAll('[data-dist="' + id + '"]').forEach(b => b.addEventListener('click', () => {
    tipo = b.dataset.tipo; document.querySelectorAll('[data-dist="' + id + '"]').forEach(x => x.classList.toggle('active', x === b));
    $(id + '-df2row').style.display = tipo === 'f' ? '' : 'none'; draw();
  }));
  $(id + '-df').addEventListener('input', draw); $(id + '-df2').addEventListener('input', draw);
  $(id + '-df2row').style.display = 'none';
  makeResizer(cvs, 0.45, draw);
}

// ============================================================
// Calculadora de potência (t, ANOVA, χ², proporções)
// ============================================================
function wPotenciaCalc(id) {
  const cvs = $(id), ctx = cvs.getContext('2d');
  let teste = 't';
  // potência analítica para cada teste, dado n POR GRUPO
  function poder(n) {
    const alpha = +$(id + '-alpha').value, ef = +$(id + '-ef').value;
    if (teste === 't') {                       // 2 amostras, d de Cohen
      const ncp = ef * Math.sqrt(n / 2), zc = invCdfN(1 - alpha / 2);
      return cdfN(ncp - zc) + cdfN(-ncp - zc);
    }
    if (teste === 'prop') {                     // 2 proporções, h de Cohen
      const ncp = ef * Math.sqrt(n / 2), zc = invCdfN(1 - alpha / 2);
      return cdfN(ncp - zc) + cdfN(-ncp - zc);
    }
    if (teste === 'anova') {                     // k grupos, f de Cohen
      const k = +$(id + '-k').value, N = n * k, df = k - 1, lam = ef * ef * N;
      return ncChi2sf(chi2inv(1 - alpha, df), df, lam);
    }
    if (teste === 'chi2') {                       // qui-quadrado, w de Cohen, n = N total
      const df = +$(id + '-df').value, lam = ef * ef * n;
      return ncChi2sf(chi2inv(1 - alpha, df), df, lam);
    }
    return 0;
  }
  function nLabel() { return teste === 'chi2' ? 'N total' : 'n por grupo'; }
  function efLabel() {
    return teste === 't' ? "tamanho de efeito (d de Cohen)" :
      teste === 'anova' ? "tamanho de efeito (f de Cohen)" :
      teste === 'chi2' ? "tamanho de efeito (w de Cohen)" :
      "tamanho de efeito (h de Cohen)";
  }
  function draw() {
    const n = +$(id + '-n').value, alpha = +$(id + '-alpha').value, ef = +$(id + '-ef').value;
    $(id + '-n-lbl').textContent = nLabel();
    $(id + '-ef-lbl').textContent = efLabel();
    $(id + '-n-v').textContent = n; $(id + '-alpha-v').textContent = alpha.toFixed(2); $(id + '-ef-v').textContent = ef.toFixed(2);
    $(id + '-k-v').textContent = $(id + '-k').value; $(id + '-df-v').textContent = $(id + '-df').value;
    $(id + '-k-row').style.display = teste === 'anova' ? '' : 'none';
    $(id + '-df-row').style.display = teste === 'chi2' ? '' : 'none';
    const pw = poder(n);
    $(id + '-pw').textContent = (pw * 100).toFixed(1) + '%';
    // n necessário para 80%
    let n80 = null;
    for (let nn = 2; nn <= 2000; nn++) { if (poder(nn) >= 0.8) { n80 = nn; break; } }
    $(id + '-n80').textContent = n80 ? n80 : '> 2000';

    const W = cvs.width, H = cvs.height; ctx.clearRect(0, 0, W, H);
    const padL = 44, padR = 16, padT = 18, padB = 34, plotW = W - padL - padR, plotH = H - padT - padB;
    const nMax = 200, toX = v => padL + v / nMax * plotW, toY = pp => padT + plotH - pp * plotH;
    // grade y
    ctx.strokeStyle = GRIDSOFT(); ctx.fillStyle = MUTED(); ctx.font = "11px 'Courier New', monospace"; ctx.textAlign = 'right';
    for (let g = 0; g <= 1.0001; g += 0.25) { const y = toY(g); ctx.beginPath(); ctx.moveTo(padL, y); ctx.lineTo(padL + plotW, y); ctx.stroke(); ctx.fillText((g * 100).toFixed(0) + '%', padL - 6, y + 4); }
    // linha 80%
    ctx.beginPath(); ctx.setLineDash([4, 3]); ctx.moveTo(padL, toY(0.8)); ctx.lineTo(padL + plotW, toY(0.8)); ctx.strokeStyle = '#1a7a4a'; ctx.lineWidth = 1.3; ctx.stroke(); ctx.setLineDash([]);
    // curva poder vs n
    ctx.beginPath(); ctx.strokeStyle = '#3266ad'; ctx.lineWidth = 2.2;
    for (let nn = 2; nn <= nMax; nn++) { const pp = poder(nn); nn === 2 ? ctx.moveTo(toX(nn), toY(pp)) : ctx.lineTo(toX(nn), toY(pp)); }
    ctx.stroke();
    // ponto atual
    if (n <= nMax) { ctx.fillStyle = '#c0392b'; ctx.beginPath(); ctx.arc(toX(n), toY(pw), 4, 0, 7); ctx.fill();
      ctx.beginPath(); ctx.setLineDash([3, 3]); ctx.moveTo(toX(n), padT); ctx.lineTo(toX(n), padT + plotH); ctx.strokeStyle = 'rgba(192,57,43,0.5)'; ctx.lineWidth = 1; ctx.stroke(); ctx.setLineDash([]); }
    // eixos x
    ctx.strokeStyle = GRID(); ctx.beginPath(); ctx.moveTo(padL, padT + plotH); ctx.lineTo(padL + plotW, padT + plotH); ctx.stroke();
    ctx.fillStyle = MUTED(); ctx.textAlign = 'center'; ctx.font = "11px 'Courier New', monospace";
    for (let v = 0; v <= nMax; v += 50) ctx.fillText(v, toX(v), padT + plotH + 16);
    ctx.fillText(nLabel(), padL + plotW / 2, padT + plotH + 30);
    ctx.fillStyle = '#1a7a4a'; ctx.textAlign = 'left'; ctx.fillText('poder 80%', padL + 6, toY(0.8) - 5);
  }
  document.querySelectorAll('[data-pot="' + id + '"]').forEach(b => b.addEventListener('click', () => {
    teste = b.dataset.teste; document.querySelectorAll('[data-pot="' + id + '"]').forEach(x => x.classList.toggle('active', x === b)); draw();
  }));
  ['n', 'alpha', 'ef', 'k', 'df'].forEach(key => $(id + '-' + key).addEventListener('input', draw));
  makeResizer(cvs, 0.5, draw);
}

// ============================================================
// Tabs + sidebar runtime
// ============================================================
function showTopic(target) {
  document.querySelectorAll('.topic').forEach(t => t.classList.toggle('active', t.id === target));
  document.querySelectorAll('.nav-link').forEach(a => a.classList.toggle('active', a.dataset.target === target));
  window.dispatchEvent(new Event('resize'));
}

window.addEventListener('DOMContentLoaded', () => {
  // inicializa widgets
  document.querySelectorAll('[data-widget]').forEach(el => {
    const fn = window[el.dataset.widget];
    if (typeof fn === 'function') { try { fn(el.dataset.id); } catch (e) { console.error('widget', el.dataset.widget, e); } }
  });

  // navegação por links da sidebar (mesma página)
  document.querySelectorAll('.nav-link[data-target]').forEach(a => {
    a.addEventListener('click', e => {
      e.preventDefault();
      const target = a.dataset.target;
      showTopic(target);
      history.replaceState(null, '', '#' + target);
      const el = document.getElementById(target);
      if (el) window.scrollTo({ top: 0, behavior: 'smooth' });
      // fecha sidebar no mobile
      document.querySelector('.sidebar')?.classList.remove('open');
    });
  });

  // ativa pelo hash, senão o primeiro tópico
  const hash = window.location.hash.slice(1);
  if (hash && document.getElementById(hash)) showTopic(hash);
  else { const first = document.querySelector('.topic'); if (first) showTopic(first.id); }

  // toggle sidebar mobile
  document.getElementById('menuToggle')?.addEventListener('click', () => {
    document.querySelector('.sidebar')?.classList.toggle('open');
  });

  // colapsar/expandir grupos da sidebar
  document.querySelectorAll('.nav-group-title').forEach(t => {
    t.addEventListener('click', () => t.parentElement.classList.toggle('collapsed'));
  });

  // alternar tema claro/escuro
  document.getElementById('themeToggle')?.addEventListener('click', () => {
    const dark = document.documentElement.getAttribute('data-theme') === 'dark';
    if (dark) document.documentElement.removeAttribute('data-theme');
    else document.documentElement.setAttribute('data-theme', 'dark');
    try { localStorage.setItem('tema', dark ? 'light' : 'dark'); } catch (e) {}
    // repinta os widgets (canvas) com as novas cores
    window.dispatchEvent(new Event('resize'));
  });
});
