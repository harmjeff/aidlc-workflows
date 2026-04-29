#!/usr/bin/env python3
"""Generate interactive HTML report with charts for git-compare results."""

import json
from pathlib import Path


def generate_interactive_html_report(
    scenarios: list[str],
    version_names: list[str],
    all_results: list[dict],
    generated_at: str,
    runs_dir: Path,
) -> str:
    """Generate an interactive HTML report with charts and navigation.

    Args:
        scenarios: List of scenario names
        version_names: List of version names in order
        all_results: List of run result dicts with version_name, scenario, output_dir, etc.
        generated_at: ISO timestamp of report generation
        runs_dir: Path to runs directory for loading metrics

    Returns:
        HTML string
    """
    from run_git_compare import (
        load_run_metrics,
        get_metric_value,
        METRIC_ROWS,
    )

    # Collect metrics per version per scenario
    scenario_data = {}
    for scenario_name in scenarios:
        scenario_results = [r for r in all_results if r["scenario"] == scenario_name]
        if not scenario_results:
            continue

        # Group by version
        version_metrics = {vn: [] for vn in version_names}
        for result in scenario_results:
            vn = result["version_name"]
            folder = Path(result["output_dir"])
            if folder.is_dir():
                metrics = load_run_metrics(folder)
                if metrics:
                    version_metrics[vn].append(metrics)

        scenario_data[scenario_name] = version_metrics

    # Compute aggregated metrics for charts
    chart_data = _prepare_chart_data(version_names, scenario_data, scenarios)

    # Generate HTML
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Git Version Comparison Report</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            line-height: 1.6;
            color: #333;
            background: #f5f5f5;
        }}

        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 2rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}

        .header h1 {{
            font-size: 2rem;
            margin-bottom: 0.5rem;
        }}

        .header .meta {{
            opacity: 0.9;
            font-size: 0.9rem;
        }}

        .container {{
            max-width: 1400px;
            margin: 0 auto;
            padding: 2rem;
        }}

        .tabs {{
            display: flex;
            gap: 0.5rem;
            margin-bottom: 2rem;
            flex-wrap: wrap;
        }}

        .tab {{
            padding: 0.75rem 1.5rem;
            background: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 0.95rem;
            font-weight: 500;
            transition: all 0.2s;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }}

        .tab:hover {{
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }}

        .tab.active {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            box-shadow: 0 4px 8px rgba(0,0,0,0.15);
        }}

        .tab-content {{
            display: none;
        }}

        .tab-content.active {{
            display: block;
        }}

        .card {{
            background: white;
            border-radius: 12px;
            padding: 2rem;
            margin-bottom: 2rem;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }}

        .card h2 {{
            margin-bottom: 1.5rem;
            color: #667eea;
            font-size: 1.5rem;
        }}

        .chart-container {{
            position: relative;
            height: 400px;
            margin-bottom: 2rem;
        }}

        .metrics-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1.5rem;
            margin-bottom: 2rem;
        }}

        .metric-card {{
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            padding: 1.5rem;
            border-radius: 8px;
            text-align: center;
        }}

        .metric-card h3 {{
            font-size: 0.9rem;
            color: #666;
            margin-bottom: 0.5rem;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}

        .metric-card .value {{
            font-size: 2rem;
            font-weight: bold;
            color: #333;
        }}

        .metric-card .delta {{
            font-size: 0.9rem;
            margin-top: 0.5rem;
        }}

        .delta.better {{
            color: #10b981;
        }}

        .delta.worse {{
            color: #ef4444;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 1rem;
        }}

        th, td {{
            padding: 0.75rem;
            text-align: left;
            border-bottom: 1px solid #e5e7eb;
        }}

        th {{
            background: #f9fafb;
            font-weight: 600;
            color: #374151;
        }}

        tr:hover {{
            background: #f9fafb;
        }}

        .version-badge {{
            display: inline-block;
            padding: 0.25rem 0.75rem;
            background: #667eea;
            color: white;
            border-radius: 12px;
            font-size: 0.85rem;
            font-weight: 500;
        }}

        .status-pass {{
            color: #10b981;
            font-weight: 600;
        }}

        .status-fail {{
            color: #ef4444;
            font-weight: 600;
        }}

        .legend {{
            display: flex;
            gap: 2rem;
            margin-top: 1.5rem;
            padding: 1rem;
            background: #f9fafb;
            border-radius: 8px;
            font-size: 0.9rem;
        }}

        .legend-item {{
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}

        .legend-color {{
            width: 20px;
            height: 20px;
            border-radius: 4px;
        }}

        @media (max-width: 768px) {{
            .container {{
                padding: 1rem;
            }}

            .header {{
                padding: 1rem;
            }}

            .header h1 {{
                font-size: 1.5rem;
            }}

            .tabs {{
                flex-direction: column;
            }}

            .tab {{
                width: 100%;
            }}

            .chart-container {{
                height: 300px;
            }}
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>🚀 Git Version Comparison Report</h1>
        <div class="meta">
            <div>Generated: {generated_at}</div>
            <div>Versions: {', '.join(version_names)}</div>
            <div>Scenarios: {', '.join(scenarios)}</div>
        </div>
    </div>

    <div class="container">
        <div class="tabs">
            <button class="tab active" onclick="switchTab('overview')">Overview</button>
            <button class="tab" onclick="switchTab('performance')">Performance</button>
            <button class="tab" onclick="switchTab('quality')">Code Quality</button>
            <button class="tab" onclick="switchTab('tests')">Testing</button>
            <button class="tab" onclick="switchTab('artifacts')">Artifacts</button>
            <button class="tab" onclick="switchTab('raw-data')">Raw Data</button>
        </div>

        <div id="overview" class="tab-content active">
            {_generate_overview_section(version_names, chart_data, scenarios)}
        </div>

        <div id="performance" class="tab-content">
            {_generate_performance_section(version_names, chart_data)}
        </div>

        <div id="quality" class="tab-content">
            {_generate_quality_section(version_names, chart_data)}
        </div>

        <div id="tests" class="tab-content">
            {_generate_tests_section(version_names, chart_data)}
        </div>

        <div id="artifacts" class="tab-content">
            {_generate_artifacts_section(version_names, chart_data)}
        </div>

        <div id="raw-data" class="tab-content">
            {_generate_raw_data_section(version_names, scenario_data, scenarios, all_results)}
        </div>
    </div>

    <script>
        const chartData = {json.dumps(chart_data, indent=2)};

        function switchTab(tabName) {{
            // Hide all tabs
            document.querySelectorAll('.tab-content').forEach(content => {{
                content.classList.remove('active');
            }});
            document.querySelectorAll('.tab').forEach(button => {{
                button.classList.remove('active');
            }});

            // Show selected tab
            document.getElementById(tabName).classList.add('active');
            event.target.classList.add('active');
        }}

        // Chart colors
        const colors = [
            'rgb(102, 126, 234)',
            'rgb(237, 100, 166)',
            'rgb(16, 185, 129)',
            'rgb(251, 146, 60)',
            'rgb(139, 92, 246)',
            'rgb(236, 72, 153)',
        ];

        // Color scale function: maps value to color gradient (red -> yellow -> green)
        function getColorForValue(value, minVal, maxVal, higherIsBetter) {{
            if (value === null || minVal === null || maxVal === null) {{
                return 'rgb(156, 163, 175)'; // Gray for null
            }}

            // Normalize value to 0-1 range
            const range = maxVal - minVal;
            let normalized = range > 0 ? (value - minVal) / range : 0.5;

            // Invert for "lower is better" metrics
            if (!higherIsBetter) {{
                normalized = 1 - normalized;
            }}

            // Color gradient: red (0) -> yellow (0.5) -> green (1)
            let r, g, b;
            if (normalized < 0.5) {{
                // Red to Yellow
                const t = normalized * 2; // 0 to 1
                r = 239; // Red stays high
                g = Math.round(68 + (234 - 68) * t); // Green increases
                b = 68; // Blue stays low
            }} else {{
                // Yellow to Green
                const t = (normalized - 0.5) * 2; // 0 to 1
                r = Math.round(234 - (234 - 16) * t); // Red decreases
                g = Math.round(234 - (234 - 185) * t); // Green adjusts
                b = Math.round(68 + (129 - 68) * t); // Blue increases
            }}

            return `rgb(${{r}}, ${{g}}, ${{b}})`;
        }}

        // Error bar plugin for 95% confidence intervals
        const errorBarPlugin = {{
            id: 'errorBars',
            afterDatasetsDraw(chart, args, options) {{
                const ctx = chart.ctx;
                chart.data.datasets.forEach((dataset, datasetIndex) => {{
                    const meta = chart.getDatasetMeta(datasetIndex);
                    if (!meta.visible || !dataset.ci95) return;

                    meta.data.forEach((point, index) => {{
                        const value = dataset.data[index];
                        const ci = dataset.ci95[index];

                        if (value === null || ci === null || ci === 0) return;

                        const x = point.x;
                        const yScale = chart.scales.y;
                        const yTop = yScale.getPixelForValue(value + ci);
                        const yBottom = yScale.getPixelForValue(value - ci);
                        const yCenter = point.y;

                        // Draw vertical line (error bar)
                        ctx.save();
                        ctx.strokeStyle = 'rgba(0, 0, 0, 0.5)';
                        ctx.lineWidth = 2;
                        ctx.beginPath();
                        ctx.moveTo(x, yTop);
                        ctx.lineTo(x, yBottom);
                        ctx.stroke();

                        // Draw top cap
                        const capWidth = 8;
                        ctx.beginPath();
                        ctx.moveTo(x - capWidth / 2, yTop);
                        ctx.lineTo(x + capWidth / 2, yTop);
                        ctx.stroke();

                        // Draw bottom cap
                        ctx.beginPath();
                        ctx.moveTo(x - capWidth / 2, yBottom);
                        ctx.lineTo(x + capWidth / 2, yBottom);
                        ctx.stroke();

                        ctx.restore();
                    }});
                }});
            }}
        }};

        function createLineChart(canvasId, title, metricKey, higherIsBetter) {{
            const ctx = document.getElementById(canvasId);
            if (!ctx) return;

            const data = chartData[metricKey];
            if (!data) return;

            // Calculate y-axis range including 95% CI bars with 10% padding
            let allMinValues = [];
            let allMaxValues = [];
            data.scenarios.forEach((scenario, scenarioIdx) => {{
                data.versions.forEach((version, versionIdx) => {{
                    const point = data.values[versionIdx][scenarioIdx];
                    if (point && point.avg !== null) {{
                        const avg = point.avg;
                        const ci = point.ci || 0;
                        // Include 95% CI bar extents
                        allMinValues.push(avg - ci);
                        allMaxValues.push(avg + ci);
                    }}
                }});
            }});

            let yMin = 0;
            let yMax = 100;
            if (allMinValues.length > 0 && allMaxValues.length > 0) {{
                const dataMin = Math.min(...allMinValues);
                const dataMax = Math.max(...allMaxValues);
                const range = dataMax - dataMin;

                // If all values are the same, add minimum padding of 10% of value
                const padding = range > 0 ? range * 0.1 : dataMax * 0.1;

                yMin = Math.max(0, dataMin - padding);
                yMax = dataMax + padding;
            }}

            // Transpose data: x-axis shows versions, each scenario is a line
            const datasets = data.scenarios.map((scenario, scenarioIdx) => {{
                const dataPoints = data.versions.map((version, versionIdx) => {{
                    const point = data.values[versionIdx][scenarioIdx];
                    return point ? point.avg : null;
                }});

                // Find min and max for color scaling
                const validValues = dataPoints.filter(v => v !== null);
                const minValue = validValues.length > 0 ? Math.min(...validValues) : null;
                const maxValue = validValues.length > 0 ? Math.max(...validValues) : null;

                // Baseline is first version (for tooltip comparison)
                const baseline = dataPoints[0];

                // Color scale from red (worst) to yellow to green (best)
                const pointColors = dataPoints.map((value, idx) => {{
                    return getColorForValue(value, minValue, maxValue, higherIsBetter);
                }});

                return {{
                    label: scenario,
                    data: dataPoints,
                    ci95: data.versions.map((version, versionIdx) => {{
                        const point = data.values[versionIdx][scenarioIdx];
                        return point ? point.ci : null;
                    }}),
                    sampleSize: data.versions.map((version, versionIdx) => {{
                        const point = data.values[versionIdx][scenarioIdx];
                        return point ? point.n : null;
                    }}),
                    borderColor: 'rgb(0, 0, 0)',  // Black lines
                    backgroundColor: pointColors,
                    pointBackgroundColor: pointColors,
                    pointBorderColor: pointColors,
                    pointBorderWidth: 2,
                    borderWidth: 2,
                    pointRadius: 6,
                    pointHoverRadius: 8,
                    tension: 0.1,
                }};
            }});

            new Chart(ctx, {{
                type: 'line',
                data: {{
                    labels: data.versions,
                    datasets: datasets,
                }},
                options: {{
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {{
                        title: {{
                            display: true,
                            text: title,
                            font: {{ size: 16, weight: 'bold' }},
                        }},
                        legend: {{
                            display: data.scenarios.length > 1,
                            position: 'top',
                        }},
                        tooltip: {{
                            callbacks: {{
                                label: function(context) {{
                                    let label = context.dataset.label || '';
                                    if (label && data.scenarios.length > 1) {{
                                        label += ': ';
                                    }} else {{
                                        label = '';
                                    }}
                                    const value = context.parsed.y;
                                    const ci = context.dataset.ci95[context.dataIndex];
                                    const n = context.dataset.sampleSize[context.dataIndex];

                                    if (value !== null) {{
                                        label += value.toFixed(2);
                                        if (ci !== null && ci > 0) {{
                                            const lower = value - ci;
                                            const upper = value + ci;
                                            label += ` (95% CI: ${{lower.toFixed(2)}}-${{upper.toFixed(2)}})`;
                                        }}
                                        if (n !== null && n > 1) {{
                                            label += ` n=${{n}}`;
                                        }}

                                        // Show better/worse indicator
                                        if (context.dataIndex > 0) {{
                                            const baseline = context.dataset.data[0];
                                            if (baseline !== null) {{
                                                const diff = value - baseline;
                                                const pctChange = (diff / baseline) * 100;
                                                const isBetter = higherIsBetter
                                                    ? value > baseline
                                                    : value < baseline;
                                                const indicator = isBetter ? '🟢' : '🔴';
                                                label += ` ${{indicator}} ${{pctChange > 0 ? '+' : ''}}${{pctChange.toFixed(1)}}%`;
                                            }}
                                        }}
                                    }}
                                    return label;
                                }},
                            }},
                        }},
                    }},
                    scales: {{
                        y: {{
                            min: yMin,
                            max: yMax,
                            title: {{
                                display: true,
                                text: title,
                            }},
                        }},
                        x: {{
                            title: {{
                                display: true,
                                text: 'Version',
                            }},
                            ticks: {{
                                maxRotation: 45,
                                minRotation: 45,
                            }},
                        }},
                    }},
                }},
                plugins: [errorBarPlugin],
            }});
        }}

        // Initialize all charts
        {_generate_chart_init_calls()}
    </script>
</body>
</html>"""

    return html


def _get_t_critical(n: int, confidence: float = 0.95) -> float:
    """Get t-critical value for confidence interval.

    Uses t-distribution for small samples, z for large samples.
    For 95% CI (two-tailed).
    """
    if n < 2:
        return 1.0

    # t-critical values for 95% CI (two-tailed, α=0.05)
    t_table = {
        2: 12.706,
        3: 4.303,
        4: 3.182,
        5: 2.776,
        6: 2.571,
        7: 2.447,
        8: 2.365,
        9: 2.306,
        10: 2.262,
        15: 2.145,
        20: 2.086,
        30: 2.045,
    }

    # Use lookup table or approximate for large n
    if n in t_table:
        return t_table[n]
    elif n > 30:
        return 1.96  # z-value for 95% CI with large samples
    else:
        # Interpolate or use closest value
        return 2.0


def _prepare_chart_data(version_names: list[str], scenario_data: dict, scenarios: list[str]) -> dict:
    """Prepare chart data structure for all metrics."""
    from run_git_compare import get_metric_value, METRIC_ROWS, _mean, _stdev
    import math

    chart_data = {}

    # Key metrics to chart
    chart_metrics = [
        ("tests_pass_pct", "Unit Test Pass %", True),
        ("contract_passed", "Contract Tests Passed", True),
        ("qualitative_score", "Qualitative Score", True),
        ("wall_clock_min", "Execution Time (min)", False),
        ("total_tokens", "Total Tokens", False),
        ("lint_total", "Lint Findings", False),
        ("security_total", "Security Findings", False),
        ("lines_of_code", "Lines of Code", True),
    ]

    for metric_key, metric_name, higher_is_better in chart_metrics:
        chart_data[metric_key] = {
            "name": metric_name,
            "higher_is_better": higher_is_better,
            "versions": version_names,
            "scenarios": scenarios,
            "values": [],  # One entry per version
        }

        for vn in version_names:
            version_data = []
            for scenario in scenarios:
                if scenario not in scenario_data:
                    version_data.append({"avg": None, "std": None})
                    continue

                mlist = scenario_data[scenario].get(vn, [])
                vals = [v for v in (get_metric_value(m, metric_key) for m in mlist) if v is not None]

                if not vals:
                    version_data.append({"avg": None, "ci": None, "n": 0})
                elif len(vals) == 1:
                    version_data.append({"avg": vals[0], "ci": None, "n": 1})
                else:
                    n = len(vals)
                    avg = _mean(vals)
                    std = _stdev(vals)
                    # Calculate 95% confidence interval: t * (std / sqrt(n))
                    t_crit = _get_t_critical(n)
                    sem = std / math.sqrt(n)
                    ci_half_width = t_crit * sem
                    version_data.append({"avg": avg, "ci": ci_half_width, "n": n})

            chart_data[metric_key]["values"].append(version_data)

    return chart_data


def _generate_overview_section(version_names: list[str], chart_data: dict, scenarios: list[str]) -> str:
    """Generate overview section HTML."""
    from run_git_compare import get_metric_value, _mean, _stdev

    # Calculate key metrics
    baseline = version_names[0] if version_names else None

    html = '<div class="card">'
    html += '<h2>📊 Overview</h2>'
    html += '<div class="metrics-grid">'

    # Show key metrics for each version
    for idx, vn in enumerate(version_names):
        qualitative = chart_data.get("qualitative_score", {})
        if qualitative and qualitative["values"]:
            scores = [v["avg"] for v in qualitative["values"][idx] if v["avg"] is not None]
            avg_score = sum(scores) / len(scores) if scores else 0

            delta_html = ""
            if idx > 0 and baseline:
                baseline_scores = [v["avg"] for v in qualitative["values"][0] if v["avg"] is not None]
                baseline_avg = sum(baseline_scores) / len(baseline_scores) if baseline_scores else 0
                delta = avg_score - baseline_avg
                if abs(delta) > 0.001:
                    delta_class = "better" if delta > 0 else "worse"
                    delta_html = f'<div class="delta {delta_class}">{delta:+.3f} vs {baseline}</div>'

            html += f'''
            <div class="metric-card">
                <h3>{vn}</h3>
                <div class="value">{avg_score:.3f}</div>
                <div style="font-size: 0.85rem; color: #666; margin-top: 0.25rem;">Qualitative Score</div>
                {delta_html}
            </div>
            '''

    html += '</div>'

    # Add summary table
    html += '<h3 style="margin-top: 2rem; margin-bottom: 1rem;">Key Metrics Summary</h3>'
    html += '<table><thead><tr><th>Metric</th>'
    for vn in version_names:
        html += f'<th>{vn}</th>'
    html += '</tr></thead><tbody>'

    # Key metrics to show
    summary_metrics = [
        ("qualitative_score", "Qualitative Score", 3),
        ("tests_pass_pct", "Unit Test Pass %", 1),
        ("contract_passed", "Contract Tests Passed", 0),
        ("wall_clock_min", "Execution Time (min)", 1),
        ("total_tokens", "Total Tokens", 0),
        ("lines_of_code", "Lines of Code", 0),
    ]

    for metric_key, metric_name, decimals in summary_metrics:
        html += f'<tr><td><strong>{metric_name}</strong></td>'
        metric_data = chart_data.get(metric_key, {})
        if metric_data and metric_data.get("values"):
            for idx in range(len(version_names)):
                # Get the first scenario's data for this version (usually only one scenario)
                version_data = metric_data["values"][idx]
                if version_data and len(version_data) > 0:
                    point = version_data[0]  # First scenario
                    if point["avg"] is None:
                        html += '<td>—</td>'
                    elif point["ci"] is None or point["ci"] == 0:
                        html += f'<td>{point["avg"]:.{decimals}f}</td>'
                    else:
                        lower = point["avg"] - point["ci"]
                        upper = point["avg"] + point["ci"]
                        html += f'<td>{point["avg"]:.{decimals}f}<br><span style="font-size: 0.85em; color: #666;">(95% CI: {lower:.{decimals}f}-{upper:.{decimals}f})</span></td>'
                else:
                    html += '<td>—</td>'
        else:
            for _ in version_names:
                html += '<td>—</td>'
        html += '</tr>'

    html += '</tbody></table>'

    # Key metrics charts
    html += '<div class="chart-container"><canvas id="chart-overview-quality"></canvas></div>'
    html += '<div class="chart-container"><canvas id="chart-overview-performance"></canvas></div>'

    html += '</div>'
    return html


def _generate_performance_section(version_names: list[str], chart_data: dict) -> str:
    """Generate performance section HTML."""
    html = '<div class="card">'
    html += '<h2>⚡ Performance Metrics</h2>'
    html += '<div class="chart-container"><canvas id="chart-perf-time"></canvas></div>'
    html += '<div class="chart-container"><canvas id="chart-perf-tokens"></canvas></div>'
    html += '<div class="chart-container"><canvas id="chart-perf-context"></canvas></div>'
    html += '</div>'
    return html


def _generate_quality_section(version_names: list[str], chart_data: dict) -> str:
    """Generate code quality section HTML."""
    html = '<div class="card">'
    html += '<h2>🔍 Code Quality</h2>'
    html += '<div class="chart-container"><canvas id="chart-quality-lint"></canvas></div>'
    html += '<div class="chart-container"><canvas id="chart-quality-security"></canvas></div>'
    html += '<div class="chart-container"><canvas id="chart-quality-qualitative"></canvas></div>'
    html += '</div>'
    return html


def _generate_tests_section(version_names: list[str], chart_data: dict) -> str:
    """Generate testing section HTML."""
    html = '<div class="card">'
    html += '<h2>✅ Testing Metrics</h2>'
    html += '<div class="chart-container"><canvas id="chart-tests-unit"></canvas></div>'
    html += '<div class="chart-container"><canvas id="chart-tests-contract"></canvas></div>'
    html += '</div>'
    return html


def _generate_artifacts_section(version_names: list[str], chart_data: dict) -> str:
    """Generate artifacts section HTML."""
    html = '<div class="card">'
    html += '<h2>📦 Generated Artifacts</h2>'
    html += '<div class="chart-container"><canvas id="chart-artifacts-loc"></canvas></div>'
    html += '<div class="chart-container"><canvas id="chart-artifacts-files"></canvas></div>'
    html += '</div>'
    return html


def _generate_raw_data_section(version_names: list[str], scenario_data: dict, scenarios: list[str], all_results: list[dict]) -> str:
    """Generate raw data section HTML."""
    from run_git_compare import get_metric_value, _mean, _stdev

    html = '<div class="card">'
    html += '<h2>📋 Raw Data</h2>'

    for scenario in scenarios:
        html += f'<h3 style="margin-top: 2rem; margin-bottom: 1rem;">{scenario}</h3>'
        html += '<table><thead><tr><th>Metric</th>'

        for vn in version_names:
            html += f'<th>{vn}</th>'

        html += '</tr></thead><tbody>'

        # Key metrics
        metrics_to_show = [
            ("tests_pass_pct", "Unit Test Pass %", 1),
            ("tests_passed", "Unit Tests Passed", 0),
            ("contract_passed", "Contract Tests Passed", 0),
            ("qualitative_score", "Qualitative Score", 3),
            ("wall_clock_min", "Execution Time (min)", 1),
            ("total_tokens", "Total Tokens", 0),
            ("lines_of_code", "Lines of Code", 0),
        ]

        for metric_key, metric_name, decimals in metrics_to_show:
            html += f'<tr><td><strong>{metric_name}</strong></td>'

            for vn in version_names:
                if scenario not in scenario_data:
                    html += '<td>—</td>'
                    continue

                mlist = scenario_data[scenario].get(vn, [])
                vals = [v for v in (get_metric_value(m, metric_key) for m in mlist) if v is not None]

                if not vals:
                    html += '<td>—</td>'
                elif len(vals) == 1:
                    html += f'<td>{vals[0]:.{decimals}f}</td>'
                else:
                    avg = _mean(vals)
                    std = _stdev(vals)
                    html += f'<td>{avg:.{decimals}f} ± {std:.{decimals}f}</td>'

            html += '</tr>'

        html += '</tbody></table>'

    # Run status table
    html += '<h3 style="margin-top: 2rem; margin-bottom: 1rem;">Run Status</h3>'
    html += '<table><thead><tr><th>Version</th><th>Scenario</th><th>Run</th><th>Status</th><th>Duration</th><th>Output</th></tr></thead><tbody>'

    for result in sorted(all_results, key=lambda x: (x["version_name"], x["scenario"], x["run_index"])):
        status_class = "status-pass" if result["status"] == "success" else "status-fail"
        duration = result.get("elapsed_seconds", 0) / 60
        html += f'''
        <tr>
            <td><span class="version-badge">{result["version_name"]}</span></td>
            <td>{result["scenario"]}</td>
            <td>{result["run_index"]}</td>
            <td class="{status_class}">{result["status"].upper()}</td>
            <td>{duration:.1f} min</td>
            <td style="font-size: 0.8rem; max-width: 300px; overflow: hidden; text-overflow: ellipsis;">{result["output_dir"]}</td>
        </tr>
        '''

    html += '</tbody></table>'
    html += '</div>'
    return html


def _generate_chart_init_calls() -> str:
    """Generate JavaScript calls to initialize all charts."""
    return """
        createLineChart('chart-overview-quality', 'Qualitative Score', 'qualitative_score', true);
        createLineChart('chart-overview-performance', 'Execution Time (min)', 'wall_clock_min', false);
        createLineChart('chart-perf-time', 'Execution Time (min)', 'wall_clock_min', false);
        createLineChart('chart-perf-tokens', 'Total Tokens', 'total_tokens', false);
        createLineChart('chart-quality-lint', 'Lint Findings', 'lint_total', false);
        createLineChart('chart-quality-security', 'Security Findings', 'security_total', false);
        createLineChart('chart-quality-qualitative', 'Qualitative Score', 'qualitative_score', true);
        createLineChart('chart-tests-unit', 'Unit Test Pass %', 'tests_pass_pct', true);
        createLineChart('chart-tests-contract', 'Contract Tests Passed', 'contract_passed', true);
        createLineChart('chart-artifacts-loc', 'Lines of Code', 'lines_of_code', true);
    """
