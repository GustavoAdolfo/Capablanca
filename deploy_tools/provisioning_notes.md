Provisionamento de um novo site
===============================

## Pacotes necessários:

+ nginx
+ python 3.*
+ virtuanenv + pip
+ git

## Configuração do Nginx Virtual Host

+ veja nginx.template.conf
+ substituir SITENAME pelo nome apropriado do site
+ substituir USERNAME pelo nome apropriado do usuário

## Serviço Systemd

+ veja gunicorn.systemd.template.service
+ substituir SITENAME e USERNAME pelos respectivos valores apropriados

## Estrutura de pastas

+ /home/USERNAME/
|----- sites/
|      |------- SITENAME/
|      |        |----------- database
|      |        |----------- source
|      |        |----------- static
|      |        |----------- virtualenv

