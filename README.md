# # Test Python

Teste para a utilizando python com Flask + Mysql
## Instalação

O sistema foi esta modularizado com [docker](https://docs.docker.com/get-docker/)
## Mysql
Usaremos docker para criar um container do banco para isso devemos seguir os seguintes passos:
1- logue no dockerhub
```bash
docker login
```
2- baixe a imagen do oracle db
```bash
 docker pull mysql:5.7
```
3 - rode a imagen peguando a porta 3306 do container e apontando para 3306 do host e passando a senha do usuario de ambiente
 ```bash
 docker run -e MYSQL_ROOT_PASSWORD=root --name mysqlFlaskdev -d -p 3306:3306 mysql:5.7
```
#com isso ja temos uma instancia do mysql configurada na versão 5.7

## Python Flask
1-na pasta root desse projeto execute o seguinte comando para geração de uma imagen docker
```bash
build . -t pythonflaskdev
```
2- posteriomente crie um container a partir da imagen linkando com o container do banco mysql
```bash
docker run -p 5000:5000 --name pythondev --link mysqlFlaskdev:mysql -d pythonflaskdev```

#-pronto a aplicação ja esta disponivel para ser utilizada 
