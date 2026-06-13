#!/usr/bin/env python3
from __future__ import annotations

import html
import sys
from datetime import datetime
from pathlib import Path


def human_size(size: int) -> str:
    units = ["B", "KB", "MB", "GB"]
    value = float(size)
    for unit in units:
        if value < 1024 or unit == units[-1]:
            if unit == "B":
                return f"{int(value)} {unit}"
            return f"{value:.1f} {unit}"
        value /= 1024
    return f"{size} B"


def collect_files(output_dir: Path) -> list[Path]:
    return sorted(
        (
            path
            for path in output_dir.iterdir()
            if path.is_file() and path.name != "index.html"
        ),
        key=lambda path: path.name.lower(),
    )


def render(output_dir: Path) -> str:
    files = collect_files(output_dir)
    rows = []
    for path in files:
        name = path.name
        stat = path.stat()
        rows.append(
            "        <tr>\n"
            f'          <td><a href="{html.escape(name, quote=True)}" download="{html.escape(name, quote=True)}" data-download>{html.escape(name)}</a></td>\n'
            f"          <td>{human_size(stat.st_size)}</td>\n"
            f"          <td>{datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d')}</td>\n"
            "        </tr>"
        )

    table_body = "\n".join(rows)
    generated = datetime.now().strftime("%Y-%m-%d")

    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Archive Test Files</title>
  <style>
    :root {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      color-scheme: light dark;
      --page-bg: #f6f7f9;
      --text: #1f2328;
      --muted: #57606a;
      --surface: #ffffff;
      --surface-muted: #f0f3f6;
      --border: #d0d7de;
      --row-border: #d8dee4;
      --link: #0969da;
      background: var(--page-bg);
      color: var(--text);
    }}
    @media (prefers-color-scheme: dark) {{
      :root {{
        --page-bg: #0d1117;
        --text: #e6edf3;
        --muted: #8b949e;
        --surface: #161b22;
        --surface-muted: #21262d;
        --border: #30363d;
        --row-border: #30363d;
        --link: #58a6ff;
      }}
    }}
    body {{
      margin: 0;
      padding: 32px;
    }}
    main {{
      max-width: 960px;
      margin: 0 auto;
    }}
    h1 {{
      margin: 0 0 8px;
      font-size: 30px;
      line-height: 1.2;
    }}
    p {{
      margin: 0 0 24px;
      color: var(--muted);
    }}
    table {{
      width: 100%;
      border-collapse: separate;
      border-spacing: 0;
      overflow: hidden;
      border: 1px solid var(--border);
      border-radius: 8px;
      background: var(--surface);
    }}
    th,
    td {{
      padding: 12px 14px;
      border-bottom: 1px solid var(--row-border);
      text-align: left;
      font-size: 14px;
    }}
    th {{
      background: var(--surface-muted);
      font-weight: 600;
    }}
    tr:last-child td {{
      border-bottom: 0;
    }}
    a {{
      color: var(--link);
      text-decoration: none;
      font-weight: 500;
    }}
    a:hover {{
      text-decoration: underline;
    }}
    @media (max-width: 640px) {{
      body {{
        padding: 20px;
      }}
      th,
      td {{
        padding: 10px;
      }}
    }}
  </style>
</head>
<body>
  <main>
    <h1>Archive Test Files</h1>
    <p>Generated on {generated}</p>
    <table>
      <thead>
        <tr>
          <th>File</th>
          <th>Size</th>
          <th>Modified</th>
        </tr>
      </thead>
      <tbody>
{table_body}
      </tbody>
    </table>
  </main>
  <script>
    document.querySelectorAll("a[data-download]").forEach((link) => {{
      link.addEventListener("click", async (event) => {{
        event.preventDefault();
        const response = await fetch(link.href);
        const blob = await response.blob();
        const url = URL.createObjectURL(blob);
        const anchor = document.createElement("a");
        anchor.href = url;
        anchor.download = link.getAttribute("download") || link.textContent.trim();
        document.body.appendChild(anchor);
        anchor.click();
        anchor.remove();
        URL.revokeObjectURL(url);
      }});
    }});
  </script>
</body>
</html>
"""


def main() -> int:
    output_dir = Path(sys.argv[1] if len(sys.argv) > 1 else ".files")
    output_dir.mkdir(parents=True, exist_ok=True)
    index_path = output_dir / "index.html"
    index_path.write_text(render(output_dir), encoding="utf-8")
    print(f"Wrote {index_path} with {len(collect_files(output_dir))} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
