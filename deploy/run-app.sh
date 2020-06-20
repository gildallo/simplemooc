#!/usr/bin/env bash
NOW=$(TZ=":America/Sao_Paulo" date +"%d-%m-%Y_%H-%M-%S")
LOG=deploy/logs/logs-deploy-${NOW}.log
echo "==================== Encerrando os processos ==========" >> $LOG
ps aux | grep gunicorn | awk '{print $2;}' | xargs kill -9 2>/dev/null >> $LOG
echo "==================== Instalando requerimentos ================" >> $LOG
pip3 install -r requirements.txt >> $LOG
echo "==================== Rodando migrações do banco ===================" >> $LOG
python3 manage.py migrate >> $LOG
echo "==================== Gerando arquivos estáticos ===================" >> $LOG
python3 manage.py collectstatic --noinput >> $LOG
echo "==================== Iniciando o Gunicorn ===================" >> $LOG
gunicorn --bind :8002 --workers 3 --log-level debug --error-logfile /django-app-02/simplemooc/deploy/logs/gunicorn-error.log --access-logfile /django-app-02/simplemooc/deploy/logs/gunicorn-access.log simplemooc.wsgi:application