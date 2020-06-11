# Simplemooc

Projeto criado pelo curso de Python e Django realizado na plataforma da Udemy

Este projeto pode usar qualquer ambiente que suporte as bibliotecas do arquivo requirements.txt.

Mas no curso criamos um ambiente para desenvolvimento usando o virtualenv, segue o comando para criação do ambiente com o virtualenv.

$ python -m venv nomedoambiente

# Deploy em ambiente de produção

Foi realizados estudos para implementar o projeto em um ambiente de produção, 
o deploy foi realizado em um Fedora 32, utilizando Docker, Gunicorn, Nginx, PostgreSQL.

* Rotina utilizada no preparo do ambiente de produção
1. Preparar uma imagem com os requisitos de serviços:
	- Baixar a imagem do centos 8 do repositório oficial do docker.
	- Criar um container, atualizar o linux no container e instalar o nano.
	- Instalar o python 3: dnf install python3
	- Instalar o gunicorn no container: pip3 install gunicorn
	- comitar o container para uma nova imagem (Criei com o nome "centos-to-django"")
2. Cria o volume para aplicação:
	- docker volume create django-app01
	- Por padrão os volumes ficam em /var/lib/docker/volumes/__data/django-app01>
3. Iniciar um container com volume do app:
	- docker run -d -p 8000:8000 --name django-app01 --mount source=django-app01,target=/django-app01 centos-to-django
4. Preparar e rodar a aplicação:
	- Clonar a aplicação no diretório do host que corresponde ao volume.
	- Configurar o postgresql do host para conversar com o container(liberar ip no pg_hba.conf)
	- Configurar o settings.py (Variáveis e banco)
	- Criei um arquivo run-deploy.sh na pasta deploy no mesmo diretório do app, com o conteúdo a seguir:
		
	\#!/usr/bin/env bash<br>
	cd /django-app01/simplemooc/<br>
	NOW=$(TZ=":America/Sao_Paulo" date +"%d-%m-%Y_%H-%M-%S")<br>
	LOG=/django-app01/deploy/logs/logs-deploy-${NOW}.log<br>
	echo "==================== Encerrando os processos gunicorn ====================" >> $LOG<br>
	ps aux | grep gunicorn | awk '{print $2;}' | xargs kill -9 2>/dev/null >> $LOG<br>
	echo "==================== Instalando requerimentos ====================" >> $LOG<br>
	pip3 install -r requeriments.txt >> $LOG<br>
	echo "==================== Rodando migrações do banco de dados ====================" >> $LOG<br>
	python3 manage.py migrate >> $LOG<br>
	echo "==================== Gerando arquivos estáticos ====================" >> $LOG<br>
	python3 manage.py collectstatic --noinput >> $LOG<br>
	echo "==================== Iniciando o gunicorn ====================" >> $LOG<br>
	gunicorn --bind :8000 --workers 3 simplemooc.wsgi:application >> $LOG<br>

	- Rodar o arquivo run-deploy.sh: docker exec -d -w /django-app01/deploy/ django-app01 ./run-deploy.sh
	- Configurar o virtualhost no nginx (É importante verificar a permissão dos diretos dos arquivos estáticos, toda a arvore deve estar acessível).
	
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