import os

# Cette fonction construit un chemin absolu vers un fichier de ressources
# basé sur l'emplacement du package '001.The Legend Of Turgut [Pygame]'.
# Elle évite les problèmes lorsque le script est lancé depuis un autre
# répertoire de travail.


def get_os_adapted_path(folder, file):
    """
    Return an absolute, OS-adapted path to a resource located in the
    game's folder structure.

    This uses the directory of this module as the project base so
    lookups work even if the process current working directory is
    different.

    :param folder: The folder name relative to the game root.
    :param file: The filename inside that folder.
    :return: Absolute path string.
    """
    # project_root: two levels up from this file (functions/ -> project root)
    module_dir = os.path.dirname(__file__)
    project_root = os.path.abspath(os.path.join(module_dir, os.pardir))

    # Build the path in an OS-safe way
    chemin = os.path.join(project_root, folder, file)

    # Normalize the path
    chemin = os.path.normpath(chemin)

    return chemin
