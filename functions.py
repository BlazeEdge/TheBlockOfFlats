from rich.progress import track
import time

def load_anim():
    for i in track(range(100), description="Loading..."):
        time.sleep(0.05)

def banner():
    banner = """            
    [bold white]████████╗██╗  ██╗███████╗  ██████╗ ██╗      █████╗  █████╗ ██╗  ██╗   █████╗ ███████╗[/bold white]
    [bold white]╚══██╔══╝██║  ██║██╔════╝  ██╔══██╗██║     ██╔══██╗██╔══██╗██║ ██╔╝  ██╔══██╗██╔════╝[/bold white]
    [bold white]   ██║   ███████║█████╗    ██████╦╝██║     ██║  ██║██║  ╚═╝█████═╝   ██║  ██║█████╗  [/bold white]
    [bold white]   ██║   ██╔══██║██╔══╝    ██╔══██╗██║     ██║  ██║██║  ██╗██╔═██╗   ██║  ██║██╔══╝  [/bold white]
    [bold white]   ██║   ██║  ██║███████╗  ██████╦╝███████╗╚█████╔╝╚█████╔╝██║ ╚██╗  ╚█████╔╝██║     [/bold white]
    [bold white]   ╚═╝   ╚═╝  ╚═╝╚══════╝  ╚═════╝ ╚══════╝ ╚════╝  ╚════╝ ╚═╝  ╚═╝   ╚════╝ ╚═╝     [/bold white] 
    
    [bold cyan]███████╗██╗      █████╗ ████████╗ ██████╗[/bold cyan]
    [bold cyan]██╔════╝██║     ██╔══██╗╚══██╔══╝██╔════╝[/bold cyan]
    [bold cyan]█████╗  ██║     ███████║   ██║   ╚█████╗ [/bold cyan]
    [bold cyan]██╔══╝  ██║     ██╔══██║   ██║    ╚═══██╗[/bold cyan]
    [bold cyan]██║     ███████╗██║  ██║   ██║   ██████╔╝[/bold cyan]
    [bold cyan]╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═════╝ [/bold cyan]
    """
    return banner