import json
import os
from datetime import datetime
from rich import print
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, IntPrompt, Confirm
from rich.progress import track, Progress, SpinnerColumn, TextColumn
import time

console = Console()
TASKS_FILE = "tasks.json"


class RichTaskManager:
    """Gestionnaire de tâches avec interface Rich"""

    def __init__(self):
        self.console = Console()
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """Charge les tâches depuis le fichier JSON"""
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

    def save_tasks(self):
        """Sauvegarde les tâches dans le fichier JSON"""
        with open(TASKS_FILE, "w", encoding="utf-8") as f:
            json.dump(self.tasks, f, indent=2, ensure_ascii=False)

    def show_header(self):
        """Affiche l'en-tête du programme"""
        self.console.print("*" * 60, style="bold blue")
        self.console.print("*" + " " * 58 + "*", style="bold blue")
        self.console.print(
            "*      🗂️  GESTIONNAIRE DE TÂCHES RICH      *", style="bold blue")
        self.console.print(
            "*        Gérez vos tâches avec style !        *", style="bold blue")
        self.console.print("*" + " " * 58 + "*", style="bold blue")
        self.console.print("*" * 60, style="bold blue")
        self.console.print()

    def show_menu(self):
        """Affiche le menu principal"""
        menu_table = Table(show_header=False, box=None, padding=(0, 2))
        menu_table.add_column("Option", style="bold cyan")
        menu_table.add_column("Description", style="white")

        menu_table.add_row("1", "📋 Voir les tâches")
        menu_table.add_row("2", "➕ Ajouter une tâche")
        menu_table.add_row("3", "✅ Marquer comme complétée")
        menu_table.add_row("4", "🗑️  Supprimer une tâche")
        menu_table.add_row("5", "📊 Statistiques")
        menu_table.add_row("6", "🚪 Quitter")

        self.console.print("*" * 50, style="bold green")
        self.console.print(
            "*           [bold green]Menu Principal[/]           *", style="bold green")
        self.console.print("*" * 50, style="bold green")
        self.console.print(menu_table)
        self.console.print("*" * 50, style="bold green")

    def list_tasks(self):
        """Affiche toutes les tâches dans un tableau Rich"""
        if not self.tasks:
            self.console.print("*" * 50, style="bold yellow")
            self.console.print(
                "*        📝 Liste des Tâches        *", style="bold yellow")
            self.console.print("*" * 50, style="bold yellow")
            self.console.print(
                "*                                  *", style="bold yellow")
            self.console.print(
                "*   [yellow]Aucune tâche trouvée.[/]   *", style="bold yellow")
            self.console.print(
                "*  Ajoutez une tâche pour commencer ! *", style="bold yellow")
            self.console.print(
                "*                                  *", style="bold yellow")
            self.console.print("*" * 50, style="bold yellow")
            return

        # Création du tableau
        table = Table(title="📋 Liste des Tâches", title_style="bold blue")
        table.add_column("ID", justify="center", style="cyan", width=6)
        table.add_column("Statut", justify="center", width=8)
        table.add_column("Tâche", style="white", min_width=30)
        table.add_column("Créée le", style="dim", width=16)

        for task in self.tasks:
            # Définition du statut avec couleur
            if task["completed"]:
                status = "[green]✅ Fait[/]"
                task_text = f"[dim strikethrough]{task['title']}[/]"
            else:
                status = "[yellow]⏳ En cours[/]"
                task_text = task['title']

            table.add_row(
                str(task["id"]),
                status,
                task_text,
                task["created"]
            )

        self.console.print(table)
        self.console.print()

    def add_task(self):
        """Ajoute une nouvelle tâche avec animation"""
        title = Prompt.ask("[green]📝 Titre de la nouvelle tâche[/]")

        if not title.strip():
            self.console.print("[red]❌ Le titre ne peut pas être vide![/]")
            return

        # Animation de chargement
        with Progress(
            SpinnerColumn(),
            TextColumn("[bold blue]Création de la tâche..."),
            console=self.console,
            transient=True
        ) as progress:
            task = progress.add_task("Creating...", total=None)
            time.sleep(1)

        # Création de la tâche
        new_task = {
            "id": len(self.tasks) + 1,
            "title": title.strip(),
            "completed": False,
            "created": datetime.now().strftime("%d/%m/%Y %H:%M")
        }

        self.tasks.append(new_task)
        self.save_tasks()

        # Message de succès
        self.console.print("*" * 50, style="bold green")
        self.console.print(
            "*              Succès              *", style="bold green")
        self.console.print("*" * 50, style="bold green")
        self.console.print(
            "*                                  *", style="bold green")
        self.console.print(
            f"* [green]✅ Tâche ajoutée avec succès ![/] *", style="bold green")
        self.console.print(f"*   {title[:30]:<30}   *", style="bold green")
        self.console.print(
            "*                                  *", style="bold green")
        self.console.print("*" * 50, style="bold green")

    def complete_task(self):
        """Marque une tâche comme complétée"""
        if not self.tasks:
            self.console.print("[yellow]📝 Aucune tâche à compléter[/]")
            return

        self.list_tasks()

        try:
            task_id = IntPrompt.ask(
                "[cyan]🎯 ID de la tâche à marquer comme complétée[/]")

            for task in self.tasks:
                if task["id"] == task_id:
                    if task["completed"]:
                        self.console.print(
                            f"[yellow]⚠️  La tâche {task_id} est déjà complétée![/]")
                        return

                    task["completed"] = True
                    self.save_tasks()

                    # Animation de succès
                    self.console.print("[green]🎉 Félicitations ![/]")
                    self.console.print("*" * 50, style="bold green")
                    self.console.print(
                        "*           Tâche Terminée          *", style="bold green")
                    self.console.print("*" * 50, style="bold green")
                    self.console.print(
                        "*                                   *", style="bold green")
                    self.console.print(
                        f"* [green]✅ Tâche #{task_id} marquée comme complétée[/] *", style="bold green")
                    self.console.print(
                        f"*   {task['title'][:29]:<29}   *", style="bold green")
                    self.console.print(
                        "*                                   *", style="bold green")
                    self.console.print("*" * 50, style="bold green")
                    return

            self.console.print(f"[red]❌ Tâche #{task_id} non trouvée[/]")

        except (ValueError, KeyboardInterrupt):
            self.console.print("[red]❌ ID invalide ou opération annulée[/]")

    def delete_task(self):
        """Supprime une tâche"""
        if not self.tasks:
            self.console.print("[yellow]📝 Aucune tâche à supprimer[/]")
            return

        self.list_tasks()

        try:
            task_id = IntPrompt.ask("[red]🗑️  ID de la tâche à supprimer[/]")

            for i, task in enumerate(self.tasks):
                if task["id"] == task_id:
                    # Confirmation
                    confirm = Confirm.ask(
                        f"[red]⚠️  Êtes-vous sûr de vouloir supprimer:[/]\n[white]'{task['title']}'[/]"
                    )

                    if confirm:
                        self.tasks.pop(i)
                        self.save_tasks()

                        self.console.print("*" * 50, style="bold red")
                        self.console.print(
                            "*             Suppression            *", style="bold red")
                        self.console.print("*" * 50, style="bold red")
                        self.console.print(
                            "*                                    *", style="bold red")
                        self.console.print(
                            f"* [red]🗑️  Tâche #{task_id} supprimée[/]       *", style="bold red")
                        self.console.print(
                            f"*   {task['title'][:30]:<30}   *", style="bold red")
                        self.console.print(
                            "*                                    *", style="bold red")
                        self.console.print("*" * 50, style="bold red")
                    else:
                        self.console.print(
                            "[yellow]⏹️  Suppression annulée[/]")
                    return

            self.console.print(f"[red]❌ Tâche #{task_id} non trouvée[/]")

        except (ValueError, KeyboardInterrupt):
            self.console.print("[red]❌ ID invalide ou opération annulée[/]")

    def show_statistics(self):
        """Affiche les statistiques des tâches"""
        if not self.tasks:
            self.console.print("[yellow]📊 Aucune statistique disponible[/]")
            return

        total_tasks = len(self.tasks)
        completed_tasks = sum(1 for task in self.tasks if task["completed"])
        pending_tasks = total_tasks - completed_tasks
        completion_rate = (completed_tasks / total_tasks) * \
            100 if total_tasks > 0 else 0

        # Tableau de statistiques
        stats_table = Table(title="📊 Statistiques des Tâches",
                            title_style="bold magenta")
        stats_table.add_column("Métrique", style="cyan", width=20)
        stats_table.add_column("Valeur", style="white", width=15)
        stats_table.add_column("Détail", style="dim", width=20)

        stats_table.add_row("📝 Total", str(total_tasks), "tâches créées")
        stats_table.add_row("✅ Complétées", str(
            completed_tasks), f"{completion_rate:.1f}% du total")
        stats_table.add_row("⏳ En cours", str(pending_tasks),
                            f"{100-completion_rate:.1f}% du total")

        self.console.print(stats_table)

        # Barre de progression visuelle
        if total_tasks > 0:
            progress_text = f"Progression: {completed_tasks}/{total_tasks} tâches complétées"
            with Progress(console=self.console) as progress:
                task = progress.add_task(
                    "[green]" + progress_text, total=total_tasks)
                progress.update(task, completed=completed_tasks)
                time.sleep(1)

    def run(self):
        """Boucle principale du programme"""
        self.console.clear()
        self.show_header()

        while True:
            try:
                self.show_menu()

                choice = Prompt.ask(
                    "[bold yellow]🎯 Choisissez une option[/]",
                    choices=["1", "2", "3", "4", "5", "6"],
                    default="1"
                )

                self.console.print()  # Ligne vide

                if choice == "1":
                    self.list_tasks()
                elif choice == "2":
                    self.add_task()
                elif choice == "3":
                    self.complete_task()
                elif choice == "4":
                    self.delete_task()
                elif choice == "5":
                    self.show_statistics()
                elif choice == "6":
                    # Animation de sortie
                    self.console.print("*" * 60, style="bold cyan")
                    self.console.print(
                        "*                    Au revoir                    *", style="bold cyan")
                    self.console.print("*" * 60, style="bold cyan")
                    self.console.print(
                        "*                                                  *", style="bold cyan")
                    self.console.print(
                        "* [bold blue]👋 Merci d'avoir utilisé le Gestionnaire![/] *", style="bold cyan")
                    self.console.print(
                        "*                  À bientôt !                    *", style="bold cyan")
                    self.console.print(
                        "*                                                  *", style="bold cyan")
                    self.console.print("*" * 60, style="bold cyan")
                    break

                # Pause avant le prochain menu
                self.console.print("\n" + "─" * 60)
                Prompt.ask(
                    "[dim]Appuyez sur Entrée pour continuer...[/]", default="")
                self.console.clear()
                self.show_header()

            except KeyboardInterrupt:
                self.console.print(
                    "\n[yellow]👋 Programme interrompu. Au revoir ![/]")
                break
            except Exception as e:
                self.console.print(f"[red]❌ Erreur: {e}[/]")


if __name__ == "__main__":
    manager = RichTaskManager()
    manager.run()
