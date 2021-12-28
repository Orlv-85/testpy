## **Подготовка и запуск проекта**

Склонировать репозиторий на локальную машину:

**_https://github.com/Orlv-85/testpy.git_**

Для запуска вебсервиса (на ubuntu):

Установите docker на локальную машину:

**_sudo apt install docker.io_**

Установите docker-compose на локальную машину:

**_sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose_**

Войдите в директорию, в которую скопирован файл:

**_docker-compose.yml_**

Чтобы создать образы и развернуть контейнеры введите команды:

**_docker-compose build .
docker-compose up_**


