import os
import re
from datetime import datetime

def define_env(env):
    """Define macros and variables for MkDocs macros plugin."""

    @env.macro
    def git_last_modified(page):
        """Return last git commit date for current page."""
        if not page.file or not page.file.src_path:
            return ""
        try:
            import subprocess
            result = subprocess.run(
                ["git", "log", "-1", "--format=%ad", "--date=short", "--", page.file.src_path],
                capture_output=True, text=True, cwd=os.getcwd()
            )
            if result.returncode == 0 and result.stdout.strip():
                return result.stdout.strip()
        except Exception:
            pass
        return ""

    @env.macro
    def git_contributors(page):
        """Return contributor count for current page."""
        if not page.file or not page.file.src_path:
            return ""
        try:
            import subprocess
            result = subprocess.run(
                ["git", "shortlog", "-sn", "--", page.file.src_path],
                capture_output=True, text=True, cwd=os.getcwd()
            )
            if result.returncode == 0 and result.stdout.strip():
                lines = result.stdout.strip().split('\n')
                return str(len(lines))
        except Exception:
            pass
        return ""

    @env.macro
    def current_year():
        return str(datetime.now().year)

    @env.macro
    def severity_badge(severity):
        """Generate a colored severity badge."""
        colors = {
            "critical": "#dc2626",
            "high": "#ea580c",
            "medium": "#ca8a04",
            "low": "#16a34a",
            "info": "#2563eb",
        }
        color = colors.get(severity.lower(), "#6b7280")
        return f'<span style="background:{color};color:white;padding:2px 8px;border-radius:4px;font-size:0.75rem;font-weight:600;text-transform:uppercase;">{severity}</span>'

    @env.macro
    def mitre_link(technique_id):
        """Generate MITRE ATT&CK link."""
        return f"https://attack.mitre.org/techniques/{technique_id.replace('.', '/')}"

    @env.macro
    def cve_link(cve_id):
        """Generate CVE link."""
        return f"https://cve.mitre.org/cgi-bin/cvename.cgi?name={cve_id}"

    @env.macro
    def tool_link(tool_name):
        """Generate standard tool reference links."""
        tools = {
            "nmap": "https://nmap.org",
            "burp": "https://portswigger.net/burp",
            "wireshark": "https://www.wireshark.org",
            "metasploit": "https://www.metasploit.com",
            "bloodhound": "https://bloodhound.specterops.io",
            "sqlmap": "http://sqlmap.org",
            "ffuf": "https://github.com/ffuf/ffuf",
            "feroxbuster": "https://github.com/epi052/feroxbuster",
            "nuclei": "https://nuclei.projectdiscovery.io",
            "crackmapexec": "https://github.com/porchetta-industries/crackmapexec",
            "impacket": "https://github.com/fortra/impacket",
            "linpeas": "https://github.com/carlospolop/PEASS-ng/tree/master/linPEAS",
            "winpeas": "https://github.com/carlospolop/PEASS-ng/tree/master/winPEAS",
            "sharphound": "https://github.com/BloodHoundAD/BloodHound/tree/master/Collectors/SharpHound",
            "rubeus": "https://github.com/GhostPack/Rubeus",
            "mimikatz": "https://github.com/gentilkiwi/mimikatz",
        }
        return tools.get(tool_name.lower(), "#")

    @env.macro
    def lab_link(lab_name):
        """Generate practice lab links."""
        labs = {
            "thm": "https://tryhackme.com",
            "htb": "https://hackthebox.com",
            "vulnhub": "https://www.vulnhub.com",
            "pentesterlab": "https://pentesterlab.com",
            "portswigger": "https://portswigger.net/web-security",
            "rootme": "https://www.root-me.org",
            "picoctf": "https://picoctf.org",
            "attackdefense": "https://attackdefense.com",
            "hackthebox_academy": "https://academy.hackthebox.com",
        }
        return labs.get(lab_name.lower(), "#")

    @env.macro
    def command_block(cmd, description="", lang="bash"):
        """Render a styled command block with optional description."""
        desc_html = f'<div class="cmd-desc">{description}</div>' if description else ""
        return f'''
<div class="command-block">
    {desc_html}
    <pre><code class="language-{lang}">{cmd}</code></pre>
</div>
'''

    @env.macro
    def note_box(title, content, type="note"):
        """Render a styled note/admonition box."""
        icons = {
            "note": "📝",
            "tip": "💡",
            "warning": "⚠️",
            "danger": "🚨",
            "example": "🧪",
            "opsec": "🕵️",
        }
        icon = icons.get(type, "📝")
        return f'''
<div class="note-box note-{type}">
    <div class="note-title">{icon} {title}</div>
    <div class="note-content">{content}</div>
</div>
'''

    @env.macro
    def table_from_dict(data, headers=None):
        """Convert list of dicts to markdown table."""
        if not data:
            return ""
        if headers is None:
            headers = list(data[0].keys())
        header_row = "| " + " | ".join(headers) + " |"
        sep_row = "| " + " | ".join(["---"] * len(headers)) + " |"
        rows = []
        for row in data:
            rows.append("| " + " | ".join(str(row.get(h, "")) for h in headers) + " |")
        return "\n".join([header_row, sep_row] + rows)

    @env.macro
    def checklist(items):
        """Render a checklist."""
        if isinstance(items, str):
            items = [i.strip() for i in items.split("\n") if i.strip()]
        return "\n".join(f"- [ ] {item}" for item in items)

    @env.macro
    def crosslink(page_path, text=None):
        """Generate internal crosslink with automatic title resolution."""
        if text:
            return f"[{text}]({page_path})"
        return f"[{page_path}]({page_path})"

    env.variables.update({
        "site_name": "CySec",
        "author": "Malik Azad",
        "github_url": "https://github.com/malik-azad/CySec",
        "current_year": str(datetime.now().year),
    })