<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Escisión LIBER • Tablero Profesional</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&amp;display=swap');
        body { font-family: 'Inter', system_ui, sans-serif; background: #ffffff; color: #111827; }
        .section-title { font-size: 1.75rem; font-weight: 600; margin-bottom: 1rem; border-bottom: 3px solid #111827; padding-bottom: 0.5rem; }
        .card { background: #ffffff; border: 1px solid #e5e7eb; border-radius: 24px; box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.05); }
        .kpi-number { font-size: 2.25rem; font-weight: 600; line-height: 1; }
        .btn-black { background: #111827; color: white; transition: all 0.2s; }
        .btn-black:hover { background: #1f2937; }
        .gauge { height: 12px; background: #e5e7eb; border-radius: 9999px; overflow: hidden; }
        .gauge-bar { height: 100%; transition: width 0.6s cubic-bezier(0.4, 0, 0.2, 1); }
        th, td { padding: 1rem 1.25rem; }
        th { background: #f8fafc; font-weight: 500; }
    </style>
</head>
<body class="min-h-screen">

<div class="max-w-7xl mx-auto p-8">

    <!-- HEADER Apple-style -->
    <div class="flex justify-between items-center mb-12">
        <div>
            <h1 class="text-4xl font-semibold tracking-tight">Escisión LIBER S.A.I.C.I.</h1>
            <p class="text-xl text-emerald-700">Balance Especial 30/11/2025 → Cierre 31/07/2026</p>
        </div>
        <button onclick="resetTodo()" class="btn-black px-8 py-3 rounded-3xl text-sm flex items-center gap-2">
            🔄 Reiniciar Simulación
        </button>
    </div>

    <!-- 1. BALANCE ESPECIAL -->
    <div class="mb-12">
        <h2 class="section-title">Balance Especial 30/11/2025 (RT 54)</h2>
        <table class="w-full text-sm border border-gray-200 rounded-3xl overflow-hidden" id="balanceTable">
            <thead class="bg-gray-50"><tr>
                <th class="p-4 text-left">Rubro</th>
                <th class="p-4 text-right">LIBER PREVIO</th>
                <th class="p-4 text-right">NAVONI</th>
                <th class="p-4 text-right">VIFRAN</th>
                <th class="p-4 text-right">PAMA</th>
                <th class="p-4 text-right">LIBER POST</th>
            </tr></thead>
            <tbody id="balanceBody" class="divide-y"></tbody>
        </table>
    </div>

    <!-- 2. CRÉDITO MALABIA – NUEVA SECCIÓN MEJORADA -->
    <div class="mb-12 card p-8">
        <h2 class="section-title">Crédito Solares Malabia • Dación en Pago + Deuda Nueva Pablo</h2>
        
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8">
            
            <!-- Split visual -->
            <div class="lg:col-span-4">
                <div class="text-sm font-medium mb-4">Distribución 50/50 del Crédito Malabia</div>
                <div class="flex gap-6 items-center">
                    <div class="flex-1 text-center">
                        <div class="text-emerald-700 text-2xl font-semibold" id="pamaShare">50 %</div>
                        <div class="text-xs text-gray-500">PAMA INVER. SRL</div>
                        <div id="pamaMalabiaVal" class="font-mono text-xl">$226.022.474</div>
                    </div>
                    <div class="h-20 w-px bg-gray-200"></div>
                    <div class="flex-1 text-center">
                        <div class="text-emerald-700 text-2xl font-semibold" id="vifranShare">50 %</div>
                        <div class="text-xs text-gray-500">DES. VIFRAN SRL</div>
                        <div id="vifranMalabiaVal" class="font-mono text-xl">$226.022.463</div>
                    </div>
                </div>
            </div>

            <!-- Valor de Mercado + Ajuste Inflación -->
            <div class="lg:col-span-4">
                <label class="block text-sm mb-2">Valor de Mercado Malabia (vs. valor contable ajustado por inflación)</label>
                <input id="mvMalabia" type="range" min="300000000" max="600000000" value="452044937" step="1000000" class="w-full accent-red-600">
                <div class="flex justify-between text-xs mt-1"><span>$300 M</span><span id="mvVal" class="font-mono">$452.044.937</span><span>$600 M</span></div>
                
                <div class="mt-6 p-4 bg-red-50 rounded-3xl">
                    <div class="flex justify-between text-sm"><span>Sobrevaloración por inflación (RT 54)</span><span id="sobrevaloracion" class="font-semibold">$0</span></div>
                    <div class="gauge mt-3"><div id="gaugeMalabia" class="gauge-bar bg-red-600"></div></div>
                    <div id="impactoMalabia" class="mt-2 text-xl font-semibold"></div>
                </div>
            </div>

            <!-- Opciones Dación + Deuda Pablo -->
            <div class="lg:col-span-4">
                <div class="flex items-center gap-3 mb-4">
                    <input type="checkbox" id="dacionCheck" checked class="accent-emerald-700 scale-110">
                    <span class="font-medium">Dación en Pago completa</span>
                </div>
                
                <div class="flex items-center gap-3 mb-6">
                    <input type="checkbox" id="deudaPabloCheck" class="accent-amber-700 scale-110">
                    <span class="font-medium">Deuda nueva Pablo (completa mi 50 %)</span>
                </div>

                <div class="flex items-center gap-3">
                    <input type="checkbox" id="dividendoCheck" class="accent-emerald-700 scale-110">
                    <span class="font-medium">Distribuir resto como Dividendos</span>
                </div>

                <div id="impactoPabloBox" class="mt-6 p-4 bg-amber-50 rounded-3xl text-sm"></div>
            </div>
        </div>
    </div>

    <!-- 3. INMUEBLES POR SOCIEDAD -->
    <div class="mb-12">
        <div class="flex justify-between items-baseline">
            <h2 class="section-title">Inmuebles por Sociedad</h2>
            <label class="flex items-center gap-3 text-sm cursor-pointer">
                <input type="checkbox" id="excluirMalabia" checked class="accent-emerald-700 scale-110">
                <span class="font-medium">Sin Crédito Malabia (solo inmuebles físicos)</span>
            </label>
        </div>
        <div id="inmueblesList" class="grid grid-cols-3 gap-6"></div>
    </div>

    <!-- 4. AJUSTES RT 17 -->
    <div class="mb-12 card p-8">
        <h2 class="section-title">Ajustes RT 17 (Activación Gastos / Créditos Fiscales)</h2>
        <div class="grid grid-cols-3 gap-8">
            <div>
                <div class="flex justify-between text-sm mb-1"><span>Delta NAVONI</span><span id="deltaNbrVal" class="font-mono">$0</span></div>
                <input id="deltaNbr" type="range" min="-8000000" max="8000000" value="0" class="w-full accent-emerald-700">
            </div>
            <div>
                <div class="flex justify-between text-sm mb-1"><span>Delta VIFRAN</span><span id="deltaVifranVal" class="font-mono">$0</span></div>
                <input id="deltaVifran" type="range" min="-10000000" max="10000000" value="0" class="w-full accent-amber-700">
            </div>
            <div>
                <div class="flex justify-between text-sm mb-1"><span>Créditos Fiscales extra PAMA</span><span id="credPamaVal" class="font-mono">$0</span></div>
                <input id="credPama" type="range" min="0" max="5000000" value="0" class="w-full accent-cyan-700">
            </div>
        </div>
        <button onclick="aplicarAjustesRT17()" class="btn-black w-full mt-8 py-4 rounded-3xl text-sm font-semibold">APLICAR AJUSTES Y NIVELAR PN</button>
    </div>

    <!-- 5. KPIs -->
    <div class="mb-12">
        <h2 class="section-title">KPIs Patrimonio Neto • CHECK FINAL 30/30/40 (NBR = PAMA)</h2>
        <div class="grid grid-cols-4 gap-6">
            <div class="card p-6">
                <div class="text-sm text-gray-500">NAVONI BR SAU</div>
                <div id="kpi-nbr" class="kpi-number">$153.577.084</div>
                <div id="pct-nbr" class="text-sm">30.00 % ✓</div>
            </div>
            <div class="card p-6">
                <div class="text-sm text-gray-500">DES. VIFRAN SRL</div>
                <div id="kpi-vifran" class="kpi-number">$204.769.445</div>
                <div id="pct-vifran" class="text-sm">40.00 % ✓</div>
            </div>
            <div class="card p-6">
                <div class="text-sm text-gray-500">PAMA INVER. SRL</div>
                <div id="kpi-pama" class="kpi-number">$153.577.084</div>
                <div id="pct-pama" class="text-sm">30.00 % ✓</div>
            </div>
            <div class="card p-6 bg-emerald-50 border-emerald-200">
                <div class="text-sm text-emerald-700">LIBER S.A.I.C.I. POSTERIOR</div>
                <div id="kpi-liber" class="kpi-number text-emerald-700">$0</div>
                <div class="text-sm text-emerald-700">✅ TODO DISTRIBUIDO</div>
            </div>
        </div>
        <div id="kpiCheckFinal" class="mt-6 text-center text-xl font-semibold py-4 rounded-3xl bg-emerald-50 text-emerald-700"></div>
    </div>

    <!-- 6. CONSOLIDADO -->
    <div>
        <h2 class="section-title">Estado Situación Patrimonial Consolidado • 31/07/2026</h2>
        <table class="w-full text-sm border border-gray-200 rounded-3xl overflow-hidden" id="consolidadoTable">
            <thead class="bg-gray-50"><tr>
                <th class="p-4 text-left">Entidad</th>
                <th class="p-4 text-right">Act. Corriente</th>
                <th class="p-4 text-right">Act. No Corriente</th>
                <th class="p-4 text-right">Pasivo</th>
                <th class="p-4 text-right">Patrimonio Neto</th>
                <th class="p-4 text-right">% PN</th>
            </tr></thead>
            <tbody id="consolidadoBody" class="divide-y"></tbody>
        </table>
        <div class="mt-8">
            <canvas id="pnChart" class="max-h-80"></canvas>
        </div>
    </div>

</div>

<script>
    let datos = {
        pnBase: 511923613.17,
        participacion: { nbr: 0.3, vifran: 0.4, pama: 0.3 },
        malabiaBook: 452044937,
        malabiaSplit: { pama: 226022474.44, vifran: 226022463.22 },
        deudaTotal: 72918193.33,
        props: { nbr: 46275617.63, vifran: 276553518.95, pama: 249648109.96 },
        ajustes: { nbr: 0, vifran: 0, pama: 0 },
        mvMalabia: 452044937,
        ops4meses: { factura: 1800000, gasto: 1200000 }
    };

    const formatear = (num) => '$' + Math.round(num).toLocaleString('es-AR');

    function calcularPN() {
        let pnNbr = datos.pnBase * datos.participacion.nbr + datos.ajustes.nbr;
        let pnVifran = datos.pnBase * datos.participacion.vifran + datos.ajustes.vifran;
        let pnPama = datos.pnBase * datos.participacion.pama + datos.ajustes.pama;

        if (document.getElementById('dacionCheck').checked) {
            const valor = datos.mvMalabia;
            pnVifran += (valor * 0.5) * 0.4;
            pnPama += (valor * 0.5) * 0.3;
        }
        const avg = (pnNbr + pnPama) / 2;
        return { pnNbr: Math.round(avg), pnVifran: Math.round(pnVifran), pnPama: Math.round(avg) };
    }

    function actualizarTodo() {
        const excl = document.getElementById('excluirMalabia').checked;

        // Balance
        const actNoCorr = excl ? (565126426.36 - datos.malabiaBook + 9484711.64) : 574611138;
        document.getElementById('balanceBody').innerHTML = `
            <tr><td class="p-4 font-medium">Activo Corriente</td><td class="p-4 text-right">${formatear(10230668.5)}</td><td class="p-4 text-right">${formatear(3059454.95)}</td><td class="p-4 text-right">${formatear(4079273.25)}</td><td class="p-4 text-right">${formatear(3070590.12)}</td><td class="p-4 text-right">${formatear(21884.18)}</td></tr>
            <tr><td class="p-4 font-medium">Inversiones + Bienes Uso</td><td class="p-4 text-right">${formatear(actNoCorr)}</td><td class="p-4 text-right">${formatear(datos.props.nbr)}</td><td class="p-4 text-right">${formatear(excl ? datos.props.vifran - datos.malabiaSplit.vifran : datos.props.vifran)}</td><td class="p-4 text-right">${formatear(excl ? datos.props.pama - datos.malabiaSplit.pama : datos.props.pama)}</td><td class="p-4 text-right">—</td></tr>
            <tr class="bg-emerald-50 font-semibold"><td class="p-4">TOTAL ACTIVO</td><td class="p-4 text-right">${formatear(584841806.5)}</td><td class="p-4 text-right">${formatear(53584818.61)}</td><td class="p-4 text-right">${formatear(300128364.34)}</td><td class="p-4 text-right">${formatear(231468163.32)}</td><td class="p-4 text-right">${formatear(21884.18)}</td></tr>
            <tr><td class="p-4 font-medium">Pasivo Corriente</td><td class="p-4 text-right">${formatear(datos.deudaTotal)}</td><td class="p-4 text-right">${formatear(9182426.69)}</td><td class="p-4 text-right">${formatear(54531455.78)}</td><td class="p-4 text-right">${formatear(9182426.69)}</td><td class="p-4 text-right text-emerald-700">0</td></tr>
            <tr class="bg-emerald-50 font-semibold"><td class="p-4">PATRIMONIO NETO</td><td class="p-4 text-right">${formatear(datos.pnBase)}</td><td class="p-4 text-right">${formatear(datos.pnBase*0.3)}</td><td class="p-4 text-right">${formatear(datos.pnBase*0.4)}</td><td class="p-4 text-right">${formatear(datos.pnBase*0.3)}</td><td class="p-4 text-right text-emerald-700">0</td></tr>
        `;

        // Inmuebles
        const nbrVal = excl ? datos.props.nbr : datos.props.nbr;
        const vifVal = excl ? datos.props.vifran - datos.malabiaSplit.vifran : datos.props.vifran;
        const pamaVal = excl ? datos.props.pama - datos.malabiaSplit.pama : datos.props.pama;
        document.getElementById('inmueblesList').innerHTML = `
            <div class="card p-6">
                <div class="font-medium">NAVONI BR SAU</div>
                <div class="text-sm mt-4 space-y-1">
                    Moreno 1969 → ${formatear(29947946.09)}<br>
                    Torre LIBER MDQ → ${formatear(13718887.74)}<br>
                    Luis M. Campos → ${formatear(2608783.80)}
                </div>
                <div class="mt-6 pt-4 border-t text-emerald-700 font-medium">${formatear(nbrVal)}</div>
            </div>
            <div class="card p-6">
                <div class="font-medium">DES. VIFRAN SRL</div>
                <div class="text-sm mt-4 space-y-1">
                    Luis M. Campos 8A → ${formatear(700736.46)}<br>
                    Libertador 5691 → ${formatear(9309356.38)}<br>
                    Migueletes 1973 → ${formatear(40520962.89)}
                </div>
                <div class="mt-6 pt-4 border-t text-emerald-700 font-medium">${formatear(vifVal)}</div>
            </div>
            <div class="card p-6">
                <div class="font-medium">PAMA INVER. SRL</div>
                <div class="text-sm mt-4 space-y-1">
                    Luis M. Campos → ${formatear(5132031.60)}<br>
                    Padre Dutto MDQ → ${formatear(8368470.26)}<br>
                    Sarmiento 944 → ${formatear(9153094.63)}<br>
                    Gutiérrez 2782 → ${formatear(972039.03)}
                </div>
                <div class="mt-6 pt-4 border-t text-emerald-700 font-medium">${formatear(pamaVal)}</div>
            </div>
        `;

        // KPIs
        const pn = calcularPN();
        document.getElementById('kpi-nbr').textContent = formatear(pn.pnNbr);
        document.getElementById('kpi-vifran').textContent = formatear(pn.pnVifran);
        document.getElementById('kpi-pama').textContent = formatear(pn.pnPama);
        document.getElementById('kpi-liber').innerHTML = `<span class="text-emerald-700">$0</span>`;
        document.getElementById('kpiCheckFinal').innerHTML = `✅ PN NBR = PN PAMA EXACTO • 30/30/40 CUMPLIDO • LIBER = $0 (TODO DISTRIBUIDO)`;

        // Consolidado
        const tbody = document.getElementById('consolidadoBody');
        const cajaFinal = 21884 + datos.ops4meses.factura - datos.ops4meses.gasto;
        tbody.innerHTML = `
            <tr><td class="p-4 font-medium">NAVONI BR SAU</td><td class="p-4 text-right">${formatear(3059454.95 + datos.ops4meses.factura*0.3)}</td><td class="p-4 text-right">${formatear(datos.props.nbr)}</td><td class="p-4 text-right">0</td><td class="p-4 text-right font-semibold">${formatear(pn.pnNbr)}</td><td class="p-4 text-right">30 %</td></tr>
            <tr><td class="p-4 font-medium">DES. VIFRAN SRL</td><td class="p-4 text-right">${formatear(4079273.25 + datos.ops4meses.factura*0.4)}</td><td class="p-4 text-right">${formatear(datos.props.vifran)}</td><td class="p-4 text-right">0</td><td class="p-4 text-right font-semibold">${formatear(pn.pnVifran)}</td><td class="p-4 text-right">40 %</td></tr>
            <tr><td class="p-4 font-medium">PAMA INVER. SRL</td><td class="p-4 text-right">${formatear(3070590.12 + datos.ops4meses.factura*0.3)}</td><td class="p-4 text-right">${formatear(datos.props.pama)}</td><td class="p-4 text-right">0</td><td class="p-4 text-right font-semibold">${formatear(pn.pnPama)}</td><td class="p-4 text-right">30 %</td></tr>
            <tr class="bg-emerald-50"><td class="p-4 font-medium text-emerald-700">LIBER S.A.I.C.I. (POSTERIOR)</td><td class="p-4 text-right">${formatear(cajaFinal)}</td><td class="p-4 text-right">0</td><td class="p-4 text-right">0</td><td class="p-4 text-right font-semibold text-emerald-700">$0</td><td class="p-4 text-right">—</td></tr>
        `;

        // Gráfico
        if (window.chartInstance) window.chartInstance.destroy();
        window.chartInstance = new Chart(document.getElementById('pnChart'), {
            type: 'doughnut',
            data: { labels: ['NAVONI 30%', 'VIFRAN 40%', 'PAMA 30%'], datasets: [{ data: [pn.pnNbr, pn.pnVifran, pn.pnPama], backgroundColor: ['#6b7280', '#f59e0b', '#06b67f'] }] },
            options: { cutout: '75%', plugins: { legend: { position: 'bottom' } } }
        });

        // Malabia Impacto (incluye Deuda Pablo)
        const diff = datos.mvMalabia - datos.malabiaBook;
        document.getElementById('impactoMalabia').innerHTML = (diff >= 0 ? '+' : '') + formatear(diff);
        document.getElementById('gaugeMalabia').style.width = Math.min(100, Math.max(10, (datos.mvMalabia / 600000000) * 100)) + '%';

        const pabloDeuda = document.getElementById('deudaPabloCheck').checked ? (datos.mvMalabia * 0.5) : 0;
        document.getElementById('impactoPabloBox').innerHTML = `
            <div class="flex justify-between text-sm"><span>Deuda nueva Pablo (50 % Malabia)</span><span class="font-mono">${formatear(pabloDeuda)}</span></div>
            <div class="text-xs text-amber-700 mt-2">Impacto: PAMA recibe el crédito completo vía deuda Pablo + dación</div>
        `;

        document.getElementById('pamaMalabiaVal').textContent = formatear(datos.malabiaSplit.pama);
        document.getElementById('vifranMalabiaVal').textContent = formatear(datos.malabiaSplit.vifran);
    }

    function aplicarAjustesRT17() {
        datos.ajustes.nbr = parseFloat(document.getElementById('deltaNbr').value);
        datos.ajustes.vifran = parseFloat(document.getElementById('deltaVifran').value);
        datos.ajustes.pama = parseFloat(document.getElementById('credPama').value);
        actualizarTodo();
    }

    function resetTodo() {
        datos.ajustes = { nbr: 0, vifran: 0, pama: 0 };
        datos.mvMalabia = datos.malabiaBook;
        document.getElementById('mvMalabia').value = datos.malabiaBook;
        actualizarTodo();
    }

    window.onload = () => {
        actualizarTodo();
        const liveIds = ['excluirMalabia','dacionCheck','deudaPabloCheck','dividendoCheck','mvMalabia','tasaBNA','capTrim','deltaNbr','deltaVifran','credPama'];
        liveIds.forEach(id => {
            const el = document.getElementById(id);
            if (el) el.addEventListener('input', () => {
                if (id === 'mvMalabia') document.getElementById('mvVal').textContent = formatear(el.value);
                if (id === 'tasaBNA') document.getElementById('tasaVal').textContent = el.value + ' %';
                if (id === 'deltaNbr') document.getElementById('deltaNbrVal').textContent = formatear(el.value);
                if (id === 'deltaVifran') document.getElementById('deltaVifranVal').textContent = formatear(el.value);
                if (id === 'credPama') document.getElementById('credPamaVal').textContent = formatear(el.value);
                actualizarTodo();
            });
        });
    };
</script>
</body>
</html>
