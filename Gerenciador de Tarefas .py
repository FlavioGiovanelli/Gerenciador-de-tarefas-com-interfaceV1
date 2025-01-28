from customtkinter import CTk, CTkLabel, CTkEntry, CTkButton, CTkFrame # type: ignore
import tkinter.messagebox as messagebox

# Inicializa a janela principal
tela = CTk()
tela.geometry("900x600")
tela.title("Gerenciador de Tarefas PIKA")

tarefas = []
tarefa_selecionada = None

def mostrar_tela_branca():
    global frame_lista, entrada_tarefa, frame_botoes, titulo_lista, status_label
    # Remove todos os widgets da janela atual
    for widget in tela.winfo_children():
        widget.destroy()

    # Configuração das divisórias
    divisoria_lateral_esquerda = CTkLabel(tela, text="", width=1.7, height=600, bg_color="silver")
    divisoria_lateral_esquerda.place(relx=0.20, rely=0, anchor="nw")

    divisoria_lateral_direita = CTkLabel(tela, text="", width=1.7, height=600, bg_color="silver")
    divisoria_lateral_direita.place(relx=0.80, rely=0, anchor="nw")

    # Campo de entrada para tarefas
    entrada_tarefa = CTkEntry(tela, placeholder_text="Nova tarefa", width=300)
    entrada_tarefa.grid(row=0, column=1, padx=20, pady=20, sticky="ew")

    # Frame para exibir a lista de tarefas
    frame_lista = CTkFrame(tela)
    frame_lista.grid(row=1, column=1, padx=20, pady=10, sticky="nsew")

    # Título da lista de tarefas
    titulo_lista = CTkLabel(tela, text="Lista de Tarefas", font=("Arial", 16))
    titulo_lista.grid(row=0, column=1, padx=20, pady=(10, 0), sticky="nw")

    # Botões para adicionar, editar e remover tarefas
    frame_botoes = CTkFrame(tela)
    frame_botoes.grid(row=0, column=0, rowspan=2, padx=20, pady=20, sticky="ns")

    botao_adicionar = CTkButton(frame_botoes, text="Adicionar", command=adicionar_tarefa)
    botao_adicionar.grid(row=0, column=0, pady=10, sticky="ew")

    botao_editar = CTkButton(frame_botoes, text="Editar", command=editar_tarefa)
    botao_editar.grid(row=1, column=0, pady=10, sticky="ew")

    botao_remover = CTkButton(frame_botoes, text="Remover", command=remover_tarefa)
    botao_remover.grid(row=2, column=0, pady=10, sticky="ew")

    # Label de status para feedback do usuário
    status_label = CTkLabel(tela, text="", font=("Arial", 12))
    status_label.grid(row=2, column=1, padx=20, pady=10, sticky="w")

    tela.grid_columnconfigure(1, weight=1)
    tela.grid_rowconfigure(1, weight=1)

def atualizar_lista():
    for widget in frame_lista.winfo_children():
        widget.destroy()

    if not tarefas:
        label_vazio = CTkLabel(frame_lista, text="Nenhuma tarefa adicionada.", font=("Arial", 14))
        label_vazio.pack(padx=10, pady=10)

    for idx, tarefa in enumerate(tarefas):
        label_tarefa = CTkLabel(frame_lista, text=tarefa, font=("Arial", 12))
        label_tarefa.pack(anchor="w", padx=10, pady=2)
        label_tarefa.bind("<Button-1>", lambda e, idx=idx: selecionar_tarefa(idx))

def selecionar_tarefa(idx):
    global tarefa_selecionada
    tarefa_selecionada = idx
    entrada_tarefa.delete(0, CTk.END)
    entrada_tarefa.insert(0, tarefas[idx])
    status_label.configure(text=f"Tarefa selecionada: {tarefas[idx]}")

def adicionar_tarefa():
    tarefa = entrada_tarefa.get().strip()
    if tarefa:
        tarefas.append(tarefa)
        atualizar_lista()
        entrada_tarefa.delete(0, CTk.END)
        status_label.configure(text="Tarefa adicionada com sucesso.")
    else:
        status_label.configure(text="Por favor, insira uma tarefa válida.")

def editar_tarefa():
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

# Cria e posiciona os widgets de login
titulo = CTkLabel(tela, text="Sistema de Login", font=("Arial", 20))
titulo.pack(pady=70)

usuario = CTkEntry(tela, placeholder_text="Usuário", width=300)
usuario.pack(pady=20)

senha = CTkEntry(tela, placeholder_text="Senha", width=300, show="*")
senha.pack(pady=20)

def login():
    nome_usuario = usuario.get().strip()
    senha_usuario = senha.get().strip()
    if nome_usuario and senha_usuario:
        print(f"Nome de usuário: {nome_usuario}, Senha: {senha_usuario}")
        mostrar_tela_branca()
    else:
        messagebox.showerror("Erro de Login", "Por favor, insira um nome de usuário e senha válidos.")

botao = CTkButton(tela, text="Login", width=300, command=login)
botao.pack(pady=70)

# Executa o loop principal
tela.mainloop()