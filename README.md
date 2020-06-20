# Simplemooc

Projeto criado pelo curso de Python e Django realizado na plataforma da Udemy

Este projeto pode usar qualquer ambiente que suporte as bibliotecas do arquivo requirements.txt.

Mas no curso criamos um ambiente para desenvolvimento usando o virtualenv, segue o comando para criação do ambiente com o virtualenv.

$ python -m venv nomedoambiente

# Deploy em ambiente de produção

Foi realizados estudos para implementar o projeto em um ambiente de produção diferenciado, 
o deploy foi realizado em um Fedora 32, utilizando Docker, Gunicorn, Nginx, PostgreSQL.

* Rotina utilizada no preparo do ambiente de produção
1. Construir uma imagem com os requisitos mínimos usando o Dockerfile da pasta deploy, usar o comando "docker build" no mesmo diretório do arquivo Dockerfile:
	- $ docker build -t centos-to-django .
2. Cria o volume para aplicação e ajustar configurações necessárias:
	- docker volume create django-app-02
	- aplicar as permissões no diretório do volume no host para o usuário 
	- Por padrão os volumes ficam em /var/lib/docker/volumes/__data/django-app-02
    - Clonar a aplicação no volume criado.
	- Configurar o postgresql do host para conversar com o container(liberar ip no pg_hba.conf)
	- Configurar o settings.py (Variáveis e banco)
	- Conferir se os serviços utilizados estão onlines: Postgres, Nginx
3. Foi utilizado a aplicação Portainer para gerenciar o docker, use as seguintes opções na criação do container:
    - Usar a imagem centos-to-django
    - port publishing: 8002:8002
    - EntryPoint: deploy/run-app.sh
    - workking dir: /django-app-02/simplemooc
    - Console: (-i -t)
    - Volume no container: /django-app-02
4. Configurar NGINX:
	- Configurar o virtualhost no nginx (É importante verificar a permissão dos diretos dos arquivos estáticos, toda a arvore deve estar acessível).
	- Recarregar configurações do nginx: nginx -s reload

# Comandos docker estudados
- Baixando uma imagem docker/centos do repositório oficial.<br>
$ docker pull centos
- Listar as imagens disponíveis no pc<br>
$ docker image ls
- Criar um container com opção interativa<br>
$ docker run -it <nome-da-imagem>
- Listar Containers ativos<br>
$ docker ps
- Lista todos os containers(ativados e desativados)<br>
$ docker ps -a
- Acessar um container em execução<br>
$ docker attach <id-ou-apelido>
- Salvar alterações realizadas na imagem<br>
$ docker commit <ID/apelido> <nome-da-nova-imagem>

- Remover imagem local<br>
$ docker rmi ID_ou_nome_da_imagem
- Criar um container com apelido<br>
$ docker run --name <apelido> <nome-da-imagem>
- Remover um container<br>
$ docker rm <id-ou-apelido>
- Informações de uso de hardware do container<br>
$ docker stats <id-ou-apelido>
- Informações uteis do container<br>
$ docker inspect <id-ou-apelido>
- Mapeando uma porta do container com o host<br>
$ docker run -it -p 8080:80 <id-ou-apelido>
- Executar container em segundo plano(Parametro -d)<br>
$ docker run -d <nome-da-imagem>
- Executar comando em modo interativo sem estar dentro do container<br>
$ docker exec -it <id-ou-apelido> <comando>
- Limpar o que não é usado<br>
$ docker system prune
- Criando Volume<br>
$ docker volume create django-app01
Observação: Os volume são criados por padrão no diretório do docker: /var/lib/docker/volumes/
- Iniciando um container com um volume<br>
$ docker run -d --name django-app01 --mount source=app01,target=/django-app01 centos-to-django