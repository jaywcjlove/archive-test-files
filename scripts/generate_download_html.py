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
      padding-bottom: 6rem;
    }}
    h1 {{
      margin: 0 0 8px;
      font-size: 30px;
      line-height: 1.2;
    }}
    .header > div:last-child {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .header {{
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      gap: 16px;
      margin-bottom: 24px;
      padding-top: 4rem;
    }}
    p {{
      margin: 0;
      color: var(--muted);
    }}
    .repo-link {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      min-height: 32px;
      padding: 0 8px;
      border: 1px solid var(--border);
      border-radius: 6px;
      background: var(--surface);
      white-space: nowrap;
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
      main {{
        padding-bottom: 1rem;
      }}
      .header {{
        display: block;
        padding-top: 0rem;
      }}
      .repo-link {{
        margin-top: 12px;
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
    <div class="header">
      <div>
        <h1>Archive Test Files</h1>
        <p>Generated on {generated}</p>
      </div>
      <div>
        <a class="repo-link" href="https://wangchujiang.com/zipora/" target="_blank" title="Zipora for macOS" rel="noopener noreferrer">
          <img src="https://wangchujiang.com/zipora/assets/logo.png" alt="Zipora" width="21" height="21" />
          <span>Zipora</span>
        </a>
        <a class="repo-link" href="https://github.com/jaywcjlove/archive-test-files" target="_blank" rel="noopener noreferrer">
          <svg aria-hidden="true" viewBox="0 0 16 16" width="18" height="18">
            <path fill="currentColor" d="M8 0C3.58 0 0 3.67 0 8.2c0 3.63 2.29 6.7 5.47 7.79.4.08.55-.18.55-.4 0-.2-.01-.86-.01-1.56-2.01.38-2.53-.5-2.69-.96-.09-.24-.48-.96-.82-1.15-.28-.15-.68-.52-.01-.53.63-.01 1.08.59 1.23.84.72 1.24 1.87.89 2.33.68.07-.53.28-.89.51-1.1-1.78-.21-3.64-.91-3.64-4.03 0-.89.31-1.62.82-2.19-.08-.21-.36-1.04.08-2.16 0 0 .67-.22 2.2.84A7.4 7.4 0 0 1 8 3.99c.68 0 1.36.09 2 .28 1.52-1.06 2.19-.84 2.19-.84.44 1.12.16 1.95.08 2.16.51.57.82 1.3.82 2.19 0 3.13-1.87 3.82-3.65 4.03.29.26.54.76.54 1.53 0 1.1-.01 1.99-.01 2.26 0 .22.15.48.55.4A8.1 8.1 0 0 0 16 8.2C16 3.67 12.42 0 8 0Z"></path>
          </svg>
          <span>GitHub</span>
        </a>
      </div>
    </div>
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
