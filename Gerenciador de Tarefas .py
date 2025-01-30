from customtkinter import CTk, CTkLabel, CTkEntry, CTkButton, CTkFrame  # type: ignore
import tkinter.messagebox as messagebox

# Inicializa a janela principal da aplicação
tela = CTk()
tela.geometry("900x600")  # Define o tamanho da janela
tela.title("Gerenciador de Tarefas PIKA")  # Define o título da janela

# Lista para armazenar as tarefas e variável para a tarefa selecionada
tarefas = []
tarefa_selecionada = None

def mostrar_tela_branca():
    """Exibe a tela principal do gerenciador de tarefas."""
    global frame_lista, entrada_tarefa, frame_botoes, titulo_lista, status_label
    
    # Remove todos os widgets da janela atual (limpa a tela)
    for widget in tela.winfo_children():
        widget.destroy()

    # Cria divisórias laterais para organização visual
    divisoria_lateral_esquerda = CTkLabel(tela, text="", width=1.7, height=600, bg_color="silver")
    divisoria_lateral_esquerda.place(relx=0.20, rely=0, anchor="nw")

    divisoria_lateral_direita = CTkLabel(tela, text="", width=1.7, height=600, bg_color="silver")
    divisoria_lateral_direita.place(relx=0.80, rely=0, anchor="nw")

    # Campo de entrada para adicionar tarefas
    entrada_tarefa = CTkEntry(tela, placeholder_text="Nova tarefa", width=300)
    entrada_tarefa.grid(row=0, column=1, padx=20, pady=20, sticky="ew")

    # Área para exibição da lista de tarefas
    frame_lista = CTkFrame(tela)
    frame_lista.grid(row=1, column=1, padx=20, pady=10, sticky="nsew")

    # Título da lista de tarefas
    titulo_lista = CTkLabel(tela, text="Lista de Tarefas", font=("Arial", 16))
    titulo_lista.grid(row=0, column=1, padx=20, pady=(10, 0), sticky="nw")

    # Criando um frame para agrupar os botões
    frame_botoes = CTkFrame(tela)
    frame_botoes.grid(row=0, column=0, rowspan=2, padx=20, pady=20, sticky="ns")

    # Botão para adicionar nova tarefa
    botao_adicionar = CTkButton(frame_botoes, text="Adicionar", command=adicionar_tarefa)
    botao_adicionar.grid(row=0, column=0, pady=10, sticky="ew")

    # Botão para editar uma tarefa existente
    botao_editar = CTkButton(frame_botoes, text="Editar", command=editar_tarefa)
    botao_editar.grid(row=1, column=0, pady=10, sticky="ew")

    # Botão para remover uma tarefa
    botao_remover = CTkButton(frame_botoes, text="Remover", command=remover_tarefa)
    botao_remover.grid(row=2, column=0, pady=10, sticky="ew")

    # Label para exibir mensagens de status
    status_label = CTkLabel(tela, text="", font=("Arial", 12))
    status_label.grid(row=2, column=1, padx=20, pady=10, sticky="w")

    # Configuração para redimensionamento automático
    tela.grid_columnconfigure(1, weight=1)
    tela.grid_rowconfigure(1, weight=1)

def atualizar_lista():
    """Atualiza a exibição da lista de tarefas."""
    for widget in frame_lista.winfo_children():
        widget.destroy()

    if not tarefas:
        # Exibe mensagem quando não há tarefas
        label_vazio = CTkLabel(frame_lista, text="Nenhuma tarefa adicionada.", font=("Arial", 14))
        label_vazio.pack(padx=10, pady=10)

    # Exibe todas as tarefas cadastradas
    for idx, tarefa in enumerate(tarefas):
        label_tarefa = CTkLabel(frame_lista, text=tarefa, font=("Arial", 12))
        label_tarefa.pack(anchor="w", padx=10, pady=2)
        label_tarefa.bind("<Button-1>", lambda e, idx=idx: selecionar_tarefa(idx))

def selecionar_tarefa(idx):
    """Seleciona uma tarefa para edição ou remoção."""
    global tarefa_selecionada
    tarefa_selecionada = idx
    entrada_tarefa.delete(0, CTk.END)
    entrada_tarefa.insert(0, tarefas[idx])
    status_label.configure(text=f"Tarefa selecionada: {tarefas[idx]}")

def adicionar_tarefa():
    """Adiciona uma nova tarefa à lista."""
    tarefa = entrada_tarefa.get().strip()
    if tarefa:
        tarefas.append(tarefa)
        atualizar_lista()
        entrada_tarefa.delete(0, CTk.END)
        status_label.configure(text="Tarefa adicionada com sucesso.")
    else:
        status_label.configure(text="Por favor, insira uma tarefa válida.")

def editar_tarefa():
    """Edita a tarefa selecionada."""
    global tarefa_selecionada
    if tarefa_selecionada is not None:
        nova_tarefa = entrada_tarefa.get().strip()
        if nova_tarefa:
            tarefas[tarefa_selecionada] = nova_tarefa
            atualizar_lista()
            entrada_tarefa.delete(0, CTk.END)
            status_label.configure(text="Tarefa editada com sucesso.")
            tarefa_selecionada = None
        else:
            status_label.configure(text="Por favor, insira uma tarefa válida.")
    else:
        status_label.configure(text="Nenhuma tarefa selecionada para edição.")

def remover_tarefa():
    """Remove a tarefa selecionada."""
    global tarefa_selecionada
    if tarefa_selecionada is not None:
        if messagebox.askokcancel("Remover Tarefa", f"Tem certeza que deseja remover a tarefa '{tarefas[tarefa_selecionada]}'?"):
            del tarefas[tarefa_selecionada]
            atualizar_lista()
            entrada_tarefa.delete(0, CTk.END)
            status_label.configure(text="Tarefa removida com sucesso.")
            tarefa_selecionada = None
    else:
        status_label.configure(text="Nenhuma tarefa selecionada para remoção.")

# Criação dos campos de login
titulo = CTkLabel(tela, text="Sistema de Login", font=("Arial", 20))
titulo.pack(pady=70)

usuario = CTkEntry(tela, placeholder_text="Usuário", width=300)
usuario.pack(pady=20)

senha = CTkEntry(tela, placeholder_text="Senha", width=300, show="*")
senha.pack(pady=20)

def login():
    """Verifica as credenciais e exibe a tela de tarefas."""
    nome_usuario = usuario.get().strip()
    senha_usuario = senha.get().strip()
    if nome_usuario and senha_usuario:
        mostrar_tela_branca()
    else:
        messagebox.showerror("Erro de Login", "Por favor, insira um nome de usuário e senha válidos.")

botao = CTkButton(tela, text="Login", width=300, command=login)
botao.pack(pady=70)

# Inicia a interface gráfica
tela.mainloop()
