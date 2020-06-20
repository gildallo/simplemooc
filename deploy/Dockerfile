# Puxa a imagem mais atual do CentOS
FROM centos

# Atualiza o CentOS
RUN dnf update -y

# Instala o python 3
RUN dnf install python3 -y

# Instala o Gunicorn
RUN pip3 install gunicorn