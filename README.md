# ENGLISH VERSION:
# File Hashing Tool
## Overview:
This is a simple tool developed in Python to calculate the SHA-256 hash of a file provided by the user. The SHA-256 hash is a unique string of characters that represents the content of the file. This tool can be useful for verifying the integrity and authenticity of files, as well as for security and encryption purposes.

## How It Works:
- The tool prompts the user for the path to the file they want to hash.
- It then reads the file in blocks of data and calculates the SHA-256 hash of the file's content.
- The resulting hash is displayed in the terminal.

## Why Calculate a File Hash?
Calculating the hash of a file serves to produce a unique and fixed representation of that file's content. This is useful for several reasons:
- **Integrity Verification:** By calculating the hash of a file, we can compare the resulting hash with a previously known hash to ensure that the file's content has not been altered.
- **Authentication:** The hash of a file can serve as a digital signature, allowing us to verify the authenticity of the file and confirm its origin.
- **Security:** The use of hashes is fundamental in many security, encryption, and authentication protocols, where data integrity is crucial.

## Step-by-Step Guide:

### 1. Installing Ubuntu on VMware:
- Download the Ubuntu ISO image.
- Open VMware and create a new virtual machine.
- Follow the instructions to install Ubuntu on the virtual machine.

### 2. Installing Visual Studio Code on Linux:
Visual Studio Code is available for various Linux distributions. By downloading and using Visual Studio Code, you agree to the license terms and privacy statement.
For other Linux distributions or more installation options, refer to the Visual Studio Code page.

### 3. Cloning the Repository and Setting Up the Environment:
- Open Visual Studio Code.
- Clone this repository to your computer:
git clone https://github.com/fernandombmuniz/hashing_file.git
- Navigate to the project directory:
cd (your-project-directory)
- Create a virtual environment for the project:
python3 -m venv venv
- **What is a Virtual Environment?**
  A virtual environment is a self-contained directory that contains a Python interpreter and all the libraries necessary for a specific project. This allows you to isolate the project's dependencies from the system's installations, ensuring consistency and avoiding conflicts between different projects.
- **Why Use a Virtual Environment?**
  Using a virtual environment is considered a best practice in Python development because it:
  Ensures portability of the project across different environments.
  Avoids dependency conflicts between projects.
  Facilitates dependency management and version control.
  Enables easy reproduction of the project's environment.
- Activate the virtual environment:
  source venv/bin/activate

### 4. Creating the Python File `hash_files.py` and Code Explanation:
- Creating the Python File hash_files.py and Code Explanation:
  In Visual Studio Code, create a new file named hash_files.py.
  Copy and paste the provided Python code for the file hashing tool into this file.
  Python Code and Detailed Explanation:

  import hashlib

def calculate_hash(file_path):
    # Create a SHA-256 hash object
    sha256 = hashlib.sha256()
    # Open the file in binary mode and iterate over it in blocks of data
    with open(file_path, "rb") as f:
        while True:
            # Read a block of data from the file
            block = f.read(4096)
            # If there are no more blocks, exit the loop
            if not block:
                break
            # Update the hash object with the read block
            sha256.update(block)
    # Return the SHA-256 hash of the file as a hexadecimal string
    return sha256.hexdigest()

if __name__ == "__main__":
    # Prompt the user for the file path
    file_path = input("Enter the path to the file: ")
    try:
        # Calculate the hash of the file and display the result
        file_hash = calculate_hash(file_path)
        print(f"The SHA-256 hash of the file '{file_path}' is: {file_hash}")
    except FileNotFoundError:
        # Display an error message if the file is not found
        print("File not found.")

This Python code prompts the user for the path to the file they want to hash, reads the file in blocks of data, calculates the SHA-256 hash of the file's content, and then displays the resulting hash in the terminal.

5. Running the File Hashing Tool:
In the Visual Studio Code terminal, execute the Python file hash_files.py:
python3 hash_files.py

When prompted, provide the full path to the file you want to hash. For example:
Enter the path to the file: /home/your-username/path/to/your/file.txt

The SHA-256 hash of the provided file will be displayed in the terminal.

Real-World Use:
File Integrity Checking: Organizations and individuals can use file hashing tools to verify if files downloaded from the internet or received from external sources have been altered or corrupted.
Information Security: In the field of information security, calculating hashes is essential to ensure data integrity and information authenticity.
Backup Integrity Verification: Companies and individuals can use hashes to verify the integrity of data backups, ensuring that the data is recoverable and has not been corrupted.

# VERSÃO EM PORTUGUÊS:
# Ferramenta de Hashing de Arquivos

## Visão Geral:
Esta é uma ferramenta simples desenvolvida em Python para calcular o hash SHA-256 de um arquivo fornecido pelo usuário. O hash SHA-256 é uma sequência de caracteres única que representa o conteúdo do arquivo. Esta ferramenta pode ser útil para verificar a integridade e autenticidade de arquivos, bem como para fins de segurança e criptografia.

## Como Funciona:
- A ferramenta solicita ao usuário o caminho para o arquivo que deseja calcular o hash.
- Em seguida, ela lê o arquivo em blocos de dados e calcula o hash SHA-256 do conteúdo do arquivo.
- O hash resultante é exibido no terminal.

