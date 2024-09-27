def processLines(lines) -> str:
    # Lire les entrées initiales
    N = int(lines[0])  # Nombre de sprints
    T = int(lines[1])  # Nombre de tâches initiales dans le backlog
    
    backlog = T  # Nombre de tâches dans le backlog

    # Traiter chaque sprint
    for i in range(2, N + 2):
        V, U = map(int, lines[i].split())  # Lire le nombre de tâches validées et modifiées
        backlog -= V  # Soustraire les tâches validées
        backlog += U  # Ajouter ou supprimer des tâches

    # Retourner OK si le backlog est vide, sinon KO
    if backlog == 0:
        return "OK"
    else:
        return "KO"
