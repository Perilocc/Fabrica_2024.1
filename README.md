# POKE API
Projeto CRUD Django Rest que consome a PokeApi e obtêm dados dos pokemons disponíveis na API.
O CRUD permite a criação, leitura, atualização e exclusão de informações relacionados aos Pokémon.

# Introdução
A PokeAPI (https://pokeapi.co/) é uma API pública que fornece uma vasta quantidade de informações sobre Pokémon, incluindo detalhes sobre os próprios Pokémon, tipos, habilidades, movimentos, entre outros. Este CRUD foi desenvolvido para interagir com a PokeAPI, permitindo operações básicas de manipulação de dados (CREATE, READ, UPDATE, DELETE)

# Como Instalar
- Inicialmente você precisará clonar este repositório em (https://github.com/Perilocc/Fabrica_2024.1.git)
- Em seguida entre no seu repositório onde se localizam os arquivos principais do projeto
- Utilize o comando: cd nome_do_seu_repositorio . Pois se você não estiver na pasta do repositório ao instalar o requirements.txt, resultará em erro.
- Crie um terminal e escreva: python -m venv venv ou python3 -m venv venv
- Depois ative a venv com: .\venv\Scripts\activate 
- Após ativar sua venv instale as dependências presentes no arquivo requirements.txt: pip install -r requirements.txt
- Agora faça a Migração das tabelas para o banco de dados utilizando: python manage.py makemigrations
- E depois confirme as migrações com o comando: python manage.py migrate
- E pronto, você consegue acessar o servidor com o comando: python manage.py runserver
- 
# Pré-Requisitos
Certifique-se de ter as dependências presentes no requirements.txt após ativar a venv e prosseguir com os outros comandos
- Python 3
- Django 5.0.3
- Django REST FRAMEWORK
- Requests (Interações e avisos)
- Bem como outras dependências presentes no requirements.txt

# Utilização
- Ao entrar no link, disponibilizado ao rodar o servidor, https://pokeapi.co/ \n
- Você encontrará a interface de urls do Django, onde você incrementará a sua url principal com o elemento api/ resultando em > http://127.0.0.1:8000/api/
- Onde resultará na interface do Django Rest e clicando no link presente chamado de PokeApi, será redirecionado para a interface do CRUD Django Rest, em que você utilizará as funções básicas da CRUD.
- A partir daqui você utilizará seus conhecimentos para manusear essa api

# Métodos da CRUD
GET: Para recuperar dados.  
POST: Para criar novos registros.  
PUT ou PATCH: Para atualizar registros existentes.  
DELETE: Para excluir registros.

# Usando a API
- Para criar um pokemon na API, você precisará colocar um nome de pokemon válido e clicar no botão POST. Isso adicionará, caso o pokemon seja válido, o pokemon a interface da API.
- Para obter todos os dados de Pokemons presentes, utilize o url: http://127.0.0.1:8000/api/PokeApi/
- Para obter um Pokemon específico de todos os dados presentes, utilize a url anterior + /id_pokemon/, resultando em: http://127.0.0.1:8000/api/PokeApi/id_pokemon/
- Para deletar um pokemon acesse a url anterior com o seu id e clique no botão DELETE, isso deletará o pokemon do banco de dados.
- Para atualizar uma informação equivocada acerca de um pokemon, a url com seu id : http://127.0.0.1:8000/api/PokeApi/id_pokemon/ e no campo preenchido com os dados altere o quiser e clique no botão PUT, equivalente ao UPDATE

# Usando a API no Insomnia
Utilize o insomnia apenas se tiver conhecimento prévio, Pois o insomnia acessará a API com o url: http://127.0.0.1:8000/api/PokeApi/
- E repita os comandos utilizados no tópico Usando a API.
- Para acessar todos os registros: http://127.0.0.1:8000/api/PokeApi/ e para registros específicos: http://127.0.0.1:8000/api/PokeApi/id_pokemon
- Para deletar um registro, troque o método para DELETE e coloque a url: http://127.0.0.1:8000/api/PokeApi/id_pokemon e envie
- Para Criar um novo registro, troque para o método POST e coloque a url: http://127.0.0.1:8000/api/PokeApi/ . Escreva o atributo nome e o nome do pokemon desejado, ex: Snorlax
- Para atualizar, mudar ou alterar algum atributo de um pokemon troque o método para PUT e use a url: http://127.0.0.1:8000/api/PokeApi/id_pokemon/ e crie os campos necessários com seus respectivos valores ou apenas o campo que deseja mudar e seu valor.

# Boa Sorte e Divirta-se!
Obrigado por explorar este CRUD Django REST para a PokeAPI! Desejamos a você boa sorte em seus projetos e esperamos que esta API seja útil em suas jornadas de desenvolvimento BackEnd. Lembre-se de fazer bom uso das informações sobre os Pokémon e de continuar explorando o vasto mundo dos Pokémons presentes nessa API. Se precisar de assistência ou tiver alguma dúvida, não hesite em me contatar. Divirta-se codificando e continue explorando a PokeAPI para se tornar um verdadeiro mestre Pokémon ou um Dev BackEnd rsrsrs.