## Por que Calcular o Hash de um Arquivo?
O cálculo do hash de um arquivo serve para produzir uma representação única e fixa do conteúdo desse arquivo. Isso é útil por várias razões:
- **Verificação de Integridade:** Ao calcular o hash de um arquivo, podemos comparar a hash resultante com uma hash previamente conhecida para garantir que o conteúdo do arquivo não foi alterado.
- **Autenticação:** O hash de um arquivo pode servir como uma assinatura digital, permitindo que verifiquemos a autenticidade do arquivo e confirmemos sua origem.
- **Segurança:** O uso de hashes é fundamental em muitos protocolos de segurança, criptografia e autenticação, onde a integridade dos dados é crucial.

## Guia Passo a Passo:

### 1. Instalação do Ubuntu na VMware:
- Baixe a imagem ISO do Ubuntu.
- Abra o VMware e crie uma nova máquina virtual.
- Siga as instruções para instalar o Ubuntu na máquina virtual.

### 2. Instalação do Visual Studio Code no Linux:
O Visual Studio Code está disponível para várias distribuições Linux. Ao baixar e usar o Visual Studio Code, você concorda com os termos de licença e a declaração de privacidade.
Para outras distribuições Linux ou mais opções de instalação, consulte a página do Visual Studio.

### 3. Clonando o Repositório e Configurando o Ambiente:
- Abra o Visual Studio
- Clone este repositório para o seu computador:
git clone https://github.com/fernandombmuniz/hashing_file.git
- Navegue até o diretório do projeto:
cd (diretorio-do-seu-projeto)
- Crie um ambiente virtual para o projeto:
python3 -m venv venv
- O que é um Ambiente Virtual?
  Um ambiente virtual é um diretório autocontido que contém um interpretador Python e todas as bibliotecas necessárias para um projeto específico. Isso permite isolar as dependências do projeto das instalações do sistema, garantindo consistência e evitando conflitos entre diferentes projetos.
- Por que Usar um Ambiente Virtual?
  Usar um ambiente virtual é considerado uma prática recomendada no desenvolvimento Python porque:
  Garante portabilidade do projeto entre diferentes ambientes.
  Evita conflitos de dependência entre projetos.
  Facilita o gerenciamento de dependências e controle de versões.
  Permite fácil reprodução do ambiente do projeto.
- Vantagens de Usar um Ambiente Virtual:
- Isolamento: Cada projeto pode ter seu próprio conjunto de dependências, isolado de outros projetos e instalações do sistema.
Gerenciamento de Dependências: Gerencie facilmente as dependências do projeto, incluindo instalação, atualização e remoção.
- Controle de Versões: Garanta consistência especificando versões exatas de dependências para cada projeto.
- Reprodutibilidade: Reproduza o ambiente do projeto em diferentes sistemas, garantindo comportamento consistente em implantações.
- Ative o ambiente virtual:
  source venv/bin/activate

### 4. Criando o arquivo python `hash_files.py` e Explicação do código:
- Criando o Arquivo Python hash_files.py e Explicação do Código:
  No Visual Studio Code, crie um novo arquivo chamado hash_files.py.
  Copie e cole o código Python fornecido para a ferramenta de hashing de arquivos neste arquivo.
  Código Python e Explicação Detalhada:
  python
  import hashlib

  def calculate_hash(file_path):
      # Crie um objeto de hash SHA-256
      sha256 = hashlib.sha256()
      # Abra o arquivo em modo binário e itere sobre ele em blocos de dados
      with open(file_path, "rb") as f:
          while True:
              # Leia um bloco de dados do arquivo
              block = f.read(4096)
              # Se não houver mais blocos, saia do loop
              if not block:
                  break
              # Atualize o objeto de hash com o bloco lido
              sha256.update(block)
      # Retorne o hash SHA-256 do arquivo como uma string hexadecimal
      return sha256.hexdigest()

  if __name__ == "__main__":
      # Solicite ao usuário o caminho para o arquivo
      file_path = input("Digite o caminho para o arquivo: ")
      try:
          # Calcule o hash do arquivo e exiba o resultado
          file_hash = calculate_hash(file_path)
          print(f"O hash SHA-256 do arquivo '{file_path}' é: {file_hash}")
      except FileNotFoundError:
          # Exiba uma mensagem de erro se o arquivo não for encontrado
          print("Arquivo não encontrado.")
  Este código Python solicita ao usuário o caminho para o arquivo que eles desejam calcular o hash, lê o arquivo em blocos de dados, calcula o hash SHA-256 do conteúdo do arquivo e, em seguida, exibe o hash resultante no terminal.

5. Executando a Ferramenta de Hashing de Arquivos:
No terminal do Visual Studio Code, execute o arquivo Python hash_files.py:
python3 hash_files.py

Quando solicitado, forneça o caminho completo para o arquivo que deseja calcular o hash. Por exemplo:
Digite o caminho para o arquivo: /home/seu-nome-de-usuário/caminho/para/seu/arquivo.txt
O hash SHA-256 do arquivo fornecido será exibido no terminal.

Uso no Mundo Real:
Verificação de Integridade de Arquivos: Organizações e indivíduos podem usar ferramentas de hashing de arquivos para verificar se os arquivos baixados da Internet ou recebidos de fontes externas foram alterados ou corrompidos.
Segurança da Informação: No campo da segurança da informação, o cálculo de hashes é essencial para garantir a integridade dos dados e a autenticidade das informações.
Verificação de Integridade de Backup: Empresas e indivíduos podem usar hashes para verificar a integridade dos backups de dados, garantindo que os dados sejam recuperáveis e não tenham sido corrompidos.