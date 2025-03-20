import subprocess
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

# Initialize rich console
console = Console()

def get_hwid():
    try:
        # Run the ioreg command to get the hardware UUID
        hwid = subprocess.check_output(
            "ioreg -rd1 -c IOPlatformExpertDevice | awk -F '\"' '/IOPlatformUUID/ {print $4}'",
            shell=True
        ).decode().strip()
        return hwid
    except Exception as e:
        return f"[red]Error retrieving HWID:[/red] {e}"

if __name__ == "__main__":
    console.print("\n[cyan]🔍 Fetching Mac Hardware ID...[/cyan]\n")

    hwid = get_hwid()

    # Display HWID in plain text while keeping styled UI
    panel = Panel(
        Text(f"Mac HWID:\n\n{hwid}", justify="center"),  # No color on HWID
        title="[bold yellow]✅ Hardware ID Retrieved[/bold yellow]",
        border_style="bright_blue"
    )

    console.print(panel)
